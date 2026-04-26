def enqueue(queue, element):
    queue.append(element)
    return queue

def dequeue(queue):
    if not is_empty(queue):
        removed_element = queue.pop(0)
        print(removed_element, "left the queue")
    else:
        print("Queue is empty")
    return queue

def peek(queue):
    if not is_empty(queue):
        return queue[0]
    else:
        print("Queue is empty")
        return None
    
def display(queue):
    print("Total elements in queue:", size(queue))
    print(*queue, sep=", ")


def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
    
def size(queue):
    return len(queue)

if __name__ == '__main__':
    queue = []
    while True:
        action = input("Enter your action (1: add, 2: delete, 3: peek, 0: stop): ")
        if action == "1":
            element = input("enter the element to be added: ")
            enqueue(queue, element)
        elif action == "2":
            dequeue(queue)
        elif action == "3":
            print(peek(queue))
        else:
            break
    display(queue)