"""
6. Sum of Digits of a Number Until It Becomes 1 Digit
Input: 9875
Step 1 → 9+8+7+5 = 29
Step 2 → 2+9 = 11
Step 3 → 1+1 = 2
Output: 2
"""

number = 9875
fake_number = str(number)
sum = 0
while sum < 10:
    for i in range(len(fake_number)):
        sum += int(fake_number[i])
print(sum)