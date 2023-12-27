# Dada la lista de enteros nums, mueve todos los ceros al final de la misma, 
# manteniendo el orden relativo de los elementos no nulos.

# Reto: reordena los valores “in place”, sin hacer una copia de la lista.

#Ejemplo 2
# Entrada:
nums = [0,1,0,3,12]
# Salida: [1,3,12,0,0]

#Ejemplo 2
# Entrada:
nums2 = [0]
# Salida: [0]

def move_ceros(numbers):
    l = 0
    for r in range(len(numbers)):
        if numbers[r]:
            numbers[l], numbers[r] = numbers[r], numbers[l]
            l += 1
    return numbers

result = move_ceros(nums)
print(result)



