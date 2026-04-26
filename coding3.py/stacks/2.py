"""
2. Push an Element

Task: Given a stack [5, 15, 25], push 35 into it and print the stack.
Description: Tests adding one element to the top of the stack.
Expected Output:
"""

from stack import push, display

num_stack = [5, 15, 25]
push(num_stack, 35)
display(num_stack)