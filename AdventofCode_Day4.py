#AdventofCode_Day4
#%%
Shifts = [1,2,3,4,5,6,7,8,9]

Elf_1 = [2,3,4]
Elf_2 = [6,7,8]
Pair_1 = (Elf_1, Elf_2)

Elf_3 = [2,3]
Elf_4 = [4,5]
Pair_2 = (Elf_3, Elf_4)

Elf_5 = [5,6,7]
Elf_6 = [7,8,9]
Pair_3 = (Elf_5, Elf_6)

Elf_7 = [2,3,4,5,6,7,8]
Elf_8 = [3,4,5,6,7]
Pair_4 = (Elf_7, Elf_8)

Elf_9 = [6]
Elf_10 = [4,5,6]
Pair_5 = (Elf_9, Elf_10)

Elf_11 = [2,3,4,5,6]
Elf_12 = [4,5,6,7,8]
Pair_6 = (Elf_11, Elf_12)
#%%
print(Pair_5[0])

#%%
def Check_IfIn(Pair):
    x = 0
    for i in Pair[0]:
        if i in Pair[1]:
            x = x + 1
        else:
            pass
        if x == len(Pair[0]):
            return 1
        else:
            pass
    x = 0
    for i in Pair[1]:
        if i in Pair[0]:
            x = x + 1
        else:
            pass
        if x == len(Pair[1]):
            return 1
        else:
            pass
    return 0
Check_IfIn(Pair_4)
# %%
all_pairs = [Pair_1, Pair_2, Pair_3, Pair_4, Pair_5, Pair_6]
for i in all_pairs:
    list_check = Check_IfIn(i)
    if list_check == 1:
        print(f'Pair {all_pairs.index(i) + 1} has a overlapping schedule!')
    else:
        pass
# %%
