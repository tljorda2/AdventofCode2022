#AdventofCode_Day5
#%%
# This was used for the example.
crate_dict = {'Crate1': ['N', 'Z'], 'Crate2': ['D', 'C', 'M'], 'Crate3': ['P']}
#PROCEDURE
#move 1 from 2 to 1
#move 3 from 1 to 3
#move 2 from 2 to 1
#move 1 from 1 to 2

# The goal here is to write a code the follows the procedure above, transfering certain items within each crate to 
# different ones. The order of the items in the dictionary are ordered from top to bottom
# The first element is at the top of the crate and the last is at the bottom
# Each item can only be moved one at a time, for example, when moving two items from Crate 1 to Crate 2, 
# You wwill first move item N and it will be on top of Crate two making N,D,C,M.
# Next you would move item Z, making the order of crate two Z,N,D,C,M

#Creating a function that can take different inputs and calculate how to move the crates
# Current cargo is the dictionary of how it is currently arranged, crate_start is what crate the item is being taken from
# crate_end is where the item is going and total_moved is the total number moved
def Crate_Move(current_cargo, crate_start, crate_end, total_moved):
    move_variable = total_moved
    # Loop to move the number of requested items
    for i in range(move_variable):
        # Gets the top item of the crate
        current_item_moved = current_cargo[crate_start][0]
        
        #removes that current item from the first crate
        current_cargo[crate_start].remove(current_item_moved)
        # Adds the current item to the new crate, at the top of it
        current_cargo[crate_end].insert(0, current_item_moved)
    return current_cargo
        
    
    
# Using the function through each of step of the procedure
move1 = Crate_Move(crate_dict, 'Crate2', 'Crate1', 1)
move2 = Crate_Move(move1, 'Crate1', 'Crate3', 3)
move3 = Crate_Move(move2, 'Crate2', 'Crate1', 2)
final = Crate_Move(move3, 'Crate1', 'Crate2', 1)
print(final)
# Answer:
#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# %%
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\\AoC_05\\AoCDay5_Data.txt') as file:
    AoCDay5_Data = file.readlines()
file.close()
# %%
# Turning the data into a list of dictionaries
all_commands = []
for line in AoCDay5_Data:
    line = line.split()
    # Create an empty dictionary
    my_dict = {line[0]: line[1], line[2]: line[3], line[4]: line[5]}
    all_commands.append(my_dict)
        
# Loop through the list and add values to the dictionary
    # for i in range(0, len(line), 2):
    #     my_dict[line[i]] = line[i+1]
    #     all_commands.append(my_dict)
# for whatever reason, it create many duplicates
# del all_commands[::2]
# del all_commands[::3]

# %%
# This is the starting position of the crates
# [M]                     [N] [Z]    
# [F]             [R] [Z] [C] [C]    
# [C]     [V]     [L] [N] [G] [V]    
# [W]     [L]     [T] [H] [V] [F] [H]
# [T]     [T] [W] [F] [B] [P] [J] [L]
# [D] [L] [H] [J] [C] [G] [S] [R] [M]
# [L] [B] [C] [P] [S] [D] [M] [Q] [P]
# [B] [N] [J] [S] [Z] [W] [F] [W] [R]
#  1   2   3   4   5   6   7   8   9
crate_dict = {1: ['M', 'F', 'C', 'W', 'T', 'D', 'L', 'B'], 
              2: ['L', 'B', 'N'],
              3: ['V', 'L', 'T', 'H', 'C', 'J'], 
              4: ['W', 'J', 'P', 'S'],
              5: ['R', 'L', 'T', 'F', 'C', 'S', 'Z'], 
              6: ['Z', 'N', 'H', 'B', 'G', 'D', 'W'],
              7: ['N', 'C', 'G', 'V', 'P', 'S', 'M', 'F'],
              8: ['Z', 'C', 'V', 'F', 'J', 'R', 'Q', 'W'],
              9: ['H', 'L', 'M', 'P', 'R']}
# Running the function on each dictionary
for i in all_commands:
    CrateStart = int(i['from'])
    CrateEnd = int(i['to'])
    TotalMoved = int(i['move'])
    x = Crate_Move(crate_dict, CrateStart, CrateEnd, TotalMoved)
    crate_dict = x
print(crate_dict)
# %%
# This will give me the final answer for the first part
Top_of_Crate = ''
for key, value in crate_dict.items():
    Top_of_Crate = Top_of_Crate + value[0]
print(Top_of_Crate)
# %%
# Part 2
# For part 2, instead of moving one at a time, we are able to move all of them at the same time
def Crate_Move2(current_cargo, crate_start, crate_end, total_moved):
    # move_variable = total_moved
    # # Loop to move the number of requested items
    # for i in range(move_variable):
        # Gets the top item of the crate
    # Using the index like that to pull the all the items being moved from the top of the crate
    current_item_moved = current_cargo[crate_start][0:total_moved]
    #removes that current item from the first crate
    # This for loop will remove all of the items in the list that are being removed from the crate
    for i in current_item_moved:
        current_cargo[crate_start].remove(i)
    # Adds the current item to the new crate, at the top of it
    # This adds those to the ending crate in a reversed order since we can now move all of the items at once
    # This means that the item in the last spot of the current_items_moved should still be in the last spot when inserted into the next list
    current_item_moved = list(reversed(current_item_moved))
    for i in current_item_moved:
        current_cargo[crate_end].insert(0, i)
    return current_cargo
#%%
crate_dict = {1: ['M', 'F', 'C', 'W', 'T', 'D', 'L', 'B'], 
              2: ['L', 'B', 'N'],
              3: ['V', 'L', 'T', 'H', 'C', 'J'], 
              4: ['W', 'J', 'P', 'S'],
              5: ['R', 'L', 'T', 'F', 'C', 'S', 'Z'], 
              6: ['Z', 'N', 'H', 'B', 'G', 'D', 'W'],
              7: ['N', 'C', 'G', 'V', 'P', 'S', 'M', 'F'],
              8: ['Z', 'C', 'V', 'F', 'J', 'R', 'Q', 'W'],
              9: ['H', 'L', 'M', 'P', 'R']}
# Running the function on each dictionary
for i in all_commands:
    CrateStart = int(i['from'])
    CrateEnd = int(i['to'])
    TotalMoved = int(i['move'])
    x = Crate_Move2(crate_dict, CrateStart, CrateEnd, TotalMoved)
    crate_dict = x
print(crate_dict)
# %%
# This will give me the final answer for the second part
Top_of_Crate = ''
for key, value in crate_dict.items():
    Top_of_Crate = Top_of_Crate + value[0]
# The answer for these questions would be a string of the items at the top of all the crates
# This will give me that string
print(Top_of_Crate)
# %%
