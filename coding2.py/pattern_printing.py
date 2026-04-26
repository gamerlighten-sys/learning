"""
1
1 2
1 2 3
1 2 3 4 
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

print()

"""
* * * * *
* * * *
* * *
* *
*
"""

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end = " ")
    print()

print()


"""
1 2 3
4 5 6
7 8 9
"""

count = 1
for i in range(1, 4):
    for j in range(1, 4):
        print(count, end = " ")
        count += 1
    print()

print()


"""
1 2 3
6 5 4
7 8 9
"""



"""
1 2 3
8 9 4
7 6 5
"""