SCORES = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40"
}
points = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
score_p1 = 0
score_p2 = 0

for point in points:
    if point == "P1":
        score_p1 += 1
    elif point == "P2":
        score_p2 += 1
    else:
        print("Player didnt found")
    if score_p1 == score_p2 and score_p1 != 0:
        print("Deuce")
    elif score_p1 >= 4 and score_p1 == score_p2 + 1:
        print("Ventaja P1")
    elif score_p2 >= 4 and score_p2 == score_p1 + 1:
        print("Ventaja P2")
    elif score_p1 >= 4 and score_p1 >= score_p2:
        print("Gana P1")
    elif score_p2 >= 4 and score_p2 >= score_p1:
        print("Gana P2")
    else:
        print(SCORES.get(score_p1), " : ", SCORES.get(score_p2))
