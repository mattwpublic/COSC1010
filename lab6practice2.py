myList = []
for x in range(10):
    num = int(input("Please enter a number: "))
    myList.append(num)

for x in myList:
    if myList[x] % 2 == 0:
        print(myList[x])
    
    
