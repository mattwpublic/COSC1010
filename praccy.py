array = ['c','a','f','b','d']

for pivot in range(1, len(array)):
    hole = pivot - 1
    while (hole >= 0) and  array[hole+1] < array[hole]:
        print("swapping... [" + str(hole) + "] " + str(array[hole]) + " and [" + str(hole+1) + "] " + str(array[hole]))
    
        swap = array[hole]
        array[hole] = array[hole+1]
        array[hole+1] = swap

        hole -= 1

print(array)
