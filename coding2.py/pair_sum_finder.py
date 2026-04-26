"""
Q3. Pair Sum Finder
Given a list of numbers and a target number, find all pairs that add up to the target.
👉 Example:

Input: [1, 2, 3, 4, 5, 6], target = 7  
Output: (1,6), (2,5), (3,4)
"""

list_of_nums = [1, 2, 3, 4, 5, 6]
target = 7
pairs = []

for num in list_of_nums:
    match = 7 - num
    pair = [num, match]
    if [match, num] in pairs:
        continue
    if match in list_of_nums:
        pairs.append(pair)
print(pairs)