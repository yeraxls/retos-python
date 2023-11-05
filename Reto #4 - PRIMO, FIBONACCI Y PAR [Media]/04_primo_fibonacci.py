#   Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#   Ejemplos:
#   - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#   - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
import math

result = ""
def es_primo(n):
    global result
    result = "es primo, "
    for i in range(2,n):
        if (n%i) == 0:
            result = "no es primo, "
            
def is_square(x):
	s = int(math.sqrt(x))
	return s*s == x

# Returns true if n is a Fibinacci Number, else false
def is_fibonacci(n):
    global result
    if is_square(5*n*n + 4) or is_square(5*n*n - 4) == True:
        result += "fibonacci, "
    else:
        result += "no es fibonacci, "
def is_par(n):
    global result
    if(n % 2 == 0):
        result += "y es par"
    else: result += "y es impar"


num = int(input("Enter a number: "))
es_primo(num)
is_fibonacci(num)
is_par(num)
print(num, result)