#%%
# Online Python - IDE, Editor, Compiler, Interpreter
#Since you can't be sure if the Elf is trying to help you or trick you,
#you should calculate the score you would get if you were to follow the strategy guide.

#For example, suppose you were given the following strategy guide:

#A Y
#B X
#C Z
#This strategy guide predicts and recommends the following:

#In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
#This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#In the second round, your opponent will choose Paper (B), and you should choose Rock (X).
#This ends in a loss for you with a score of 1 (1 + 0).
#The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
X = 'rock'
Y = 'paper'
Z = 'scissors'
A = 'rock'
B = 'scissors'
C = 'paper'
# Create a function that can be iterated through repeatetly
def RockPaperScissors(Player1, Player2):
    possible_choices = ['rock', 'paper', 'scissors']
    # Seeing if I can make the input all lowercase to match the possible choices.
    try:
        Player1.lower()
    except:
        pass
    try:
        Player2.lower()
    except:
        pass
    
    # Checking if the possible choices are in the list
    if Player1 in possible_choices:
        pass
    else:
        raise ValueError(f'Please select one of the following:\n{possible_choices}')
    if Player2 in possible_choices:
        pass
    else:
        raise ValueError(f'Please select one of the following:\n{possible_choices}')
    
    # If statements for determining the outcome of the game
    if Player1 == 'rock':
        choice_points1 = 1
        if Player2 == 'scissors':
            choice_points2 = 3
            return [6, 0, choice_points1, choice_points2]
        elif Player2 == 'rock':
            choice_points2 = 1
            return [3, 3, choice_points1, choice_points2]
        elif Player2 == 'paper':
            choice_points2 = 2 
            return [0, 6, choice_points1, choice_points2]
    elif Player1 == 'scissors':
        choice_points1 = 3
        if Player2 == 'scissors':
            choice_points2 = 3
            return [3, 3, choice_points1, choice_points2]
        elif Player2 == 'rock':
            choice_points2 = 1
            return [0, 6, choice_points1, choice_points2]
        elif Player2 == 'paper':
            choice_points2 = 2 
            return [6, 0, choice_points1, choice_points2]
    elif Player1 == 'paper':
        choice_points1 = 2 
        if Player2 == 'scissors':
            choice_points2 = 3
            return [0, 6, choice_points1, choice_points2]
        elif Player2 == 'rock':
            choice_points2 = 1
            return [6, 0, choice_points1, choice_points2]
        elif Player2 == 'paper':
            choice_points2 = 2 
            return [3, 3, choice_points1, choice_points2]
# Creating variables for the outcome of the three rounds.
#%%
# Getting the total results
# Getting the data from the text file
with open('C:\\Users\\Timothy Jordan\\Desktop\\Pandas Practice\\Advent of Code\\AoC_02\\AoCDay2_Data.txt') as file:
    Day2_Data = file.readlines()
results = []
# for loop that takes the input data, converts it into a usable input for the function, and stores each of the results in a list

for line in Day2_Data:
    Player1 = line[0]
    Player2 = line[2]
    if Player1 == 'A':
        Player1 = 'rock'
    elif Player1 == 'B':
        Player1 = 'paper'
    elif Player1 == 'C':
        Player1 = 'scissors'
    if Player2 == 'X':
        Player2 = 'rock'
    elif Player2 == 'Y':
        Player2 = 'paper'
    elif Player2 == 'Z':
        Player2 = 'scissors'
    round = RockPaperScissors(Player1, Player2)
    results.append(round)
#%%
#Calculating the final score for both
Player1_Score = 0
Player2_Score = 0
for i in results:
    Player1_Score = Player1_Score+i[0]+i[2]
    Player2_Score = Player2_Score+i[1]+i[3]
print(f'Player 1 Total Score: {Player1_Score}\nPlayer 2 Total Score: {Player2_Score}\nTotal Score: {Player1_Score+Player2_Score}')
#In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

#What would your total score be if everything goes exactly according to your strategy guide?
# %%
# Part 2
# The second column is no longer your input, but what the outcome of the game should be
# If you chose X, it means you lost, if you chose Y, it means you need to tie and if you chose Z, it means you won
# Mapping the outcomes
# Honestly probably could have done this instead of the way i did the ifelse statements for above
# I might change it later
outcomes = {'A':{'X': 'scissors', 'Y': 'rock', 'Z': 'paper'},
            'B':{'X': 'rock', 'Y': 'paper', 'Z': 'scissors'},
            'C':{'X': 'paper', 'Y': 'scissors', 'Z': 'rock'}}

results = []
# for loop that takes the input data, converts it into a usable input for the function, and stores each of the results in a list
# This for loop will map each of the outcomes to the correct choice for player 2
for line in Day2_Data:
    Player1 = line[0]
    Player2_Outcome = line[2]
    if Player1 == 'A':
        Player1 = 'rock'
        Player2 = outcomes['A'][Player2_Outcome]
    elif Player1 == 'B':
        Player1 = 'paper'
        Player2 = outcomes['B'][Player2_Outcome]
    elif Player1 == 'C':
        Player1 = 'scissors'
        Player2 = outcomes['C'][Player2_Outcome]
    round = RockPaperScissors(Player1, Player2)
    results.append(round)

#Calculating the final score for both
Player1_Score = 0
Player2_Score = 0
for i in results:
    Player1_Score = Player1_Score+i[0]+i[2]
    Player2_Score = Player2_Score+i[1]+i[3]
print(f'Player 1 Total Score: {Player1_Score}\nPlayer 2 Total Score: {Player2_Score}\nTotal Score: {Player1_Score+Player2_Score}')
# %%
