# Dada una cadena de caracteres, invierte solo todas las vocales de la cadena.
# Las vocales son ‘a’, ‘e’, ‘i’, ‘o’ y ‘u’, ‘A’, ‘E’, ‘I’, ‘O’, ‘U’.
def invert_vowels(text : str):
    vowels = "aeiouAEIOU"
    text_lst = list(text)
    pl = 0
    pr = len(text_lst) - 1

    while pl < pr:
        if text_lst[pl] in vowels and text_lst[pr] in vowels:
            text_lst[pl], text_lst[pr] = text_lst[pr], text_lst[pl]
            pl += 1
            pr -= 1
        elif text_lst[pl] in vowels:
            pr -= 1
        elif text_lst[pr] in vowels:
            pl += 1
        else :
            pl += 1
            pr -= 1
    
    return "".join(text_lst)


# Ejemplo 1:
s = "hola"
# # Salida: "halo"
result = invert_vowels(s)
print(result)


# Ejemplo 2:
# # Entrada:
s2 = "leetcode"
# # Salida: "leotcede"
result2 = invert_vowels(s2)
print(result2)

# Ejemplo 1:
s3 = "hello"
# # Salida: "holle"
result3 = invert_vowels(s3)
print(result3)