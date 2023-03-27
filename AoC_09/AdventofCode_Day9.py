# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:53:59 2023

@author: cacru
"""
import re

# Opening the text file containing the input data and turning it into a list of list pairs
with open("C:\\Users\\cacru\\OneDrive\\Desktop\\AoCDay9_Data.txt") as file:
    AoCDay9_Data = file.readlines()
file.close()
pattern = r'[\n]'

New_Data = []
for i in AoCDay9_Data:
    new_string = re.sub(pattern, '', i)
    new_list = new_string.split()
    New_Data.append(new_list)
    
print(New_Data)
test = ['R 4'.split(), 'U 4'.split(), 'L 3'.split(),
        'D 1'.split(), 'R 4'.split(), 'D 1'.split(),
        'L 5'.split(), 'R 2'.split()]

#%%
# returns 2 variables that should be assigned like a, b =
# Honestly may be redundant
def Rope_Directions(direction_movement):
    direction = direction_movement[0]
    movement = int(direction_movement[1])
    return [direction, movement]

# This returns a cooridinate corresponding to the direction
# The X coord represents Left and Right, where Right is positive
# The Y coord represents Up and Down, where up is positive
def Direction(arg):
    valid_args = ['U', 'D', 'R', 'L']
    try:
        arg.upper()
    except:
        raise TypeError(f'arg must be a string in {valid_args}')
    if arg not in valid_args:
        raise TypeError(f'arg must be a string in {valid_args}')
    if arg == 'U':
        return [0, 1]
    elif arg == 'D':
        return [0, -1]
    elif arg == 'R':
        return [1, 0]
    elif arg == 'L':
        return [-1, 0]

# This is manhattan distance used to check the distance from the head to the tail
# If the manhattan distance is 3, the tail needs to be moved diagonal
def DistanceCheck(lst1, lst2):
    if len(lst1) == len(lst2):
        pass
    else:
        raise ValueError('The inputs need to be the same length')
    manhattan = 0
    for i in range(len(lst1)):
        sum_ = abs(lst1[i] - lst2[i])
        manhattan += sum_
    return manhattan

# This checks if the tail needs to be moved diagonally
def Diagonal(distance):
    if distance >= 3:
        return True
    else:
        return False
    
# This determines how to move the tail diagonally using its current coordinates
# It needs to move diagonally based on the direction of the heads position
def DiagonalDirection(lst1, lst2):
    # Comparing the x and y for each coordinate
    x1 = lst1[0]
    x2 = lst2[0]
    y1 = lst1[1]
    y2 = lst2[1]
    # if both coords are greater in the first, the tail needs to move in the negative direction
    if x1>x2 and y1>y2:
        return [-1, -1]
    #Checks if x1(head) is greater than x2(tail) and y1 is LESS THAN y2
    elif x1>x2 and y1<y2:
        return [-1, 1]
    elif x1<x2 and y1>y2:
        return [1, -1]
    elif x1<x2 and y1<y2:
        return [1, 1]

# An added check to make sure that the head is not in the same row or column as the tail if 
# the manhattan distance is 3
# It should never get to this situation though
def tail_move(lst1, lst2):
    if lst1[0] == lst2[0] or lst1[1] == lst2[1]:
        return True
    else:
        return False

def euclidian(lst1, lst2):
    # Im not going to make this generalized
    x = abs(lst1[0] - lst2[0])
    y = abs(lst1[1] - lst2[1])
    z = x**2 + y**2
    return [x,y]
def main_(head_pos, tail_pos, movearg, unique_positions):
    # head_pos is the current position of the head: [x,y]
    # tail_pos is the current position of the tail: [x,y]
    # movearg should be the command movement in the form of a list [Direction, Spaces]
    # getting the commands first and transforming the Spaces into an int
    commands = Rope_Directions(movearg)
    # Getting the direction in a coordinate format
    '''
    [1,0] is right
    [0,1] is up
    [-1,0] is left
    [0,-1] is down
    '''
    numerical_direction = Direction(commands[0])
    # Now we have the direction here stored
    # creating an empty list that will be used to store the unique positions visited by the tail
    # Now that we have a coord representation o fhow to move, we need to move
    for i in range(commands[1]):
        # Moving the head position once
        head_pos = listadd(head_pos, numerical_direction)
        # Getting the distance between the head position and the tail position
        dist = DistanceCheck(head_pos, tail_pos)
        # Creating a flag to see if the distance is equal to or greater than 3
        flag = Diagonal(dist)
        # If statement to move the tail diagonally if needed
        if flag == True:
            # Getting the direction that the tail needs to move in a coordinate format
            diag = DiagonalDirection(tail_pos, head_pos)
            # second flag to see if the tail is in the same column or row as the head
            # This should never occur if the distance is equal to or greater than 3
            flag2 = tail_move(head_pos, tail_pos)
            if flag2 == True:
                return ValueError('Tail is in the same row/column as the head and the distance is greater than 2')
            else:
                # This is where the tail diagnoal movement should come in
                tail_pos = listadd(tail_pos, diag)
        else:
            if DistanceCheck(head_pos, tail_pos) == 1:
                continue
            elif euclidian(head_pos, tail_pos) == [1,1]:
                continue
            # This was the line that led me to be stuck for months
            # I forgot to add a flag that checks if the head and tail are in the same spot
            # This is something that is okay to happen
            # Main issue with my code before is this basically pushed the tail rope
            # They would never be on the same coordinate
            elif head_pos == tail_pos:
                continue
            else:
                tail_pos = listadd(tail_pos, numerical_direction)
        # Adding the unique positions to a list
        if tail_pos in unique_positions:
            pass
        else:
            unique_positions.append(tail_pos)

    return unique_positions, head_pos, tail_pos
    
    #for i in range(number):
'''
CURRENT STEP BY STEP
---------------------
1. Rope Direction will take in the movearg and convert it into [str(), int()]
    a. EX: ['U', '5'] to ['U', 5]
2. Next, numerical_directions will turn the str direction into a coord value
    a. EX: 'U' will become [0,1]. It is in [x, y] format
3.Start of the for loop now
4. 
'''
def listadd(lst1, lst2):
    new_list = [lst1[i] + lst2[i] for i in range(len(lst1))]
    return new_list
# %%i in range

# Creating an empty list that will contain all of the unique positions
# Also the starting positions of the head and tail
unique_pos = []
head = [0,0]
tail = [0,0]
for i in New_Data:
    unqiue_pos, head, tail = main_(head, tail, i, unique_pos)

#%%
# PART 2
# Try and make this for any length rope.
# This scenario will have a rope of 10 knots, where the last knot is the new tail
# Going to try and use a for loop to iterate through a list of the back half of the rope\

def part_move(h, t):
    if h[0] == t[0]:
        if h[1] > t[1]:
            return [0, 1]
        elif h[1] < t[1]:
            return [0, -1]
    elif h[1] == t[1]:
        if h[0] > t[0]:
            return [1, 0]
        elif h[0] < t[0]:
            return [-1, 0]
    else:
        return 'UHHHHHH IDK MAN'
        
def main2(head_pos, tail_lst, movearg, unique_positions):
    # head_pos is the current position of the head: [x,y]
    # tail is going to be a list of of all tail positions
    # movearg should be the command movement in the form of a list [Direction, Spaces]
    # getting the commands first and transforming the Spaces into an int
    commands = Rope_Directions(movearg)
    numerical_direction = Direction(commands[0])
    for i in range(commands[1]):
        head_pos = listadd(head_pos, numerical_direction)
        tail1 = tail_lst[0]
        dist = DistanceCheck(head_pos, tail1)
        flag = Diagonal(dist)
        if flag == True:
            diag = DiagonalDirection(tail1, head_pos)
            flag2 = tail_move(head_pos, tail1)
            if flag2 == True:
                raise ValueError('Tail is in the same row/column as the head and the distance is greater than 2')
            else:
                tail_lst[0] = listadd(tail1, diag)
        else:
            if DistanceCheck(head_pos, tail1) == 1:
                pass
            elif euclidian(head_pos, tail1) == [1,1]:
                pass
            elif head_pos == tail1:
                pass
            else:
                tail_lst[0] = listadd(tail1, numerical_direction)
        counter = 0
        for knot in tail_lst[1:]:
            temp_head = tail_lst[counter]
            dist2 = DistanceCheck(temp_head, knot)
            flag = Diagonal(dist2)
            if flag == True:
                diag = DiagonalDirection(knot, temp_head)
                flag2 = tail_move(temp_head, knot)
                if flag2 == True:
                    raise ValueError('Tail is in the same row/column as the head and the distance is greater than 2')
                else:
                    tail_lst[counter+1] = listadd(knot, diag)
            else:
                if DistanceCheck(temp_head, knot) == 1:
                    pass
                elif euclidian(temp_head, knot) == [1,1]:
                    pass
                elif temp_head == knot:
                    pass
                else:
                    new_move = part_move(temp_head, knot)
                    tail_lst[counter+1] = listadd(knot, new_move)
            counter += 1
        tail_len = len(tail_lst)
        true_tail = tail_lst[tail_len-1]
        if true_tail in unique_positions:
            pass
        else:
            unique_positions.append(true_tail)
    return unique_positions, head_pos, tail_lst


#%%
unique_pos = []
head = [0,0]
tail = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
for i in New_Data:
    unqiue_pos, head, tail = main2(head, tail, i, unique_pos)
        
        