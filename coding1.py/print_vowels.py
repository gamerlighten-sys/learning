string = str(input("enter a string (a word or a sentence): "))
vowel_list = []
count = 0

for letter in string:
    if count == 5:
        break
    elif letter.lower() == 'a' or letter.lower() == 'e'  or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
        vowel_list.append(letter.lower())
        count += 1
    else:
        pass

print(vowel_list)