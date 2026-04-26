"""
Q4. Flatten Nested Tuple
You have a nested tuple:
nested = ((1, 2), (3, 4), (5, 6))

Write a program to turn it into:
(1, 2, 3, 4, 5, 6)
"""

nested = ((1, 2), (3, 4), (5, 6))
flattened_tuple = ()
for item in nested:
    flattened_tuple += item
print(flattened_tuple)