"""12. Implement Stack Menu Program

Task: Create a menu-driven program with options:

Push

Pop

Peek

Display

Exit
Description: Full stack implementation using user input.
Expected Output (sample):"""

from stack import push, pop, peek, display

stack = []

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        element = input("Enter an element: ")
        push(stack, element)

    elif choice == 2:
        pop(stack)

    elif choice == 3:
        print(peek(stack))

    elif choice == 4:
        display(stack)
        
    elif choice == 5:
        break

    else:
        print("Invalid choice")