#Matthew Wideman
#In Lab Assignment
#11/10/22

while True:

    user_number1 = int(input("What is the first number: "))
    user_number2 = int(input("What is the second number: "))
    user_op = input("What operation: ")

    if user_op == '+':
        user_result = user_number1 + user_number2
    elif user_op == '-':
        user_result = user_number1 - user_number2
    elif user_op == '/':
        user_result = user_number1 / user_number2
    elif user_op == '*':
        user_result = user_number1 * user_number2
    elif user_op == 'DONE':
        break
    else:
        print("Invalid operand")
        continue
    print(user_number1, user_op, user_number2, '=', user_op
