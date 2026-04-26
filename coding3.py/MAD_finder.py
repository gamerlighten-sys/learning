mean_counter = 0
abs_counter = 0
mad_counter = 0

def find_mean(arr):
    global mean_counter
    mean_counter += 1
    return sum(arr)/len(arr)

def find_absolute_value(number):
    global abs_counter
    abs_counter += 1
    return abs(number)

def find_MAD(arr):
    global mad_counter
    mad_counter += 1
    absolute_deviation_arr = []
    mean = find_mean(arr)
    for num in arr:  
        difference = num - mean
        absolute_deviation_arr.append(find_absolute_value(difference))
    mad = find_mean(absolute_deviation_arr)
    return mad


arr = []
length = int(input("What is the length of the set of numbers: "))
for i in range(length):
    num = float(input("Enter a number: "))
    arr.append(num)

print(find_MAD(arr))
print(mean_counter, abs_counter, mad_counter)
