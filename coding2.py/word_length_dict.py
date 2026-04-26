"""
Q4. Word Length Dictionary
Ask the user for a sentence.
Create a dictionary where each word is the key and its length is the value.
👉 Example:

Input: "python is fun"
Output: {'python': 6, 'is': 2, 'fun': 3}
"""

text = "python is fun"
list_of_words = text.split(" ")
word_to_length = {}

for word in list_of_words:
    word_to_length.update({word : len(word)})
print(word_to_length)