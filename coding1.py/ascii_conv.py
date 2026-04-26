print("welcome to ascii value converter,")
print("a website which you probably wont ever use!")
print()
print("Convert ascii value to character or character to ascii value")
print()
print("1. ascii value to character")
print("2. character to ascii value")
question = input("enter either 1 or 2: ")


if question == "1":
    print()
    ascii_value = int(input("enter ascii value: "))
    character = chr(ascii_value)
    print(character)
    print()

elif question == "2":
    print()
    character = input("enter character: ")
    ascii_value = ord(character)
    print(ascii_value)
    print()






# character = chr(ascii_value)
# print(character)