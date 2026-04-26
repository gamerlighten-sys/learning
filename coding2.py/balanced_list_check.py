"""
Q4. Balanced List Check
Ask the user for a list of numbers.
Print "Balanced" if the sum of the first half equals the sum of the second half.
👉 Example:

Input: [1, 2, 3, 3, 2, 1]
Output: Balanced
"""

list_nums = [1, 2, 3, 3, 2, 1]
middle = (len(list_nums)) // 2

first_half = 0
second_half = 0

for i in range(middle):
    first_half += list_nums[i] 

for i in range(middle, len(list_nums)):
    second_half += list_nums[i] 

if first_half == second_half:
    print("Balanced")
else:
    print("Unbalanced")