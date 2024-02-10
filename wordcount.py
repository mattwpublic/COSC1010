def clean_word(word):
    cleanword = ''
    for char in word:
        temp = char.lower()
        if char.isalpha():
            cleanword += temp
    return cleanword

def main():
    file_handler = open('textfile.txt')
    search_terms = []
    search_term_occurrances = []
    user_search_terms = input("What words do you want to count? ")
    search_terms_split = user_search_terms.split(',')
    for word in search_terms_split:
        if clean_word(word) == '':
            continue
        search_terms.append(clean_word(word))
    if len(search_terms) == 0:
        print("No words entered")
    for x in search_terms:
        search_term_occurrances.append(0)
        
    for line in file_handler:
        for word in line.split():
            for x in search_terms:
                if x == clean_word(word):
                    search_term_occurrances[search_terms.index(x)] += 1
                
    for x in search_terms:
        print("The count of", search_terms[search_terms.index(x)], "is", search_term_occurrances[search_terms.index(x)])
        
main()
