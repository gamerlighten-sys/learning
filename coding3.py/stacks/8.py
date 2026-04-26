"""8. Reverse a Stack

Task: Reverse a stack [10, 20, 30, 40] using another stack.
Description: Tests understanding of LIFO behavior.
Expected Output:"""

from stack import pop, push, is_empty

num_stack =  [10, 20, 30, 40]
temp_stack = []

while is_empty(num_stack) != True: 
    element = pop(num_stack)
    push(temp_stack, element)

print(f"reversed stack: {temp_stack}")