"""14. Reverse a String Using Stack

Task: Reverse the string "STACK" using a stack.
Description: Tests real-world stack usage.
Expected Output:"""

string = "STACK"
stack = []
reversed_string = ""

for char in string:
    stack.append(char)

while stack:
    reversed_string += stack.pop()

print(reversed_string)