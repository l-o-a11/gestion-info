"""
Módulo de integración con pandas para exportación y filtrado de registros.
Proporciona funcionalidades avanzadas de reportes, exportación a CSV y filtrado de datos.
"""

import pandas as pd
import os
from datetime import datetime


class ManagerReportes:
    """Gestor de reportes y exportación de datos con pandas"""
    
    def __init__(self, data_dir=None):
        """
        Inicializa el gestor de reportes.
        
        Args:
            data_dir (str, optional): Directorio donde se almacenarán los reportes.
                                      Si no se especifica, usa la carpeta 'data' del proyecto.
        """
        if data_dir is None:
            # Usar la carpeta data existente en la raíz del proyecto
            data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        self.data_dir = data_dir
        
        # Verificar que la carpeta existe (no crear automáticamente)
        if not os.path.exists(data_dir):
            raise ValueError(f"La carpeta de datos no existe: {data_dir}")
    
    def exportar_a_csv(self, registros, *args, nombre_archivo=None, **kwargs):
        """
        Exporta registros a archivo CSV con opciones configurables.
        
        Args:
            registros (list): Lista de registros (diccionarios)
            *args: Argumentos posicionales adicionales (para extensibilidad)
            nombre_archivo (str, optional): Nombre personalizado del archivo
            **kwargs: Argumentos adicionales:
                - incluir_timestamp (bool): Incluir timestamp en nombre de archivo (default: True)
                - separador (str): Separador CSV (default: ',')
                - encoding (str): Codificación (default: 'utf-8')
        
        Returns:
            tuple: (éxito: bool, mensaje: str, ruta_archivo: str)
        """
        if not registros:
            return False, "Error: No hay registros para exportar", None
        
        try:
            # Configurar opciones
            incluir_timestamp = kwargs.get('incluir_timestamp', True)
            separador = kwargs.get('separador', ',')
            encoding = kwargs.get('encoding', 'utf-8')
            
            # Crear DataFrame
            df = pd.DataFrame(registros)
            
            # Generar nombre de archivo
            if nombre_archivo is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") if incluir_timestamp else ""
                nombre_archivo = f"reporte_registros_{timestamp}.csv" if timestamp else "reporte_registros.csv"
            elif not nombre_archivo.endswith('.csv'):
                nombre_archivo += '.csv'
            
            ruta_completa = os.path.join(self.data_dir, nombre_archivo)
            
            # Exportar a CSV
            df.to_csv(ruta_completa, sep=separador, encoding=encoding, index=False)
            
            mensaje = f"Reporte exportado exitosamente: {ruta_completa}"
            return True, mensaje, ruta_completa
            
        except Exception as e:
            return False, f"Error al exportar CSV: {str(e)}", None
    
    def filtrar_registros(self, registros, *args, **kwargs):
        """
        Filtra y ordena registros usando pandas DataFrame.
        
        Args:
            registros (list): Lista de registros
            *args: Argumentos posicionales (para extensibilidad)
            **kwargs: Criterios de filtro:
                - edad_min (int): Edad mínima
                - edad_max (int): Edad máxima
                - nombre (str): Búsqueda en nombre (substring)
                - email (str): Búsqueda en email (substring)
                - ordenar_por (str): Campo para ordenar (default: 'id')
                - orden_asc (bool): Ascendente (True) o descendente (False) (default: True)
        
        Returns:
            tuple: (éxito: bool, mensaje: str, registros_filtrados: list)
        """
        if not registros:
            return False, "No hay registros para filtrar", []
        
        try:
            df = pd.DataFrame(registros)
            df_filtrado = df.copy()
            
            # Aplicar filtros
            if 'edad_min' in kwargs:
                edad_min = kwargs['edad_min']
                df_filtrado = df_filtrado[df_filtrado['edad'] >= edad_min]
            
            if 'edad_max' in kwargs:
                edad_max = kwargs['edad_max']
                df_filtrado = df_filtrado[df_filtrado['edad'] <= edad_max]
            
            if 'nombre' in kwargs:
                nombre_busqueda = kwargs['nombre'].lower()
                df_filtrado = df_filtrado[df_filtrado['nombre'].str.lower().str.contains(nombre_busqueda)]
            
            if 'email' in kwargs:
                email_busqueda = kwargs['email'].lower()
                df_filtrado = df_filtrado[df_filtrado['email'].str.lower().str.contains(email_busqueda)]
            
            # Ordenar
            ordenar_por = kwargs.get('ordenar_por', 'id')
            orden_asc = kwargs.get('orden_asc', True)
            
            if ordenar_por in df_filtrado.columns:
                df_filtrado = df_filtrado.sort_values(by=ordenar_por, ascending=orden_asc)
            
            registros_resultado = df_filtrado.to_dict(orient='records')
            
            mensaje = f"Filtrado exitoso: {len(registros_resultado)} registros encontrados"
            return True, mensaje, registros_resultado
            
        except Exception as e:
            return False, f"Error al filtrar: {str(e)}", []
    
    def generar_reporte_estadistico(self, registros, *args, **kwargs):
        """
        Genera un reporte estadístico de los registros.
        
        Args:
            registros (list): Lista de registros
            *args: Argumentos posicionales (para extensibilidad)
            **kwargs: Opciones adicionales
        
        Returns:
            dict: Estadísticas del dataset
        """
        if not registros:
            return {}
        
        try:
            df = pd.DataFrame(registros)
            
            estadisticas = {
                'total_registros': len(df),
                'total_personas_unicas': len(df['id'].unique()),
                'edad_promedio': round(df['edad'].mean(), 2),
                'edad_minima': int(df['edad'].min()),
                'edad_maxima': int(df['edad'].max()),
                'edad_mediana': int(df['edad'].median()),
                'desv_std_edad': round(df['edad'].std(), 2)
            }
            
            return estadisticas
            
        except Exception as e:
            return {'error': str(e)}
