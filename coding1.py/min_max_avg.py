print("\nin this website we will take the numbers you enter")
print("and find the Largest, Smallest, and Average\n")
num = 1
num_list = []
num_sum = 0
largest_num = -10000000
smallest_num = 10000000

while (num != 0):
    num = int(input("enter number between -1 mil to 1 mil (enter 0 to stop): "))
    if num != 0:
        num_list.append(num)
    #    num_list += [num]
    
    num_sum += num
    
    # if largest_num < num:
    #     largest_num = num

    # if smallest_num > num and num != 0:
    #     smallest_num = num

    if num > largest_num:
        largest_num = num

    if num < smallest_num and num != 0:
        smallest_num = num


print(num_list)

# largest
print(f"Largest Number: {largest_num}")

# smallest
print(f"Smallest Number: {smallest_num}")

# average
average = num_sum / len(num_list)
print(f"Average Number: {average}")