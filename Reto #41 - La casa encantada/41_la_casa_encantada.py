import random
render_choices  = {
    "room" : "⬜️",
    "door" : "🚪",
    "ghost" : "👻",
    "candy" : "🍭",
    "question" : "❓",
    "player" : "👱"
    }

def create_house():
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

create_house()