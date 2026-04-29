# Sistema de Gestión de Información

Un sistema interactivo de gestión de registros con funcionalidades avanzadas de reportes, filtrado y análisis estadístico utilizando Python y pandas.

## ✨ Características

### Gestión de Registros

- ✅ Crear nuevos registros (ID, nombre, email, edad)
- ✅ Listar todos los registros
- ✅ Buscar registro por ID
- ✅ Actualizar registros existentes
- ✅ Eliminar registros

### Exportación y Reportes

- ✅ **Exportar a CSV** con timestamp automático
- ✅ Opciones configurables (separador, encoding UTF-8 compatible con Excel)
- ✅ Almacenamiento en carpeta `data/`

### Filtrado y Ordenamiento Avanzado

- ✅ Filtrar por rango de edad (mínima y máxima)
- ✅ Búsqueda parcial en nombre y email
- ✅ Ordenar por cualquier campo (id, nombre, email, edad)
- ✅ Orden ascendente o descendente
- ✅ Implementado con **pandas DataFrame**

### Análisis Estadístico

- ✅ Total de registros y personas únicas
- ✅ Edad promedio, mínima, máxima y mediana
- ✅ Desviación estándar de edades

## 📋 Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes)

## 🚀 Instalación

### Paso 1: Clonar o descargar el proyecto

```bash
cd gestion-info
```

### Paso 2: Crear entorno virtual (Recomendado)

**Con venv estándar:**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🎮 Uso

### Ejecutar la aplicación

```bash
python src/main.py
```

### Menú Principal

```
======================================================================
SISTEMA DE GESTIÓN DE INFORMACIÓN
======================================================================
1. Crear nuevo registro
2. Listar todos los registros
3. Buscar registro por ID
4. Actualizar registro por ID
5. Eliminar registro por ID
6. Exportar registros a CSV
7. Filtrar y ordenar registros
8. Ver estadísticas
9. Salir
======================================================================
```

## 📊 Ejemplos de Uso

### 1️⃣ Crear Registro

```
Ingrese ID (número): 1
Ingrese nombre: Juan
Ingrese email: juan@example.com
Ingrese edad: 28
```

### 2️⃣ Exportar a CSV

- Selecciona opción 6
- Ingresa nombre de archivo (opcional, ej: "reporte_empleados")
- Se genera: `reporte_empleados_20260428_143022.csv`

### 3️⃣ Filtrar y Ordenar

- Selecciona opción 7
- **Edad mínima**: 25
- **Edad máxima**: 40
- **Buscar en nombre**: juan
- **Ordenar por**: edad
- **Orden**: D (descendente)

### 4️⃣ Ver Estadísticas

- Selecciona opción 8
- Se muestran automáticamente todos los cálculos estadísticos

## 📁 Estructura del Proyecto

```
gestion-info/
├── src/
│   ├── main.py              # Punto de entrada principal
│   ├── menu.py              # Funciones interactivas del menú
│   ├── service.py           # Lógica de gestión de registros
│   ├── integration.py       # Exportación, filtrado y análisis (pandas)
│   ├── file.py              # Operaciones con archivos JSON
│   └── validate.py          # Validaciones de datos
├── data/
│   └── records.json         # Base de datos en JSON
├── test/
│   └── tests.py             # Pruebas unitarias
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

## 📦 Dependencias

| Librería     | Versión | Uso                                    |
| ------------ | ------- | -------------------------------------- |
| **colorama** | 0.4.6   | Colores en consola (interfaz mejorada) |
| **pandas**   | 2.2.0   | DataFrames, filtrado, exportación CSV  |

## 💻 Características Técnicas

### Uso de \*args y \*\*kwargs

Implementado en `integration.py` para máxima flexibilidad:

```python
# Exportación con opciones personalizadas
manager.exportar_a_csv(
    registros,
    nombre_archivo="mi_reporte",
    incluir_timestamp=False,
    separador=";",
    encoding="utf-8"
)

# Filtrado con múltiples criterios
manager.filtrar_registros(
    registros,
    edad_min=25,
    edad_max=40,
    nombre="juan",
    email="@gmail.com",
    ordenar_por="edad",
    orden_asc=False
)
```

### Validaciones Integradas

- **ID**: Número entero positivo único
- **Nombre**: 2+ caracteres
- **Email**: Formato válido y único
- **Edad**: Entre 0 y 120 años

### Persistencia de Datos

- Almacenamiento en `data/records.json`
- Carga automática al iniciar
- Guardado automático tras cada operación

### Exportación CSV

- **Formato**: UTF-8 con BOM (compatible Excel Windows)
- **Timestamp automático**: `reporte_registros_20260428_143022.csv`
- **Personalizable**: Nombre, separador, encoding

## 🔧 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'pandas'"

```bash
pip install pandas
```

### Error: "ModuleNotFoundError: No module named 'colorama'"

```bash
pip install colorama
```

### Los datos no se guardan

- Verifica permisos en la carpeta `data/`
- Asegúrate de presionar Enter después de cada operación

### El CSV no se genera

- Verifica que exista la carpeta `data/`
- Comprueba permisos de escritura

## 📝 Licencia

Libre para uso educativo - 2026
