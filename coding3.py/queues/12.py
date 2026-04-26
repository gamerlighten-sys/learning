"""
Create a Queue class with methods:

enqueue()

dequeue()

display()

Add 10,20,30 and remove one element.
"""

from queue import enqueue, dequeue, display

queue = []
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)
dequeue(queue)
display(queue)