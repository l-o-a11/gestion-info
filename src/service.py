# Servicio de gestión de registros en memoria
from validate import validar_id, validar_nombre, validar_email, validar_edad


class GestorRegistros:
    """Gestiona registros de personas en memoria con validaciones y sets para unicidad"""
    
    def __init__(self):
        self.registros = []  # Lista de diccionarios con registros
        self.ids_unicos = set()  # Set para IDs únicos
        self.emails_unicos = set()  # Set para emails únicos
    
    def new_register(self, id_persona, nombre, email, edad):
        """
        Crea un nuevo registro si cumple validaciones.
        Retorna (éxito, mensaje, registro)
        """
        # Validar ID
        valido, resultado = validar_id(id_persona)
        if not valido:
            return False, f"Error en ID: {resultado}", None
        id_persona = resultado
        
        # Validar que el ID no exista
        if id_persona in self.ids_unicos:
            return False, f"Error: El ID {id_persona} ya existe", None
        
        # Validar nombre
        valido, resultado = validar_nombre(nombre)
        if not valido:
            return False, f"Error en nombre: {resultado}", None
        nombre = resultado
        
        # Validar email
        valido, resultado = validar_email(email)
        if not valido:
            return False, f"Error en email: {resultado}", None
        email = resultado
        
        # Validar que el email no exista
        if email in self.emails_unicos:
            return False, f"Error: El email {email} ya está registrado", None
        
        # Validar edad
        valido, resultado = validar_edad(edad)
        if not valido:
            return False, f"Error en edad: {resultado}", None
        edad = resultado
        
        # Crear registro
        registro = {
            'id': id_persona,
            'nombre': nombre,
            'email': email,
            'edad': edad
        }
        
        # Agregar a memoria
        self.registros.append(registro)
        self.ids_unicos.add(id_persona)
        self.emails_unicos.add(email)
        
        return True, f"Registro creado exitosamente", registro
    
    def list_records(self):
        """Retorna la lista completa de registros"""
        return self.registros
    
    def search_record(self, id_persona):
        """Busca un registro por ID"""
        resultado = sorted(
            [r for r in self.registros if r['id'] == id_persona],
            key=lambda x: x['id'] # Lambda para crear funciones pequeñas y anónimas
        )
        return resultado[0] if resultado else None
    
    def update_record(self, id_persona, nombre=None, email=None, edad=None):
        """Actualiza un registro existente por ID"""
        for registro in self.registros:
            if registro['id'] == id_persona:
                # Validar y actualizar nombre
                if nombre is not None:
                    valido, resultado = validar_nombre(nombre)
                    if not valido:
                        return False, f"Error en nombre: {resultado}"
                    registro['nombre'] = resultado
                
                # Validar y actualizar email
                if email is not None:
                    valido, resultado = validar_email(email)
                    if not valido:
                        return False, f"Error en email: {resultado}"
                    if resultado != registro['email'] and resultado in self.emails_unicos:
                        return False, f"Error: El email {resultado} ya está registrado"
                    self.emails_unicos.discard(registro['email'])
                    registro['email'] = resultado
                    self.emails_unicos.add(resultado)
                
                # Validar y actualizar edad
                if edad is not None:
                    valido, resultado = validar_edad(edad)
                    if not valido:
                        return False, f"Error en edad: {resultado}"
                    registro['edad'] = resultado
                
                return True, "Registro actualizado exitosamente"
        
        return False, f"No se encontró registro con ID {id_persona}"
    
    def delete_record(self, id_persona):
        """Elimina un registro por ID"""
        for i, registro in enumerate(self.registros):
            if registro['id'] == id_persona:
                self.ids_unicos.discard(registro['id'])
                self.emails_unicos.discard(registro['email'])
                del self.registros[i]
                return True, "Registro eliminado exitosamente"
        return False, f"No se encontró registro con ID {id_persona}"
    
    def limpiar_registros(self):
        """Limpia todos los registros"""
        self.registros = []
        self.ids_unicos = set()
        self.emails_unicos = set()
