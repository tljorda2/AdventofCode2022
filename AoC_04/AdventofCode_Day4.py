#AdventofCode_Day4
#%%
import re
# Shifts = [1,2,3,4,5,6,7,8,9]
# # Here I am defining each of the possible shifts fop the elves
# Elf_1 = [2,3,4]
# Elf_2 = [6,7,8]
# Pair_1 = (Elf_1, Elf_2)

# Elf_3 = [2,3]
# Elf_4 = [4,5]
# Pair_2 = (Elf_3, Elf_4)

# Elf_5 = [5,6,7]
# Elf_6 = [7,8,9]
# Pair_3 = (Elf_5, Elf_6)

# Elf_7 = [2,3,4,5,6,7,8]
# Elf_8 = [3,4,5,6,7]
# Pair_4 = (Elf_7, Elf_8)

# Elf_9 = [6]
# Elf_10 = [4,5,6]
# Pair_5 = (Elf_9, Elf_10)

# Elf_11 = [2,3,4,5,6]
# Elf_12 = [4,5,6,7,8]
# Pair_6 = (Elf_11, Elf_12)


#%%
# This is a function that allows me to check if the entire shift of one elf is in the shift of its pair
# 
def Check_IfIn(Pair):
    # Have to add one to the second value in order for it to include it
    Elf_1 = range(Pair[0][0],Pair[0][1]+1)
    Elf_2 = range(Pair[1][0],Pair[1][1]+1)
    x = 0
    # Checking to see if all of the values in the first elf are in elf 2
    for i in Elf_1:
        if i in Elf_2:
            x = x + 1
        else:
            pass
        if x == len(Elf_1):
            return 1
        else:
            pass
    # Checking to see if all of the values in the second elf are in the first
    x = 0
    for i in Elf_2:
        if i in Elf_1:
            x = x + 1
        else:
            pass
        if x == len(Elf_2):
            return 1
        else:
            pass
    return 0


#%%
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\\AoC_04\\AoCDay4_Data.txt') as file:
    AoCDay4_Data = file.readlines()
file.close()
# Taking out some of the extra characters to make it easier for me to interpret
pattern = r'[\n]'
# This reorganizes the data into pairs of lists with the integer assignemnts that makes it easier for me to slice
New_Data = []
for i in AoCDay4_Data:
    new_string = re.sub(pattern, '', i)
    new_list = new_string.split()
    new_list = new_list[0].split(',')
    temp_list = []
    for item in new_list:
        new_item = item.replace('-',',')
        x = new_item.split(',')
        integers = [int(str) for str in x]

        temp_list.append(integers)
        
    New_Data.append(temp_list)

# New_Data2 = []
# for i in New_Data:
#     new_list2 = i.split(',')
#     New_Data2.append()
# %%
# for loop to iterate through all of the items in the data
total_overlap = 0
for i in New_Data:
    list_check = Check_IfIn(i)
    if list_check == 1:
        total_overlap += 1
    else:
        pass
print(total_overlap)
# Answer should be 471
# %%
# Part 2
# Now it wants us to find where it is overlapping
# Copying the Check_IfIn function and adjusting it for this scenario

def Overlap(Pair):
    # Have to add one to the second value in order for it to include it
    Elf_1 = range(Pair[0][0],Pair[0][1]+1)
    Elf_2 = range(Pair[1][0],Pair[1][1]+1)

    # Checking to see if any of the values in the first elf are in elf 2
    for i in Elf_1:
        if i in Elf_2:
            return 1
    # Checking to see if any of the values in the second elf are in the first
    for i in Elf_2:
        if i in Elf_1:
            return 1
    return 0
#%%
# Running the same loop to iterate through all of the data
total_overlap = 0
for i in New_Data:
    list_check = Overlap(i)
    if list_check == 1:
        total_overlap += 1
    else:
        pass
print(total_overlap)
# Answer should be 888
# %%
