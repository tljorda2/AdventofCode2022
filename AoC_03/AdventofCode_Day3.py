# Advent of Code Day 3
#%%
# This day for advent of code gave us the following strings
# It wants us to split this strings in half and find the common letters between the two halfs
# After that, each letter has a specific value assigned to it
# The value is in alphabetical order with a = 1 and z = 27. Additionally, capital letters are treated differently
# A = 28 while Z = 54
# Here I created variables for the strings to make them easier to manage
# I used these to test the code
# rucksack1 = 'vJrwpWtwJgWrhcsFMMfFFhFp'
# rucksack2 = 'qHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
# rucksack3 = 'PmmdzqPrVvPwwTWBwg'
# rucksack4 = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
# rucksack5 = 'ttgJtRGJQctTZtZT'
# rucksack6 = 'CrZsJsPPZsGzwwsLwLmpwMDw'

# Creating a new list in order to iterate through the strings with one for loop
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\\AoC_03\\AoCDay3_Data.txt') as file:
    total_storage = file.readlines()
# This is going to be the list for the new strings that came from splitting the current ones in half
compartment_list = []
file.close()
for i in total_storage:
    n = int(len(i)/2)
    compartment1 = i[0:n]
    compartment2 = i[n:]
    compartment_list.append([compartment1, compartment2])
# Here I am creating new list variables that we are going to append later
# This is for the overall common letters
common_letters = []
internal_common_letters = []
for i in compartment_list:
    lst1_unique = set(i[0])
    for letter in lst1_unique:
        lst2_unique = set(i[1])
        if letter in lst2_unique:
            internal_common_letters.append(letter)
common_letters.append(internal_common_letters)

# String that I am going to interate through to get a list that is easier to get the integer location of the letters
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = []
for let in alphabet:
    lst.append(let)

# Here I calculate the final value
total_value=0
for item in common_letters[0]:
    # I add one to the index of the current letter since a = 1 and index starts at 0
    value = int(lst.index(item)) + 1
    total_value = value + total_value
# The answer should be 157
print(total_value)

# %%
# Part 2
# For part two, every three lines of the input will have a common letter, I need to go through those three lines, find the common letter, 
# and figure out its value and the sum of all those letters
# total_storage = list(zip(*[iter(total_storage)]*3))


# %%
# This code serperate every three lines into its own list which will be used to find the common letters.
x = 1
lst = []
temporary_lst = []
for line in total_storage:

    if x < 3:
        temporary_lst.append(line)
        x += 1
    elif x == 3:
        temporary_lst.append(line)
        x = 1
        lst.append(temporary_lst)
        temporary_lst = []
print(lst)
# %%
# This is one mess of a for loop that iterates through the list made above of every three lines
final_list = []
for i in lst:
    unique_letters = []
    x = 0
    for string in i:
        # Go through and make sets of the unique characters
        if x == 0:
            unique = set(string)
            x += 1
        elif x == 1:
            unique2 = set(string)
            x += 1
        elif x == 2:
            unique3 = set(string)
            x = 0
            # Turn them back to lists and combine them
            # I tend to make everything into list5s if possible because they are what I am most comfortable with
            unique = list(unique)
            unique2 = list(unique2)
            unique3 = list(unique3)
            # Combining them and then getting the values that appeared over 2 times, which would be the shared letter for all three
            unique = unique + unique2 + unique3
            unique = set([x for x in unique if unique.count(x) > 2])
            # There is a single instance that does not have the \n in it, so I just made this to remove all of them except that one instance
            try:
                unique.remove('\n')
            except:
                print(unique)
            unique = list(unique)
            final_list.append(unique[0])
print(final_list)
                    
# %%
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = []
for let in alphabet:
    lst.append(let)

# Here I calculate the final value
total_value=0
for item in final_list:
    # I add one to the index of the current letter since a = 1 and index starts at 0
    value = int(lst.index(item)) + 1
    total_value = value + total_value
# The answer should be 157
print(total_value)
# %%
