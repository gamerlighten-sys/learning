"""
Q4. Remove Adjacent Duplicates

Given a list, remove only adjacent duplicates (not all duplicates).
👉 Example:
Input: [1, 1, 2, 3, 3, 3, 2]
Output: [1, 2, 3, 2]
"""

list_nums = [1, 1, 2, 3, 3, 3, 2]
new_list = []

for i in range(len(list_nums)):
    if i == 0:
        new_list.append(list_nums[i])
    elif list_nums[i] != list_nums[i - 1]:
        new_list.append(list_nums[i])

print(new_list)