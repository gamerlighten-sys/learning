# input shape then input length, height, radius, side lengths, base size respectively
# calculate area and perimeter based on what shape is entered using different formulas
# print area and perimeter of whichever shape user wanted

welcome_msg = """

welcome to area and perimeter calculator!😊

1. square
2. rectangle
3. parallelogram
4. triangle
5. circle
"""

print(welcome_msg)

shape = input("enter what shape you want: ")
area = 0
perimeter = 0
pi = 3.14159

if shape == "square":
    length = int(input("what is the side length: "))
    print()
    area = length * length
    perimeter = length * 4
    

elif shape == "rectangle" or shape == "parallelogram":
    length = int(input("what is the length: "))
    height = int(input("what is the height: "))
    print()
    area = length * height
    perimeter = (length * 2) + (height * 2)
   

elif shape == "triangle":
    height = int(input("what is the height: "))
    base = int(input("what is the length base: "))
    side1 = int(input("what is the length of the first side: "))
    side2 = int(input("what is the length of the second side: "))
    print()
    area = base * height / 2
    perimeter = base + side1 + side2
   

elif shape == "circle":
    radius = int(input("what is the radius: "))
    print()
    area = 3.14159 * (radius * radius)
    perimeter = 2 * 3.14159 * radius


else:
    print("invalid input, please try fixing your spelling")


print("area of", shape, "is", area)
print("perimeter of", shape, "is", perimeter)
   