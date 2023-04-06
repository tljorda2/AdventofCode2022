# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 12:05:26 2023

@author: cacru
"""
import re

# Opening the text file containing the input data and turning it into a list of list pairs
with open("C:\\Users\\cacru\\OneDrive\\Desktop\\AoCDay10_Data.txt") as file:
    AoCDay9_Data = file.readlines()
file.close()
pattern = r'[\n]'

New_Data = []
for i in AoCDay9_Data:
    new_string = re.sub(pattern, '', i)
    new_list = new_string.split()
    New_Data.append(new_list)
while True:
    break
# noop is do nothing
# addx adds a value
def main():
    start_value = 1
    cycle = 1
    multiplier = list(range(20,221,40))
    signal_strength = []
    for command in New_Data:
        if command[0] == 'noop':
            if cycle in multiplier:
                signal_strength.append(cycle*start_value)
                print(cycle, start_value)
            else:
                pass
            cycle += 1
        elif command[0] == 'addx':
            if cycle in multiplier:
                signal_strength.append(cycle*start_value)
                print(cycle, start_value)
            else:
                pass
            cycle += 1
            if cycle in multiplier:
                signal_strength.append(cycle*start_value)
                print(cycle, start_value)
            else:
                pass
            start_value += int(command[1])
            cycle += 1
    return signal_strength
#%%
# Lower 14760
# Higher 12980
answer = main()
print(sum(answer))
#%%
def reset():
    dot_line = ''
    for i in range(40):
        dot_line += '.'
    return dot_line

def main2():
    dot_line_cycle = reset()
    dot_line_final = reset()
    start_value = 1
    cycle = 0
    multiplier = list(range(20,221,40))
    signal_strength = []
    for command in New_Data:
        if command[0] == 'noop':
            dot_line_cycle = dot_line_cycle[:start_value-1] + '###' + dot_line_cycle[start_value+2:]
            dot_line_final = dot_line_final[:cycle] + dot_line_cycle[cycle] + dot_line_final[cycle+1:]
            dot_line_cycle = reset()
            if cycle == 39:
                #print line and reset dot_line
                signal_strength.append(cycle*start_value)
                print(dot_line_final)
                dot_line_final = reset()
                cycle = 0
            else:
                cycle += 1
        elif command[0] == 'addx':
            dot_line_cycle = dot_line_cycle[:start_value-1] + '###' + dot_line_cycle[start_value+2:]
            dot_line_final = dot_line_final[:cycle] + dot_line_cycle[cycle] + dot_line_final[cycle+1:]
            dot_line_cycle = reset()
            if cycle == 39:
                #print line and reset dot_line
                signal_strength.append(cycle*start_value)
                print(dot_line_final)
                dot_line_final = reset()
                cycle = 0
            else:
                cycle += 1
            dot_line_cycle = dot_line_cycle[:start_value-1] + '###' + dot_line_cycle[start_value+2:]
            dot_line_final = dot_line_final[:cycle] + dot_line_cycle[cycle] + dot_line_final[cycle+1:]
            dot_line_cycle = reset()
            if cycle == 39:
                #print line and reset dot_line
                signal_strength.append(cycle*start_value)
                print(dot_line_final)
                dot_line_final = reset()
                cycle = 0
            else:
                cycle += 1
            start_value += int(command[1])
    return signal_strength


#%%
while True:
    break
main2()