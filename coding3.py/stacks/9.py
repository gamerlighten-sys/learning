"""9. Push Only Even Numbers

Task: From the list [1, 2, 3, 4, 5, 6], push only even numbers into a stack.
Description: Combines condition checking with stack operations.
Expected Output:"""

from stack import push, display

num_stack = [1, 2, 3, 4, 5, 6]
new_stack = []

for i in range(len(num_stack)):
    if num_stack[i] % 2 == 0:
        push(new_stack, num_stack[i])
    else:
        pass

display(new_stack)