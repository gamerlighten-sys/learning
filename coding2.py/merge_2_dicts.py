"""
Q5. Merge Two Dictionaries

You have two dictionaries.
Create a new one that combines them.
👉 Example:
a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
Output: {'x': 1, 'y': 3, 'z': 4}
"""

a = {
    'x': 1, 
    'y': 2
    }

b = {
    'y': 3,
    'z': 4
    }

a.update(b)
print(a)