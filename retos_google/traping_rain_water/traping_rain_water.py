def rainWaterV1(arr):
    maxLeft = [0]*len(arr)
    maxRight = [0]*len(arr)
    total = 0
    # get max value at left of i
    maxVal = -1
    for i in range(1, len(arr)):
        maxVal = max(arr[i-1], maxVal)
        maxLeft[i] = maxVal
    maxVal = -1
    # get max value at right of i
    for i in range(len(arr)-2, -1, -1):
        maxVal = max(arr[i+1], maxVal)
        maxRight[i] = maxVal
    # get sum of areas
    for i in range(len(arr)):
        area = min(maxLeft[i], maxRight[i])-arr[i]
        if area > -1:
            total += area
    return total

alturas = [0, 1, 0, 2, 1,0,1,3,2,1,2,1]
# 6
result = rainWaterV1(alturas)
print(result)