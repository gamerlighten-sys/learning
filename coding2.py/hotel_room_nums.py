floors = int(input("enter number of floors: "))
if floors > 99 or floors < 1:
    print("please enter a number from 1 to 99")
    exit(0)

rooms_in_each_floor = int(input("enter number of rooms in each floor: "))
if rooms_in_each_floor > 99 or rooms_in_each_floor < 1:
    print("please enter a number from 1 to 99")
    exit(0)

room_num = 1

if floors > 99 or rooms_in_each_floor > 99 or floors < 1 or rooms_in_each_floor < 1:
    print("please enter a number from 1 to 99")

for i in range(1, floors + 1):
    for j in range(1, rooms_in_each_floor + 1):
        if room_num < 10:
            if i < 10:
                print(f"0{i}0{room_num}")
            else:
                print(f"{i}0{room_num}")
        
        else:
            if i < 10:    
                print(f"0{i}{room_num}")
            else:
                print(f"{i}{room_num}")
        room_num += 1
    room_num = 1