"""
Write a program that counts down from 10 to 1
using a while loop and prints "Happy New Year!" at the end.
"""

import time


timer = 10

while (timer > 0):
    print(timer)
    time.sleep(1)
    timer -= 1

print("Happy New Year!")