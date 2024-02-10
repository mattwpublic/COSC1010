team_dict = {}

while True:
    
    user_operation = input("What operation would you like to do: quit, add, remove, count, or display: ")


    if user_operation == 'quit' or user_operation == 'add' or user_operation == 'remove' or user_operation == 'count' or user_operation == 'display':
        if user_operation == 'add':
            user_team = input("Please enter a team name:")
            if user_team in team_dict:
                user_team_yearwon = input("What additional year did the " + user_team + " win the NBA championship:")
                team_dict[user_team] = user_team_yearwon
                print(user_team, "was added to the dictionary")
            else:
                user_team_yearwon = input("what year did the " + user_team + " win the NBA championship:")
                team_dict[user_team] = user_team_yearwon
                print(user_team, "was added to the dictionary")
        elif user_operation == 'remove':
            user_team = input("Please enter a team name:")
            if user_team in team_dict:
                team_dict.pop(user_team)
                print(user_team, "was removed from the dictionary")
            else:
                print("This team is not valid, please try again")
        elif user_operation == 'display':
            print(team_dict)
        elif user_operation == 'count':
            count = 0
            for x in team_dict:
                count += 1
            print(count, "teams have won the NBA championship")
        elif user_operation == 'quit':
            break
    else:
        print("This is not a valid option, please try again")
