                                    ## While Loop ##


##Basic While Loop

#Approach 1
starting_index = 0
while starting_index < 300:
    starting_index +=1
    print(starting_index)
    if starting_index == 20:
        break
    
#Approach 2
range_Start = 10
while range_Start < 10000000000000000000000:
    range_Start *=2
    print(range_Start)


##Break while Loop

#Approach 1

starting_index = 0
while starting_index <1000:
    starting_index += 1
    print(starting_index)
    if starting_index ==60:
        break
#Approach 2
main_range = 10
while main_range <1000:
    main_range += 1
    if main_range == 800:
        continue
    print(main_range)
        
##The else Statement

#Approach 1

starting_range = 0
while starting_range <6:
    starting_range +=1
    print(starting_range)
else:
        print(f"{starting_range} is not smaller to end length")


































