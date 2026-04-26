# Create a queue [1,2,3,4]. Remove elements one by one and print them

from queue import dequeue, peek

queue = [1,2,3,4]
for element in queue:
    peek(queue)
    dequeue(queue)