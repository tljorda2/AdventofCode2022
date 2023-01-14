
# Advent of Code 2022 Number One
# %%

# Opening the text file that has the data
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\AoCDay1_Data.txt') as file:
    # Reading all of the lines
    Day1_Data = file.readlines()
file.close()
# Setting up two variables. As we go through the file, one will keep track of the sum for the current elf while the other will have the current max of all elves
current_max = 0
current_sum = 0
# Iterating through the data
for d in Day1_Data:
    # Elves are seperated by blank lines, so if we come across one, it is the end of the current elf
    if d == "\n":
        current_max = max(current_sum, current_max)
        current_sum = 0
    else:
        current_sum += int(d)

print(current_max)
# %%
# Part two
# Part two wants us to figure out the max for the top three elves
total_calories = []
current_sum = 0
for line in Day1_Data:
    if line == '\n':
        total_calories.append(current_sum)
        current_sum = 0
    else:
        current_sum += int(line)
# Sorting the list and then getting the top three values that way
total_sorted = sorted(total_calories)
top_three = total_sorted[-3:]
sum(top_three)
# %%
