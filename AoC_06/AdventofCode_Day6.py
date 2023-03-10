# This day for the Advent of Code wants us to take a string and find the character that 
# Starts a sequence of 4 unique characters.
#%%
# These first four strings were test strings
# string = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
# string1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
# string2 = 'nppdvjthqldpwncqszvftbrmjlhg'
# string3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
# Read the text file and save the string into a variable
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\\AoC_06\\AoCDay6_Data.txt') as file:
    file_string = file.readlines()
    string4 = file_string[0]
#%%
# This is a function that will go through the string and locate the first sequence of 4 unique characters
def Packet_Decoder(string):
    # Variables for the function
    current_position = 0
    string_list = list(string)
    x = ''
    # For loop to iterate through each letter of the string
    for letter in string_list:
        # Getting the current position of the letter
        current_position = current_position + 1
        if letter not in x:
            x = x + letter
            # If statement to check if we have met the required length of the string to stop. It needs to be five since
            # the counter starts with 1 and we are adding one in the for loop
            if len(x) == 4:
                return [current_position, x]

        elif letter in x:
            # Getting an integer value that I can use to slice the string and cut out everything before the 
            # repeat number
            letter_pos = x.rfind(letter)+1
            # Slicing the string and adding the new letter
            x = x[letter_pos:]
            x = x + letter
    return 'There are no strings of 4 letters that are unique'
            
# %%
# The answer for Part One
print(Packet_Decoder(string4))
# Part Two
# %%
# Instead of 4 characters, it wants 14
# For this, I could use the same exact function, just change the len() function check to 14
# Resuing the same function:
def Packet_Decoder2(string):
    # Variables for the function
    current_position = 0
    string_list = list(string)
    x = ''
    # For loop to iterate through each letter of the string
    for letter in string_list:
        # Getting the current position of the letter
        current_position = current_position + 1
        if letter not in x:
            x = x + letter
            # If statement to check if we have met the required length of the string to stop. It needs to be five since
            # the counter starts with 1 and we are adding one in the for loop
            if len(x) == 14:
                return [current_position, x]

        elif letter in x:
            # Getting an integer value that I can use to slice the string and cut out everything before the 
            # repeat number
            letter_pos = x.rfind(letter)+1
            # Slicing the string and adding the new letter
            x = x[letter_pos:]
            x = x + letter
    return 'There are no strings of 4 letters that are unique'

print(Packet_Decoder2(string4))
# %%
