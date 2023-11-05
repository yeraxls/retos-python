import random
import string

def enter_password(num_characters = 0):
    num_characters = input("Longitud entre 8 y 16 caracteres: ")
    if not int(num_characters) in range(8, 17):
        print("Introduzca un valor válido")
        enter_password(num_characters)
    else: return num_characters

length = enter_password()

upper_case = input("Contiene mayusculas (Y / N): ")
upper_case = True if upper_case.lower() == "y" else False

lower_case = input("Contiene minusculas (Y / N): ")
lower_case = True if lower_case.lower() == "y" else False

digits = input("Contiene números (Y / N): ")
digits = True if digits.lower() == "y" else False

symbols = input("Contiene símbolos (Y / N): ")
symbols = True if symbols.lower() == "y" else False


def generate_password(length, uppercase, lowercase, digits, symbols):
    password_chars = ""
    if uppercase:
        password_chars += string.ascii_uppercase
    if lowercase:
        password_chars += string.ascii_lowercase
    if digits:
        password_chars += string.digits
    if symbols:
        password_chars += string.punctuation
    if not uppercase and not digits and not symbols:
        password_chars += string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_chars) for _ in range(length))

# Ejemplo de uso
password = generate_password(int(length), upper_case, lower_case, digits, symbols)
print(f"\nLa password generada es: {password}")