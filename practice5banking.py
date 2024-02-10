#Banker Program
#Matthew Wideman
#10/13/22
account_names = []
account_balances = []
def accounts_sort(name_array, balance_array):
    sorted_balances = []
    sorted_names = []
    while True:
        max_value = 0
        for _, n in enumerate(balance_array): #pylint: disable=C0103
            if n > max_value:
                max_value = n
        sorted_names.append(name_array[balance_array.index(max_value)])
        sorted_balances.append(max_value)
        name_array.pop(balance_array.index(max_value))
        balance_array.pop(balance_array.index(max_value))
        if balance_array == []:
            break
    print(sorted_names)
    print(sorted_balances)
while True:
    accName = input("Name of account: ")
    if accName == 'done':
        for x, i in enumerate(account_balances):
            if i >= 200:
                account_balances[x] += 50
            elif i <= 25:
                account_names.remove(account_names[x])
                account_balances.remove(i)
        if account_names == []:
            print("No accounts!")
            break
        accounts_sort(account_names, account_balances)
        break
    accBal = int(input("Balance of account: "))
    if accBal <= 0:
        print("Invalid balance!")
    elif accName in account_names:
        account_balances[account_names.index(accName)] += accBal
    else:
        account_names.append(accName)
        account_balances.append(accBal)
