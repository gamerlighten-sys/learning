sentence = str(input("enter a sentence: "))
word_count = 1

for letter in sentence:
    if letter == " ":
        word_count += 1
print(f"there is {word_count} words in that sentence ")