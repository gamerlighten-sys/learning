"""
Q1. Find Longest Word
Ask the user for a sentence and find the longest word in it.
If two words are tied, print both.
👉 Example:

Input: "coding is awesome and fun"
Output: awesome
"""

text = "coding is awesome and fun"
list_words = text.split()
longest_count = 0
longest_word = ""

for word in list_words:
    if len(word) > longest_count:
        longest_word = word
        longest_count = len(word)

print(longest_word)