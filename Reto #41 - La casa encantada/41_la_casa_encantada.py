import random
render_choices  = {
    "room" : "⬜️",
    "door" : "🚪",
    "ghost" : "👻",
    "candy" : "🍭",
    "question" : "❓",
    "player" : "👱"
    }

def create_house() ->  (list, list):
    house = [list([render_choices["room"]]) *4 for _ in range(4)]

    door = list()
    if random.choice([True,False]):
        #columnas perimetro
        door = [random.randint(0, 3), random.choice([0, 3])]
    else:
        #filas perimetro
       door = [random.choice([0, 3]), random.randint(0, 3)]
    house[door[0]][door[1]]= render_choices["door"]

    def generate_candy(door: list) -> list:
        candy =[random.randint(0, 3), random.randint(0, 3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy
    
    candy = generate_candy(door)

    house[candy[0]][candy[1]] = render_choices["candy"]

    for row in house:
        print("".join(map(str, row)))
    return house, door
def move(position: list) -> list:

    row, col = position[0], position[1]

    movements = "N S E O "

    if row == 0: movements = movements.replace("N ", "")
    if row == 3: movements = movements.replace("S ", "")
    if col == 0: movements = movements.replace("O ", "")
    if col == 3: movements = movements.replace("E ", "")

    movement = input(f"¿Hacia dónde te quieres desplazar [ {movements}]?: ").upper()

    if movement in movements:
        if movement == "N": position = [row - 1, col]
        elif movement == "S": position = [row + 1, col]
        elif movement == "E": position = [row, col + 1]
        elif movement == "O": position = [row, col - 1]

        return position
    else:
        print("Desplazamiento incorrecto. Selecciona una de las opciones válidas.")
        return move(position)

def riddle():

    riddles = [
        ("¿Qué lenguaje de programación fue creado por Guido van Rossum?", "Python"),
        ("¿Cuál es el sistema operativo de código abierto más popular?", "Linux"),
        ("¿Qué compañía desarrolló el sistema operativo Windows?", "Microsoft"),
        ("¿Qué lenguaje de programación se utiliza principalmente para el desarrollo web del lado del cliente?", "JavaScript"),
        ("¿Cuál es el protocolo estándar para enviar correos electrónicos?", "SMTP"),
        ("¿Qué significa HTML?", "HyperText Markup Language"),
        ("¿Cuál es la base de datos relacional de código abierto más popular?", "MySQL"),
        ("¿Qué significa URL?", "Uniform Resource Locator"),
        ("¿Qué compañía desarrolló el lenguaje de programación Java?", "Sun"),
        ("¿Qué estructura de datos es LIFO?", "Pila"),
        ("¿Qué lenguaje de programación fue diseñado por Bjarne Stroustrup?", "C++"),
        ("¿Qué significa HTTP?", "HyperText Transfer Protocol"),
        ("¿Qué significa SQL?", "Structured Query Language"),
        ("¿Cuál es el lenguaje de hojas de estilo utilizado en la web?", "CSS"),
        ("¿Qué significa API?", "Application Programming Interface"),
        ("¿Qué estructura de datos es FIFO?", "Cola"),
        ("¿Cuál es el lenguaje de programación más antiguo aún en uso?", "Fortran"),
        ("¿Qué significa IDE?", "Integrated Development Environment"),
        ("¿Qué compañía es la creadora del sistema operativo macOS?", "Apple"),
        ("¿Qué lenguaje se utiliza comúnmente para el desarrollo de aplicaciones Android?", "Kotlin")
    ]

    current_riddle = riddles[random.randint(0, len(riddles) - 1)]

    while True:
        answer = input(f"{current_riddle[0]}: ")

        if answer.lower() == current_riddle[1].lower():
            print("Respuesta correcta!\n")
            return
        else:
            print("Respuesta incorrecta!\n")
house, door = create_house()

position = door
print(f"Posición inicial: {position}")

print(f"""
{render_choices['ghost']} BoooOOOoOoo!
Si quieres encontrar los dulces 🍭 de la casa encantada 🏰
tendrás que buscarlos a través de sus habitaciones.
Pero recuerda, no podrás moverte si antes no respondes
correctamente a su enigma.
""")
while True:
    for row in house:
        print("".join(map(str, row)))
    oldposition = position
    position = move(position)
    print(f"Posición: {position}\n")

    house_room = house[position[0]][position[1]]

    if house_room == "⬜️":

        print("Responde correctamente a esta pregunta.")
        riddle()

        ghost = random.randint(1, 10) == 1
        if ghost:
            print(f"{render_choices['ghost']} BoooOOOoOoo! Para salir de esta habitación deberás responder otra pregunta más.")
            riddle()
        house[position[0]][position[1]] = render_choices["player"]
        if not(house[oldposition[0]][oldposition[1]] == render_choices["door"]):
            house[oldposition[0]][oldposition[1]] = render_choices["room"]

    elif house_room == {render_choices['candy']}:
        print(f"""
{render_choices['ghost']} BoooOOOoOoo!
Has encontrado los dulces {render_choices['candy']} y escapado de la casa encantada 🏰
Feliz Halloween! 🎃
    """)
        break