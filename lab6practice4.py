done = False

myList = []

while done == False:
    num = input("Please enter an integer value or 'DONE' if you are finished:")
    if num == 'DONE':
        break
    numint = int(num)
    myList.append(numint)

lisAvg = sum(myList)/len(myList)

print("The average of all values in the list is:", lisAvg)
