"""During admission in a course, the names of the students
are inserted in ascending order. Thus, performing the
sorting operation at the time of inserting elements in
a list. Identify the type of sorting technique being used
and write a program using a user defined function that
is invoked every time a name is input and stores the
name in ascending order of names in the list."""

arr = []
length = int(input("how many names are you inputting: "))
name = input("Enter name: ")
arr.append(name.lower())

for i in range(1, length):
    name = input("Enter name: ")
    arr.append(name.lower())
    j = i - 1
    key = arr[i]

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
print(arr)