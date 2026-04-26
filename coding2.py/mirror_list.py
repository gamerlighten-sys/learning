"""
Q2. Mirror List
Make a list of numbers and then make it “mirror” itself.
👉 Example:

Input: [1, 2, 3]
Output: [1, 2, 3, 3, 2, 1]
"""

list_nums = [1, 2, 3]
final_list = list_nums+list_nums[::-1]
print(final_list)