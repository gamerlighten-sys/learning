"""11. Copy One Stack to Another

Task: Copy all elements from stack1 [1, 2, 3] to stack2.
Description: Uses stack operations to duplicate contents.
Expected Output:"""

from stack import push, display

stack1 = [1, 2, 3]
stack2 = []

for i in range(len(stack1)):
    element = stack1[i]
    push(stack2, element)

display(stack2)