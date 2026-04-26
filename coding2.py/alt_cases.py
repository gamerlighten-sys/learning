"""
Q3. Alternate Case
Ask the user for a word.
Print a new version where the letters go uppercase, lowercase, uppercase, lowercase… and so on.
👉 Example:

Input: python
Output: PyThOn
"""

text = "python"
alternate_case = ""

for i in range(len(text)):
    if i % 2 == 0:
        alternate_case += text[i].upper()
    else:
        alternate_case += text[i].lower()

print(alternate_case)