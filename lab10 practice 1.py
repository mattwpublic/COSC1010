string = input("Enter string:")

string_dict = {}

for char in string:
    if char in string_dict:
        string_dict[char] += 1
        continue
    string_dict[char] = 1

print(string_dict)
