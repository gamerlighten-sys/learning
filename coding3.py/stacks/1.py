"""1. Create and Display a Stack

Task: Create an empty stack using a list. Push the values 10, 20, 30 and print the stack.
Description: Practice basic stack creation and push using append().
Expected Output:"""

from stack import push, display

num_stack = []
push(num_stack, 10)
push(num_stack, 20)
push(num_stack, 30)
display(num_stack)