"""
Q1 Count Uppercase and Lowercase Letters
Ask the user for a sentence and count how many uppercase and lowercase letters it has.
👉 Example:

Input: "Hello World"
Output:
Uppercase: 2  
Lowercase: 8
"""

text = "Hello World"
upper_case = 0
lower_case = 0

for char in text:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1
    else:
        continue

print(f"UPPER CASE: {upper_case}")
print(f"lower case: {lower_case}")