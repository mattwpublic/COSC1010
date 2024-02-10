example_list = [1,2,3,4,5,6,2,3,7,8,2,5,6,7,2,1,1,1,2,4,5,6,7]

print("The last value of the list is:", example_list[len(example_list)-1])

print("The first three valuess of the list are:")
      
for x in range(3):
      print(example_list[x])

print("The last 3 values of the list are:")

for x in range(1, 4):
      print(example_list[len(example_list) - x])
