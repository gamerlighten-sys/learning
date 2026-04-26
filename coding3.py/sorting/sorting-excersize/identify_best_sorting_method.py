"""Identify the number of swaps required for sorting the
following list using selection sort and bubble sort and
identify which is the better sorting technique with
respect to the number of comparisons."""

arr = [63, 42, 21, 9]


# selection sort
swaps, comparisons = 0, 0

for i in range(len(arr)):
    smallest = arr[i]
    smallest_index = i

    for j in range(i+1, len(arr)):

        element = arr[j]
        comparisons += 1
        if element < smallest:
            smallest = element
            smallest_index = j

    swaps += 1
    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

print("Sorted array:")
print(arr)
print(f"Swaps: {swaps}, Comparisons: {comparisons}\n")


# bubble sort
swaps, comparisons = 0, 0

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        comparisons += 1
        if arr[j+1] < arr[j]:
            swaps += 1
            arr[j+1], arr[j] = arr[j], arr[j+1]

print("Sorted array:")
print(arr)
print(f"swaps: {swaps}, comparisons: {comparisons}")


"""Selection sort has 4 swaps and 6 comparisons, while bubble sort has 6 swaps and 6 comparisons
This means that selection sort is a better sorting algorithm"""