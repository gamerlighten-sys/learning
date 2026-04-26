"""7. Pop Until Empty

Task: Given a stack [1, 2, 3], keep popping elements until the stack becomes empty.
Description: Uses a loop to remove all elements.
Expected Output:"""

from stack import is_empty, pop, display

num_stack = [1, 2, 3]

while is_empty(num_stack) != True:
    element = pop(num_stack)
    print(f"popped: {element}")

display(num_stack)