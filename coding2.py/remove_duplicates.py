"""
Q1. Remove Duplicates from a List
Ask the user for a list of numbers (use split() for input).
Print a new list that has all the numbers but no duplicates — keep the original order.
👉 Example:

Input: [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4]
"""

list_nums = [1, 2, 2, 3, 1, 4]
unique_nums = []

for num in list_nums:
    if num not in unique_nums:
        unique_nums.append(num)
print(unique_nums)