num_of_first_name = int(input("how many first names do you want: "))
num_of_last_name = int(input("how many last names do you want: "))
FirstNames = []
LastNames = []

for i in range(num_of_first_name):
    name = str(input("enter First name: "))
    FirstNames.append(name)

for i in range(num_of_last_name):
    name = str(input("enter Last name: "))
    LastNames.append(name)

for Lname in LastNames:
    for Fname in FirstNames:
        print(Fname, Lname)