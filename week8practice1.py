#def nameaddress(name, address):
    #print(name, address)

#username = input("Please enter your name: ")
#useraddress = input("Please enter your address: ")

#nameaddress(username, useraddress)


#def nameread(first, last):
    #fullname = first, last
    #return fullname

#firstname = input("Please enter your first name: ")
#lastname = input("Please enter your last name: ")

#print(nameread(firstname, lastname))

def returnstars(num):
    if num == '1':
        return '*'
    elif num == '2':
        return '**'
    elif num == '3':
        return '***'

usernum = input("Please enter a number: ")

print(returnstars(usernum))
