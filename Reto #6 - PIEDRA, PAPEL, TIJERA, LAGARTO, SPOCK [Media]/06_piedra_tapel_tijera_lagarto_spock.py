score_p1 = 0
score_p2 = 0


def check_for_stone(p2: str):
    global score_p1
    global score_p2
    if(p2 == "tijeras"):
        score_p1 += 1
    elif(p2 == "papel"):
        score_p2 += 1

def check_for_scissors(p2: str):
    global score_p1
    global score_p2
    if(p2 == "papel"):
        score_p1 += 1
    elif(p2 == "piedra"):
        score_p2 += 1

def check_for_paper(p2: str):
    global score_p1
    global score_p2
    if(p2 == "piedra"):
        score_p1 += 1
    elif(p2 == "tijeras"):
        score_p2 += 1

def check_results(p1: str, p2: str):
    if p1 == "piedra":
        check_for_stone(p2)
    elif p1 == "tijeras":
        check_for_scissors(p2)
    elif p1 == "papel":
        check_for_paper(p2)

def check_victory():
    global score_p1
    global score_p2
    if score_p1 == score_p2:
        print("Tie, empate")
    elif score_p1 > score_p1:
        print("victoria jugador 1")
    else: print("victoria jugador 2")
    print(score_p1)
    print(score_p2)

def game(entrada : list):
    for i in entrada:
        check_results(i[0], i[1])
    check_victory()

game([("piedra","tijeras"), ("tijeras","piedra"), ("papel","tijeras")])