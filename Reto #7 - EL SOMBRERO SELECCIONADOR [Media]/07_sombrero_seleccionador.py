# Crea un programa que simule el comportamiento del sombrero seleccionador del
#   universo mágico de Harry Potter.
#   - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#   - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#   - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#     coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
#   - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#     Por ejemplo, en Slytherin se premia la ambición y la astucia.

#Gryffindor valiente, temple, caballerosidad, imprudente
#Slytherin Ambicioso, astutos, líderes fuertes, piensan antes de actuar
#Ravenclaw Ingenioso, valora el aprendizaje, sabiduría intelecto
#Hufflepuff Leal e inteligente, trabajadores, amigables

casas = {
    0 : "Gryffindor",
    1 : "Slytherin",
    2 : "Ravenclaw",
    3 : "Hufflepuff",
}
puntos =[0,0,0,0]
def select_choice():
    global puntos
    num = input("introduce el número: ")
    if num.isnumeric():
        puntos[int(num)-1] += 1
    else:
        select_choice()
def final_choice(puntos : list):
    num = max(puntos, key=int)
    print("Te espera fama en tu nueva casa")
    print(f"Bienvenido a la casa {casas[puntos.index(num)]}")


print("Bienvenidos a Hogwarts \nResponde al sombre seleccionador")

print("te consideras mas...")
print("\t1-valiente") #-griffindor
print("\t2-astuto") #- slytherin
print("\t3-ingenioso") #- ravenclaw
print("\t4-leal") #- hufflepuff
select_choice()

print("mi comportamiento hacia los demás es:")
print("\t1-caballeroso") #-griffindor
print("\t2-quiero liderar") #- slytherin
print("\t3-foco de sabiduria") #- ravenclaw
print("\t4-amigable") #- hufflepuff
select_choice()

print("En una situación de peligro:")
print("\t1-actúo sin pensar") #-griffindor
print("\t2-pienso antes de actuar") #- slytherin
print("\t3-Intento algo ingenioso") #- ravenclaw
print("\t4-trabajo duro para solventarlo") #- hufflepuff
select_choice()


final_choice(puntos)
