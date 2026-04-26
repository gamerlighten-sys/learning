# Create a queue using a list. Add the numbers 10, 20, 30 and print the queue.

from queue import enque, display

queue = []
enque(queue, 10)
enque(queue, 20)
enque(queue, 30)
display(queue)