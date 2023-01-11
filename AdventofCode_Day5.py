#AdventofCode_Day5
#%%
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
