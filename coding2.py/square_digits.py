"""
Q3. Square Numbers List
Create a list of numbers 1 to 10 using a loop.
Then make another list that contains the square of each number.
👉 Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
"""
num_list = []
square_list = []

for i in range(1, 11):
    num_list.append(i)

for i in range(1, 11):
    square_list.append(i**2)

print(num_list)
print(square_list)