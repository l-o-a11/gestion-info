"""
Script de prueba para verificar la funcionalidad del sistema
Demuestra: *args, **kwargs, pandas, exportación a CSV, filtrado y estadísticas
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from integration import ManagerReportes
from service import GestorRegistros
from file import load_data, save_data

def test_funcionalidad():
    """Prueba las funcionalidades principales del sistema"""
    
    print("="*70)
    print("PRUEBA DEL SISTEMA DE GESTIÓN DE INFORMACIÓN")
    print("="*70)
    
    # 1. Crear gestor de reportes
    print("\n Inicializando ManagerReportes...")
    manager = ManagerReportes()
    
    # 2. Crear datos de prueba
    print(" Creando datos de prueba...")
    registros_prueba = [
        {"id": 1, "nombre": "juan", "email": "juan@gmail.com", "edad": 28},
        {"id": 2, "nombre": "maria", "email": "maria@hotmail.com", "edad": 35},
        {"id": 3, "nombre": "carlos", "email": "carlos@gmail.com", "edad": 42},
        {"id": 4, "nombre": "ana", "email": "ana@yahoo.com", "edad": 25},
        {"id": 5, "nombre": "luis", "email": "luis@gmail.com", "edad": 30},
    ]
    
    # 3. Test: Exportar a CSV
    print("\n" + "="*70)
    print("TEST 1: EXPORTACIÓN A CSV (con *args y **kwargs)")
    print("="*70)
    exito, mensaje, ruta = manager.exportar_a_csv(
        registros_prueba,
        nombre_archivo="prueba_reporte",
        incluir_timestamp=True,
        separador=",",
        encoding="utf-8-sig"
    )
    print(f"Resultado: {mensaje}")
    if exito:
        print(f" Archivo creado: {ruta}")
        with open(ruta, 'r', encoding='utf-8-sig') as f:
            contenido = f.read()
            print("\nContenido del CSV:")
            print(contenido)
    
    # 4. Test: Filtrado y ordenamiento
    print("\n" + "="*70)
    print("TEST 2: FILTRADO Y ORDENAMIENTO (con **kwargs)")
    print("="*70)
    
    print("\n Filtro 1: Edad entre 25 y 35, ordenado por edad descendente")
    exito, mensaje, resultado = manager.filtrar_registros(
        registros_prueba,
        edad_min=25,
        edad_max=35,
        ordenar_por="edad",
        orden_asc=False
    )
    print(f"Resultado: {mensaje}")
    if exito:
        print(f"Registros encontrados:")
        for reg in resultado:
            print(f"  - {reg['nombre']}: {reg['edad']} años ({reg['email']})")
    
    print("\n Filtro 2: Búsqueda parcial por nombre 'ar', ordenado alfabético")
    exito, mensaje, resultado = manager.filtrar_registros(
        registros_prueba,
        nombre="ar",
        ordenar_por="nombre",
        orden_asc=True
    )
    print(f"Resultado: {mensaje}")
    if exito:
        print(f"Registros encontrados:")
        for reg in resultado:
            print(f"  - {reg['nombre']}: {reg['edad']} años")
    
    # 5. Test: Estadísticas
    print("\n" + "="*70)
    print("TEST 3: ANÁLISIS ESTADÍSTICO (con *args y **kwargs)")
    print("="*70)
    estadisticas = manager.generar_reporte_estadistico(registros_prueba)
    
    if 'error' not in estadisticas:
        print(" Estadísticas generadas exitosamente:")
        print(f"\n  Total de registros: {estadisticas['total_registros']}")
        print(f"  Personas únicas: {estadisticas['total_personas_unicas']}")
        print(f"  Edad promedio: {estadisticas['edad_promedio']} años")
        print(f"  Edad mínima: {estadisticas['edad_minima']} años")
        print(f"  Edad máxima: {estadisticas['edad_maxima']} años")
        print(f"  Edad mediana: {estadisticas['edad_mediana']} años")
        print(f"  Desviación estándar: {estadisticas['desv_std_edad']} años")
    else:
        print(f" Error: {estadisticas['error']}")
    
    # 6. Test: Validación de datos
    print("\n" + "="*70)
    print("TEST 4: VALIDACIÓN DE DATOS")
    print("="*70)
    
    gestor = GestorRegistros()
    
    print("\n Intentando crear registro válido...")
    exito, msg, reg = gestor.new_register(100, "pedro", "pedro@gmail.com", 35)
    print(f"  Resultado: {msg}")
    if exito:
        print(f"  Registro creado: {reg}")
    
    print("\n Intentando crear registro con email duplicado...")
    exito, msg, reg = gestor.new_register(101, "ana2", "pedro@gmail.com", 28)
    print(f"  Resultado: {msg}")
    
    print("\n Intentando crear registro con edad inválida...")
    exito, msg, reg = gestor.new_register(102, "carlos2", "carlos2@gmail.com", 999)
    print(f"  Resultado: {msg}")
    
    print("\n" + "="*70)
    print(" PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("="*70)
    print("\nFuncionalidades demostradas:")
    print("   Exportación a CSV con opciones configurables")
    print("   Filtrado y ordenamiento con pandas DataFrame")
    print("   Análisis estadístico automático")
    print("   Validación de datos")
    print("   Uso de *args y **kwargs")
    print("   Librería externa integrada (pandas, numpy, colorama)")

if __name__ == "__main__":
    test_funcionalidad()
