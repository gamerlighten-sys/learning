arr = [3, 2, -1, 8, 14, -6, 7]
print("Length of array:", len(arr))
swaps, comparisons = 0, 0

for i in range(len(arr)):   # defines number of iterations
    for j in range(len(arr)-i-1): # does the actual compare and swap
        comparisons += 1
        if arr[j+1] < arr[j]:
            swaps += 1
            arr[j+1], arr[j] = arr[j], arr[j+1]

print(arr)
print(f"swaps: {swaps}, comparisons: {comparisons}")