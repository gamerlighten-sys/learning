"""
1. Reverse a List Without Using reverse() or Slicing
Input: [1, 2, 3, 4]
Output: [4, 3, 2, 1]
"""

num_list = [1, 2, 3, 4]
for i in range(len(num_list)):
    print(num_list[-1])
    new_list = num_list.insert(i, num_list[-1])
    print(num_list[i])
    new_list = num_list.remove(num_list[-1])