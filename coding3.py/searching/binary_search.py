def binary_search(arr, key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        else:
            if key < arr[mid]:
                end = mid - 1   # so that we ignore the current mid
            else:
                start = mid + 1     # so that we ignore the current mid
    return -1
        
arr = [1, 3, 4, 6, 7, 9, 12, 15, 18, 27]
key = int(input("Enter number to be found: "))

if binary_search(arr, key) == -1:
    print("key was not found in the array")
    exit(0)

print(binary_search(arr, key))