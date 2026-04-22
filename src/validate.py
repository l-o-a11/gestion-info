# Funciones de validación de campos

def validar_id(id_valor):
    """Valida que el ID sea un número entero positivo"""
    try:
        id_int = int(id_valor)
        if id_int <= 0:
            return False, "El ID debe ser un número positivo"
        return True, id_int
    except ValueError:
        return False, "El ID debe ser un número entero"


def validar_nombre(nombre):
    """Valida que el nombre no esté vacío y sea texto"""
    if not nombre or not isinstance(nombre, str):
        return False, "El nombre no puede estar vacío"
    if len(nombre) < 2:
        return False, "El nombre debe tener al menos 2 caracteres"
    return True, nombre.strip()


def validar_email(email):
    """Valida que el email tenga formato correcto"""
    if not email or '@' not in email or '.' not in email:
        return False, "El email debe contener @ y un dominio válido"
    if len(email) < 5:
        return False, "El email es demasiado corto"
    return True, email.strip().lower()


def validar_edad(edad):
    """Valida que la edad sea un número entre 0 y 120"""
    try:
        edad_int = int(edad)
        if edad_int < 0 or edad_int > 120:
            return False, "La edad debe estar entre 0 y 120 años"
        return True, edad_int
    except ValueError:
        return False, "La edad debe ser un número entero"
