def is_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
   
def push(stack, item):
    stack.append(item)
    return stack


def pop(stack):
    if is_empty(stack):
        print("stack is empty")
    else:
        return stack.pop()


def size(stack):
    return len(stack)


def top(stack):
    if is_empty(stack):
        print("stack is empty")
        return None
    else:
        position = size(stack) - 1
        return stack[position]


def display(stack):
    print("current stack: ")
    print(*stack, sep=", ")


def clear_stack(stack):
    while True:
        pop(stack)
        if is_empty(stack):
            break
    return stack
       
def peek(stack):
    if not is_empty(stack):
        return stack[0]
    else:
        print("Stack is empty")
        return None
   


if __name__ == "__main__":
    book_stack = []
    push(book_stack, "harry potter")
    push(book_stack, "percy jackson")
    display(book_stack)
    print(f"Their are {size(book_stack)} books in this stack")
    pop(book_stack)
    push(book_stack, "artemis fowl")
    print(f"the book at the top of the stack is {top(book_stack)}")
    display(book_stack)
    clear_stack(book_stack)
    display(book_stack)
