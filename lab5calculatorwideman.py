#Matthew Wideman
#9/29/22
#Calculator

running = True

while running == True:
    
    x = input("What is the first number: ")
    y = input("What is the second number: ")

    op = input("What operation: ")

    if x == 'DONE' or y == 'DONE' or op== 'DONE':
        break
        
    if y == '0' and op == '/':
        print('Divide by zero error')
        continue
    
    else:
    
        result = 0

        num1 = int(x)
        num2 = int(y)

        if op == '+':
            result = num1 + num2
            print(x, '+', y, '=' , result) 
        elif op == '-':
            result = num1 - num2
            print(x, '-', y, '=', result) 
        elif op == '/':
            result = int(num1 / num2)
            rem = num1%num2
            print(x, '/', y, '=', result, 'with a remainder of', rem) 
        elif op == '*':
            result = num1 * num2
            print(x, '*', y, '=', result)
        else:
            print("Invalid operand")
