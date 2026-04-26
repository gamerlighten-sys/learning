arr = [3, 2, -1, 8, 14, -6, 7]

swaps, comparisons = 0, 0

for i in range(len(arr)): # iterate n number of times to sort the entire array

    # doing this so that only the rest of the un sorted array is considered
    # i elemts are already sorted
    smallest = arr[i]
    smallest_index = i

    # j loop finds smallest element
    for j in range(i+1, len(arr)):  # i+1, since i elements are already sorted, works without i+1 as well

        element = arr[j]
        comparisons += 1
        if element < smallest:
            smallest = element
            smallest_index = j

    # swaps it and moves at the i-th place
    swaps += 1
    arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

print("Sorted array:")
print(arr)
print(f"Swaps: {swaps}, Comparisons: {comparisons}")