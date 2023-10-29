def multiples3or5(number):
    aList = []
    i = 0
    if number < 0:
        return 0

    while i < number:
        if i % 3 == 0:
            aList.append(i)
        elif i % 5 == 0:
            if i not in aList:
                aList.append(i)
        i += 1 
    sum = 0
    for i in aList:
        sum += i
    return sum


    
        

print(multiples3or5(5))


