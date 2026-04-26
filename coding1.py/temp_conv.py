# input number
# input(celsius) × 1.8 + 32
# print farenheit

print("what do you want to convert (pick 1 or 2)")
print("1. farenheit -> celsius")
print("2. celsius -> farenheit")
choice = int(input("enter choice: "))
print()

if choice == 1:
    farenheit = float(input("enter degrees farenheit here: "))
    celsius = (farenheit - 32) * 5/9
    print()
    print(farenheit,"degrees farenheit is", celsius,"degrees celsius")


elif choice == 2:
    celsius = float(input("enter degrees celsius here: "))
    farenheit = celsius * 1.8 + 32
    print()
    print(celsius,"degrees celsius is", farenheit,"degrees farenheit")