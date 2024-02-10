num = int(input("Please enter a number: "))

if num == 1:
    print(1)
elif num == 0:
    print(1)
elif num == 2:
    print(2)
else:
    i = 1
    result = 1
    for x in range(1, (num+1)):
        result = result*i
        i += 1
    print(result)
