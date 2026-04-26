# Ask the user to enter 3 numbers and add them to a queue.

from queue import enqueue

queue = []

for i in range(3):
    num = int(input("Enter number: "))
    enqueue(num)

print("Queue:", queue)