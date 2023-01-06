
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
Win = 6
Loss = 0
Draw = 3

Rock = 1
Paper = 2
Scissors = 3

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
            print('Rock beats scissors! player 1 wins!')
            return [6, 0, choice_points1, choice_points2]
        elif Player2 == 'rock':
            choice_points2 = 1
            print('It is a draw!')
            return [3, 3, choice_points1, choice_points2]
        elif Player2 == 'paper':
            choice_points2 = 2 
            print('Paper beats rock! Player 2 Wins!')
            return [0, 6, choice_points1, choice_points2]
    elif Player1 == 'scissors':
        choice_points1 = 3
        if Player2 == 'scissors':
            choice_points2 = 3
            print('It is a draw!')
            return [3, 3, choice_points1, choice_points2]
        elif Player2 == 'rock':
            choice_points2 = 1
            print('Rock beats scissors! PLayer 2 wins!')
            return [0, 6, choice_points1, choice_points2]
        elif Player2 == 'paper':
            choice_points2 = 2 
            print('Scissors beats paper! Player 1 wins!')
            return [6, 0, choice_points1, choice_points2]
    elif Player1 == 'paper':
        choice_points1 = 2 
        if Player2 == 'scissors':
            choice_points2 = 3
            print('Scissors beats paper! Player 2 wins!')
            return [0, 6, choice_points1, choice_points2]
        elif Player2 == 'rock':
            choice_points2 = 1
            print('Paper beats rock! Player 1 wins!')
            return [6, 0, choice_points1, choice_points2]
        elif Player2 == 'paper':
            choice_points2 = 2 
            print('It is a draw!')
            return [3, 3, choice_points1, choice_points2]
# Creating variables for the outcome of the three rounds.
round1 = RockPaperScissors('paper', 'rock')
round2 = RockPaperScissors('rock', 'paper')
round3 = RockPaperScissors('scissors', 'scissors')

#Calculating the final score for both
results = [round1, round2, round3]
Player1_Score = 0
Player2_Score = 0
for i in results:
    Player1_Score = Player1_Score+i[0]+i[2]
    Player2_Score = Player2_Score+i[1]+i[3]
print(f'Player 1 Total Score: {Player1_Score}\nPlayer 2 Total Score: {Player2_Score}')
#In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

#What would your total score be if everything goes exactly according to your strategy guide?