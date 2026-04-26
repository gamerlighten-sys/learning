"""
Q1. Character Counter
Ask the user for a word.
Count how many times each letter appears using a dictionary.
👉 Example:

Input: "banana"
Output: {'b': 1, 'a': 3, 'n': 2}
"""

word = "banana"
char_count = {}

for char in word:
    if char in char_count:
        continue
    char_count.update({char : word.count(char)})
print(char_count)