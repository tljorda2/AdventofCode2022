# For this day, we are looking to clear up file space in a disk
# We need to delete all directories that have a total size under 100000
#%%
# This is what the file system looks like based on the commands given below
# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)

# Puzzle Input
# The $ represents commands to be executed
# cd means to change the directory
# cd x means to move inward one level while cd .. means to move outward one level
# cd / moves the current directory to the outermost one
# ls prints out all the current files and directories in the current directory
#-------------------
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
#-------------------
# Creating a dictionary to represent the fiel system
file_system = {'/':{'b.txt':14848514, 'c.dat':8504156, 
                    'a':{'f': 29116, 'g': 2557, 'h.lst': 62596,
                         'e':{'i': 584}},
                    'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}

# %%
# Refining the code above because it is kind of a mess
# I need to have every directory saved as a variable
# This means that each type the value in the key:value pair is a dictionary, it needs to be saved
# I think a for loop is going to be th ebest place to start, iterating through the dictionary
# I should try and make this a function
def filesize_calculator(dictionary: dict) -> dict:
    if type(dictionary) == dict:
        pass
    else:
        raise TypeError('The input needs to be a dictionary')
    #Creating a variable that can be returned from the function
    Folder_Storage = []
    # Variable to store the size of the files in the top level directory
    # I decided to use a dictionary to repsent the folder and storage size
    top_directory_size = {'/':0}
    for item in dictionary['/']:
        # Recieve the current value of the key
        current_item_size = dictionary['/'].get(item)
        # If else statement to check if it is a file or a folder
        # If it is a folder, it will have another dictionary as its value
        if type(current_item_size) == int:
            # Adding to the total size of the folder
            top_directory_size['/'] += current_item_size
        elif type(current_item_size) == dict:
            # Essentially doing the same thing as above but for a second layer
            lower_directory_size = {item: 0}
            for i in current_item_size.values():
                if type(i) == int:
                    lower_directory_size[item] += i
                elif type(i) == dict:
                    Folder_Storage.append(i)

            Folder_Storage.append(lower_directory_size)
    Folder_Storage.append(top_directory_size)
    # Returns a list with key value pairs of folders and the size of the folder
    return Folder_Storage
            # Getting the drive that we are currently working with
# %%
x = filesize_calculator(file_system)
print(x)
# For loop that iterates through the output and finds the files under a size of 100000
for item in x:
    for key in item:
        folder_size = item.get(key)
        if folder_size > 100000:
            pass
        else:
            print(f'The {key} folder needs to be deleted as its size, {folder_size} is under 100000')
# %%
