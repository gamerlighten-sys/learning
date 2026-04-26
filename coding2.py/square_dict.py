"""
Q5. Square Dictionary
Ask the user for a number n.
Make a dictionary with numbers 1 to n as keys and their squares as values.
👉 Example:

Input: 5
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

n = 5
square_values = {}
for i in range(1, n + 1):
    square_values.update({i : i**2})
print(square_values)