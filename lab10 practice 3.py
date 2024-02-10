sentence_dict = {}
user_string = input("Input:")

words = user_string.split()

for word in words:
    firstletter = word[0]
    if str(firstletter) in sentence_dict:
        if word not in sentence_dict[firstletter]:
            sentence_dict.append(word)
    else:
        sentence_dict[firstletter] = word
print(sentence_dict)
