# # print ("Sistema listo")  
from colorama import init, Fore, Style, Back
import os

# init(autoreset=True)

# # Crear adgoritmo de almacenamiento de datos en lista y tiene, manejo de funciones, orden de mayor a menor, listas, menu interactivo y manejo de errores

# print (Fore.CYAN +"===================================================================================")
# print( Back.BLUE +"======================Manejo de listas y errores====================================")
# print (Style.BRIGHT + Fore.WHITE +"===================================================================================")
# try: 
#     print("Bienvenido al sistema de gestión de información")
# except ValueError:
#     print("Error: Valor no válido. Por favor, ingrese un número.")

from service import GestorRegistros
from file import load_data, save_data

init(autoreset=True)

# Ruta del archivo JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'records.json')

def mostrar_menu():
    """Muestra el menú principal"""
    print(Fore.CYAN + "=" * 70)
    print(Fore.CYAN + "SISTEMA DE GESTIÓN DE INFORMACIÓN")
    print(Fore.CYAN + "=" * 70)
    print(Fore.GREEN + "1. Crear nuevo registro")
    print(Fore.GREEN + "2. Listar todos los registros")
    print(Fore.GREEN + "3. Buscar registro por ID")
    print(Fore.GREEN + "4. Actualizar registro por ID")
    print(Fore.GREEN + "5. Eliminar registro por ID")
    print(Fore.GREEN + "6. Salir")
    print(Fore.CYAN + "=" * 70)


def new_register_interactivo(gestor):
    """Permite crear un registro interactivamente"""
    print("\n" + Fore.YELLOW + "--- CREAR NUEVO REGISTRO ---")
    
    try:
        id_persona = input("Ingrese ID (número): ").strip()
        nombre = input("Ingrese nombre: ").strip()
        email = input("Ingrese email: ").strip()
        edad = input("Ingrese edad: ").strip()
        
        exito, mensaje, registro = gestor.new_register(id_persona, nombre, email, edad)
        
        if exito:
            print(Fore.GREEN + f" {mensaje}")
            print(f"  ID: {registro['id']}")
            print(f"  Nombre: {registro['nombre']}")
            print(f"  Email: {registro['email']}")
            print(f"  Edad: {registro['edad']} años")
            
            # Guardar datos en archivo JSON
            save_data(DATA_FILE, gestor.list_records())
        else:
            print(Fore.RED + f" {mensaje}")
    
    except Exception as e:
        print(Fore.RED + f" Error inesperado: {e}")


def list_records_interactivo(gestor):
    """Muestra todos los registros registrados"""
    registros = gestor.list_records()
    
    if not registros:
        print(Fore.YELLOW + "No hay registros registrados aún.")
        return
    
    print(" " + Fore.YELLOW + "LISTA DE REGISTROS")
    print("-" * 70)
    print(f"{'ID':<5} {'Nombre':<20} {'Email':<25} {'Edad':<5}")
    print("-" * 70)
    
    for registro in registros:
        print(f"{registro['id']:<5} {registro['nombre']:<20} {registro['email']:<25} {registro['edad']:<5}")
    


def buscar_registro_interactivo(gestor):
    """Busca un registro por ID"""
    try:
        id_buscar = int(input("\nIngrese ID a buscar: ").strip())
        registro = gestor.search_record(id_buscar)
        
        if registro:
            print(Fore.GREEN + " Registro encontrado:")
            print(f"  ID: {registro['id']}")
            print(f"  Nombre: {registro['nombre']}")
            print(f"  Email: {registro['email']}")
            print(f"  Edad: {registro['edad']} años")
        else:
            print(Fore.RED + f" No se encontró registro con ID {id_buscar}")
    
    except ValueError:
        print(Fore.RED + " El ID debe ser un número")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")

def update_record_interactivo(gestor):
    """Actualiza un registro por ID"""
    try:
        id_actualizar = int(input("\nIngrese ID a actualizar: ").strip())
        nombre = input("Ingrese nuevo nombre (dejar vacío para no cambiar): ").strip()
        email = input("Ingrese nuevo email (dejar vacío para no cambiar): ").strip()
        edad = input("Ingrese nueva edad (dejar vacío para no cambiar): ").strip()
        
        # Solo enviar campos que se desean actualizar
        nombre = nombre if nombre else None
        email = email if email else None
        edad = edad if edad else None
        
        exito, mensaje = gestor.update_record(id_actualizar, nombre, email, edad)
        
        if exito:
            print(Fore.GREEN + f" {mensaje}")
            # Guardar datos en archivo JSON
            save_data(DATA_FILE, gestor.list_records())
        else:
            print(Fore.RED + f" {mensaje}")
    
    except ValueError:
        print(Fore.RED + " El ID debe ser un número")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")

def delete_record_interactivo(gestor):
    """Elimina un registro por ID"""
    try:
        id_eliminar = int(input("\nIngrese ID a eliminar: ").strip())
        exito, mensaje = gestor.delete_record(id_eliminar)
        
        if exito:
            print(Fore.GREEN + f" {mensaje}")
            # Guardar datos en archivo JSON
            save_data(DATA_FILE, gestor.list_records())
        else:
            print(Fore.RED + f" {mensaje}")
    
    except ValueError:
        print(Fore.RED + " El ID debe ser un número")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")


def main():
    """Función principal del programa"""
    print(Fore.MAGENTA + Style.BRIGHT + "\n¡Bienvenido al Sistema de Gestión de Información!\n")
    
    gestor = GestorRegistros()
    
    # Cargar datos desde archivo JSON
    print(Fore.CYAN + " Cargando datos desde el archivo...")
    registros_cargados = load_data(DATA_FILE)
    
    if registros_cargados:
        print(Fore.GREEN + f" Se cargaron {len(registros_cargados)} registros desde el archivo.\n")
        # Restaurar registros en el gestor
        for registro in registros_cargados:
            gestor.registros.append(registro)
            gestor.ids_unicos.add(registro['id'])
            gestor.emails_unicos.add(registro['email'])
    else:
        print(Fore.YELLOW + "  No hay registros previos. Se inicia con lista vacía.\n")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            new_register_interactivo(gestor)
        
        elif opcion == "2":
            list_records_interactivo(gestor)
        
        elif opcion == "3":
            buscar_registro_interactivo(gestor)
                
        elif opcion == "4":
            update_record_interactivo(gestor)
            
        elif opcion == "5":
            delete_record_interactivo(gestor)
                
        elif opcion == "6":
            print(Fore.MAGENTA + Style.BRIGHT + "\n¡Hasta luego!\n")
            break
        
        else:
            print(Fore.RED + " Opción no válida. Por favor, seleccione entre 1 y 5")
        
        input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()
