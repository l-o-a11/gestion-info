from colorama import init, Fore, Style, Back
import os
from file import save_data

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


def new_register_interactivo(gestor, data_file):
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
            save_data(data_file, gestor.list_records())
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

def update_record_interactivo(gestor, data_file):
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
            save_data(data_file, gestor.list_records())
        else:
            print(Fore.RED + f" {mensaje}")
    
    except ValueError:
        print(Fore.RED + " El ID debe ser un número")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")

def delete_record_interactivo(gestor, data_file):
    """Elimina un registro por ID"""
    try:
        id_eliminar = int(input("\nIngrese ID a eliminar: ").strip())
        exito, mensaje = gestor.delete_record(id_eliminar)
        
        if exito:
            print(Fore.GREEN + f" {mensaje}")
            # Guardar datos en archivo JSON
            save_data(data_file, gestor.list_records())
        else:
            print(Fore.RED + f" {mensaje}")
    
    except ValueError:
        print(Fore.RED + " El ID debe ser un número")
    except Exception as e:
        print(Fore.RED + f" Error: {e}")

