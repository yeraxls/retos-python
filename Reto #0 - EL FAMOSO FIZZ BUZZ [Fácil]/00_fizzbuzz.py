def check_num(num):
    if num % 3== 0 and num % 5== 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

for i in range (101): 
    print(check_num(i))
    i+=1
