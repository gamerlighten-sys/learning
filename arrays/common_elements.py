"""
Q1. Common Elements Finder
Ask the user for two lists. Print all 
the elements that appear in both lists.
👉 Example:

Input: [1, 2, 3, 4] and [3, 4, 5, 6]
Output: [3, 4]
"""

list1 = []
list1_count = int(input("Enter how many nums you want in list1: "))
for i in range(list1_count):
    num1 = int(input("Enter num for list: "))
    list1.append(num1)

list2 = []
list2_count = int(input("Enter how many nums you want in list1: "))
for i in range(list2_count):
    num2 = int(input("Enter num for list: "))
    list2.append(num2)

# list3 = list1 + list2
# for num in list3:
#     if num in final_list:
#         continue
#     elif list3.count(num) > 1:
#         final_list.append(num)

set1 = set(list1)
set2 = set(list2)
common = set1 & set2
# common = set1.intersection(set2)

print(common)