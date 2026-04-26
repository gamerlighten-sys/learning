print("welcome to value swapper!!!")

first_value = int(input("enter first value: "))
second_value = int(input("enter second value: "))
print("before swap:", first_value, second_value)

temp = second_value
second_value = first_value
first_value = temp

print("after swap:", first_value, second_value)

