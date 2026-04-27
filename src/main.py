# # print ("Sistema listo")  
from colorama import init, Fore, Style, Back
import os
from menu import mostrar_menu, new_register_interactivo, list_records_interactivo, buscar_registro_interactivo, update_record_interactivo, delete_record_interactivo
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
            new_register_interactivo(gestor, DATA_FILE)
        
        elif opcion == "2":
            list_records_interactivo(gestor)
        
        elif opcion == "3":
            buscar_registro_interactivo(gestor)
                
        elif opcion == "4":
            update_record_interactivo(gestor, DATA_FILE)
            
        elif opcion == "5":
            delete_record_interactivo(gestor, DATA_FILE)
                
        elif opcion == "6":
            print(Fore.MAGENTA + Style.BRIGHT + "\n¡Hasta luego!\n")
            break
        
        else:
            print(Fore.RED + " Opción no válida. Por favor, seleccione entre 1 y 5")
        
        input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()
