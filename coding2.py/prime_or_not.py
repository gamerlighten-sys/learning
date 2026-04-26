number = int(input("enter number to see if it's prime: "))
prime_or_not = ""

if number == 2:
    print(f"{number} is prime")
    exit(0)
elif number == 1 or number <= 0:
    print(f"{number} isn't prime")
    exit(0)


for i in range(2, number):
    if number % i == 0:
        prime_or_not = "isn't prime"
        break
    elif number % i != 0:
        prime_or_not = "is prime"

print(number, prime_or_not)