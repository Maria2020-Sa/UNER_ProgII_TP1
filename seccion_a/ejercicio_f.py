import re

def contrasena_valida(contrasena):
    # Validación de longitud
    if len(contrasena) < 6 or len(contrasena) > 20:
        return False
    
    # Validación de al menos un número
    if not re.search(r'\d', contrasena):
        return False
    
    # Validación de al menos dos letras mayúsculas
    if len(re.findall(r'[A-Z]', contrasena)) < 2:
        return False
    
    # Validación de al menos un carácter especial
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena):
        return False
    
    # Validación de que no contenga espacios
    if ' ' in contrasena:
        return False
    
    return True


print(contrasena_valida("A1@bcD"))  # True
print(contrasena_valida("abc123"))  # False
