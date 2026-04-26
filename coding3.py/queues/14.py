# Customers "A", "B", "C", "D" are waiting in a queue. Serve customers one by one.

from queue import dequeue, size

queue = ["A", "B", "C", "D"]

while size(queue) > 0:
    customer = dequeue(queue)
    print("Serving", customer)
