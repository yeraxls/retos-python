# Crea un generador de números pseudoaleatorios entre 0 y 100.
# - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 
#  Es más complicado de lo que parece...
from datetime import datetime

date = datetime.now().microsecond
res = [int(x) for x in str(date)]

num =f"{res[0]}{res[1]}"
num2 =f"{res[0]}{res[1]}{res[2]}"

print(f"numero aleatorio {num if int(num2) >= 100 else num2 }")





print("Solucion Moure")


import time


def random():
    return time.time_ns() % 101


for _ in range(0, 101):
    print(random())