even_list = []

odd_list = []

while True:
    num = input("Please enter an integer value or 'DONE' (when finished):")
    
    if num == 'DONE':
        break

    elif type(num) is int == False:
        continue
    
    intnum = int(num)
    
    if intnum % 2 == 0:
        even_list.append(intnum)
        
    else:
        odd_list.append(intnum)
        
print("Even numbers entered:", even_list)

print("Odd numbers entered:", odd_list)
        
        
