"""
Q3. Even and Odd Splitter
Ask the user for a list of numbers.
Create two new lists: one with all even numbers, and one with all odd numbers.
Then print them separately.
👉 Example:

Input: [1, 2, 3, 4, 5, 6]
Output:
Even: [2, 4, 6]
Odd: [1, 3, 5]
"""

list_nums = [1, 2, 3, 4, 5, 6]
even_list = []
odd_list = []

for num in list_nums:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print(even_list)
print(odd_list)