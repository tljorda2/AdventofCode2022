#%%
import math
import tkinter as tk
import black
#%%
sqr = math.sqrt()
def addition(x, y):
    answer = x+y
    return answer
def subtraction(x, y):
    answer = x-y
    return answer
def multiply(x, y):
    answer = x*y
    return answer
def division(x, y):
    answer = x/y
    return answer

#%%
root = tk.Tk()
root.geometry("312x324")
root.resizable(0,0)
root.title('Calculator')

#%%
# Advent of Code 2022 Number One
# Amount of calories each elf is carrying where the numbers represent the calories in the item
elf = {'elf1': [1000, 2000, 3000],
       'elf2': [4000], 'elf3':[5000, 6000],
       'elf4':[7000, 8000, 9000], 'elf5':[10000]}
# Need to find the elf with the most calories
for i in elf.keys():
    total = 0
    elf_total = {}
    for item in elf[i]:
        total = total + item
    # This is not working how I want it to. It is only storing the last elf
    elf_total.update({i: total})
    print(f'{i}: {total}')
print(elf_total)
# %%
# Advent of Code 2022 Number 2

black; "C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\baseball archive\\PitchData_Functions"
# %%
