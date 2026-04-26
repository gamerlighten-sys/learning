def linear_search(num_list, key):
    for i in range(len(num_list)):
        if key == num_list[i]:
            return i
    return None
        
num_list = [7, 18, 2, 1, -9, -4, -5]
key = int(input("Enter the number you want to find: "))

if linear_search(num_list, key) == None:
    print(f"{key} is not present in the list")
else:
    print(f"{key} was found at index {linear_search(num_list, key)}")