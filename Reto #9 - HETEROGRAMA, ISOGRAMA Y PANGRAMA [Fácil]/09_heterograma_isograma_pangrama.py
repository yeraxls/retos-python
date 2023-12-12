
#es una palabra o frase que no contiene ninguna letra repetida
def es_heterograma(text: str):
    print(f"comprobación de heterograma: {text}")
    letras = set(text)
    
    print(f"{text}{'' if len(letras) == len(text) else ' no' } es un heterograma")

#palabra o frase en la que cada letra aparece el mismo número de veces
def es_isograma(text: str):
    print(f"comprobación de isograma: {text}")

#es un texto que usa todas las letras posibles del alfabeto de un idioma.
def es_pangrama(text: str):
    print(f"comprobación de pangrama: {text}")


text_input = input("introduce un texto: ")

es_heterograma(text_input)

es_isograma(text_input)

es_pangrama(text_input)