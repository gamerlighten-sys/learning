number = int(input("enter number till where you would like to calculate odd/even sum: "))

even_sum = 0
odd_sum = 0


for i in range(0, number + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    
print(f"Even Sum: {even_sum}")
print(f"Odd Sum: {odd_sum}")