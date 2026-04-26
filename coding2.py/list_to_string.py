"""
Q2. List to String
Take a list of words and join them into one string separated by spaces.
👉 Example:

Input: ["Python", "is", "cool"]
Output: "Python is cool"
"""

list_of_words = ["Python", "is", "cool"]
string = ""
for word in list_of_words:
    string += word
    string += " "
print(string)