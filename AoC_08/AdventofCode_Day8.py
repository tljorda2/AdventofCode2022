# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:05:25 2023

@author: cacru
"""
#%%
# Here I am going to make it into a numpy matrix
# The matrix made here is the example matrix. this was only used to test the script
import numpy as np
Tree_Heights_List = [3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]
Tree_Heights_Matrix = np.matrix(Tree_Heights_List)
print(Tree_Heights_Matrix)
#%%
# Reading the text file with the input data and creating a matrix from it that can be entered into
# The function
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\\AoC_08\\AoCDay8_Data.txt') as file:
    AoCDay8_Data = file.readlines()
file.close()

# Iterating through the lines read from the file
# Each line is initially created as a single string within a list
# Need to split each number in each string into an individual number
# That is apart of a new list that was the string
Tree_Heights_List = []
for line in AoCDay8_Data:
    line_formatted = []
    # Iterating through each letter
    for num in line:
        #using try since the data contains '\n'
        # This will convert each character into the integer type and append it to a temporary list
        try:
            # Temporary variable to store the number
            temp_x = int(num)
            line_formatted.append(temp_x)
        except:
            # Will delete the special character
            del num
    print(len(line_formatted))
    print(line_formatted)
    # Append the temporary list to our overall list that contains all the lines
    Tree_Heights_List.append(line_formatted)
Tree_Heights_Matrix = np.matrix(Tree_Heights_List)
print(Tree_Heights_Matrix)
#%%
# Creating a function that will take a subarray from a numpy matrix and check if a number is outright the largest number
def CheckRow2(number, matrix_row):
    # np.nditer iterates through each item of an array
    for i in np.nditer(matrix_row):
        # If there is any number that is equal to or greater than the input number, it returns false
        if i >= number:
            return False
        # Passing to the next iteration of the for loop
        else:
            pass
    # If it runs through each number where all of them are less than the inputed number, it returns True
    # This means that the number is the outright max in the subarray given
    return True


#%%
# Creating a function that will take in any matrix and return the count of all visible trees

def TreeCheck(matrix):
    # Getting the shape or "Dimensions" of the matrix inputted
    # This will be used to ignore the values that are on the edge of the matrix and later assign a value of 1 to them
    map_dim = np.shape(matrix)
    map_dim = list(map_dim)
    # Creating an empty matrix that is the same exact size as the one inputted
    # This will be what is changed to refelect the map of visible trees
    return_matrix = np.zeros([map_dim[0], map_dim[1]])
    # First for loop to get the row
    for i in range(map_dim[0]):
        # Second for loop to get the column
        for j in range(map_dim[1]):
            # Getting the current number based on the row and column
            current_tree = matrix[i,j]
            # This if-statement is written to ignore the edge values for now
            if i == 0 or j == 0 or i == (map_dim[0]-1) or j == (map_dim[1]-1):
                pass
            else:
                # This will get the arrays for each cardinal direction from the current tree while not including it
                Upper_Column = matrix[:i,j]
                # In order to exclude the current tree, we have to add one to the index in some situations
                Lower_Column = matrix[i+1:,j]
                Right_Column = matrix[i,j+1:]
                Left_Column = matrix[i,:j]
                # Calling the first function to see if the tree is visible
                # Using "or" since it only needs to be visible in one direction
                # Checks if any of the functions return True
                if (CheckRow2(current_tree, Upper_Column) or
                    CheckRow2(current_tree, Lower_Column) or
                    CheckRow2(current_tree, Right_Column) or
                    CheckRow2(current_tree, Left_Column)):
                    # This will set the position of the current tree to one in the empty matrix
                    return_matrix[i,j] = True
                else:
                    # If none of them return true, this will set the position of the current tree to 0 in the empty matrix.
                    return_matrix[i,j] = False
    # Setting the value of all the edges to 1, since they are all visible
    return_matrix[:,0] = 1
    return_matrix[0,:] = 1
    # We have the subtract one from the dimension since indexing starts with 0
    return_matrix[:,map_dim[0]-1] = 1
    return_matrix[map_dim[1]-1,:] = 1
    # Add all the values from the new matrix, where 1 is a visible tree and 0 is not
    # This will return the total amount of visible trees, which is what is needed
    summed_total = np.sum(return_matrix)
    return summed_total
# Printing the amount of visible trees from the given data
print(TreeCheck(Tree_Heights_Matrix))
# The answer for my data should be 1560
# %%
# Part two wants the scenic value of each pf the trees
# This is measured by the number of visible trees in each direction multiplied together
def ScenicScore(number, matrix_row):
    for i in np.nditer(matrix_row):
        