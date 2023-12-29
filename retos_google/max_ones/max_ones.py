def max_ones(A: [int], K: int) -> int:
   comienzo = 0
   cuentaCeros = 0
   mayorLongitud = 0
   for final in range(len(A)):
       if A[final] == 0: cuentaCeros += 1
       while cuentaCeros > K:
           if A[comienzo] == 0: cuentaCeros -= 1
           comienzo += 1
       mayorLongitud = max(mayorLongitud, final - comienzo + 1)
   return mayorLongitud



# Entrada: 
nums = [1,1,1,0,0,0,1,1,1,0]
k = 2
# Salida: 5
result = max_ones(nums,k)
print(result)
# Explicación: [1,1,1,0,0,-1,1,1,1,1,1-]

# Ejemplo 2:

# Entrada:
nums2 = [0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1]
k2 = 3
result2 = max_ones(nums2,k2)
print(result2)
# Salida: 10
