# Advent of Code Day 3
#%%
# This day for advent of code gave us the following strings
# It wants us to split this strings in half and find the common letters between the two halfs
# After that, each letter has a specific value assigned to it
# The value is in alphabetical order with a = 1 and z = 27. Additionally, capital letters are treated differently
# A = 28 while Z = 54
# Here I created variables for the strings to make them easier to manage
rucksack1 = 'vJrwpWtwJgWrhcsFMMfFFhFp'
rucksack2 = 'qHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
rucksack3 = 'PmmdzqPrVvPwwTWBwg'
rucksack4 = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
rucksack5 = 'ttgJtRGJQctTZtZT'
rucksack6 = 'CrZsJsPPZsGzwwsLwLmpwMDw'

# Creating a new list in order to iterate through the strings with one for loop
total_storage = [rucksack1, rucksack2, rucksack3, rucksack4, rucksack5, rucksack6]
# This is going to be the list for the new strings that came from splitting the current ones in half
compartment_list = []

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
