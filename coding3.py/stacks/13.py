"""13. Check for Balanced Parentheses

Task: Check whether the expression (a+b)*(c+d) has balanced parentheses using a stack.
Description: Classic stack problem using push and pop.
Expected Output:"""

expression = "(a+b)*(c+d)"
stack = []

for i in range(len(expression)):
    char = expression[i]
    if char == "(":
        stack.append(char)
    elif char == ")":
        if stack[i-1] == "(":
            stack.pop()
        else:
            print("Not balanced")
            break

if len(stack) == 0:
    print("Balanced parentheses")
else:
    print("Not balanced")