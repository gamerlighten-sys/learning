"""
Q2. Highest Value Finder
You’re given a dictionary of names and scores.
Find who got the highest score.
👉 Example:

scores = {'Alice': 82, 'Bob': 91, 'Charlie': 87}
Output: Bob got the highest score: 91
"""

scores = {'Alice': 82, 'Bob': 91, 'Charlie': 87}
highest_value = max(scores.values())
for person in scores:
    if scores[person] == highest_value:
        print(f"{person} got the highest score: {highest_value}")
        exit(0)
    else:
        continue