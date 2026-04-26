"""
4. Peek the Stack

Task: Given a stack [100, 200, 300], print the top element without removing it.
Description: Practice accessing the last element.
Expected Output:
"""

import stack

num_stack = []
while True:
   inp = int(input("Enter a number (0 to stop): "))
   if inp == 0:
      break
   stack.push(num_stack, inp)

print("The top element is:", stack.top(num_stack))