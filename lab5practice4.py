inputNum = input("Please enter a 5-digit number: ")
minNum = 0
maxNum = 0

i = 1

for x in inputNum:
    if i == 1:
        minNum = x
    elif i == 5:
        maxNum = x
    i += 1
print(minNum, maxNum)
