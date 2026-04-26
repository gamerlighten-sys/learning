"""
3. Pop an Element

Task: Given a stack [1, 2, 3, 4], pop one element and print the stack.
Description: Tests removing the top element using pop().
Expected Output:
"""

from stack import display

num_stack = [1, 2, 3, 4]
num_stack.pop()
display(num_stack)