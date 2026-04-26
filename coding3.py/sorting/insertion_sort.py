arr = [3, 2, -1, 8, 14, -6, 7]

for i in range(1, len(arr)):
    j = i - 1  # to compare with the previous elements and see where the key belongs
    key = arr[i]

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
print(arr)