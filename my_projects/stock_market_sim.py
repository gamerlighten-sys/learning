"""
in this code you can buy shares that randomely change every 2 seconds, using the random module
there will be a graph that is randomely changes every 2 seconds, in sync with the price of your stock

the goal for the user of this program is to hit 1 million dollars
- they will start with 1000 dollars
- goal and starting money can change later after testing for balancing
"""

import random, time

count_of_days = time.perf_counter()
situations = ["/", "\_", "_"]
up_down = [None, True, False]


microsoft = 100
# nike = 55
# mcdonalds = 80
# spacex = 205
# apple = 120
# ashley = 15
# chipotle = 1010

for i in range(1, 1000):
    print(f"day {i} has begun")
    count_of_days = time.perf_counter = 0
    while count_of_days <= 45:
        option = random.randint(0, 2)
        change = random.randint(0, 1)
        if change == True and option == "/":
            print(situations[option], end="")
        time.sleep(1)




#                         ___/
#         |\____         /
#        _|     \_    __|
#       /         \__/