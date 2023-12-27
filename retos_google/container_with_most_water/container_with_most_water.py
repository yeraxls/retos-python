def max_area(alturas:[]):
    area_max = 0
    pointer = 0
    pointer_end = len(alturas) - 1

    while pointer < pointer_end:
        area = min(alturas[pointer], alturas[pointer_end]) * (pointer_end - pointer)
        if area > area_max:
            area_max = area
        if alturas[pointer] >= alturas[pointer_end]:
            pointer_end -= 1
        else:
            pointer += 1

    return area_max


# Ejemplo 1:
alturas = [1,8,6,2,5,4,8,3,7]
result1 = max_area(alturas)
print(result1)
# 49

# Ejemplo 2:
alturas2 = [8,1,6,2,5,4,1,3,7]
result2 = max_area(alturas2)
print(result2)
# 56