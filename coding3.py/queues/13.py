# Create a queue with numbers 1–5, then remove the first two.

from queue import dequeue, display

queue = [1,2,3,4,5]
dequeue(queue)
dequeue(queue)
display(queue)