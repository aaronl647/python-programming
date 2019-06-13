import random
'''
def play_pig():
    player1_score, player2_score = 0,0
    turn = random.randint(0,1)
    #while either player has not reached a score of 10
    while (True):
        #if its player 1s turn roll or hold
        if turn == 0:
            choice = input("[PLAYER 1] Roll of hold: ")
            if choice == 'r':
                round_score = random.randint(1,6)
                if round_score == 1: #player loses turn and score gets set to 0
                    player1_score = 0
                    turn = 1
                else:
                    player1_score += round_score
                print(f"Round score: {round_score}, Total score: {player1_score}")
            else:
                turn = 1
        
        if turn == 1:
            choice = input("[PLAYER 2] Roll of hold: ")
            if choice == 'r':
                round_score = random.randint(1,6)
                if round_score == 1: #player loses turn and score gets set to 0
                    player2_score = 0
                    turn = 0
                else:
                    player2_score += round_score
                print(f"Round score: {round_score}, Total score: {player2_score}")
            else: 
                turn = 0

        if player1_score >= 10 or player2_score >= 10:
            break
    
    if player1_score >=10:
        print("PLAYER 1 WINS!!!")
    
    else:
        print("PLAYER 2 WINS!!!")

    #check if a player has won
play_pig()
'''
#####################################################################################
#refactor, user functions

player_scores = [0,0]
turn_var = [random.randint(0,1)]

def roll(turn):
        choice = input(f"[PLAYER {turn_var} ] Roll of hold:")
        if choice == 'r':
            round_score = random.randint(1,6)
            if round_score == 1: #player loses turn and score gets set to 0
                player_scores[turn] = 0
                if turn_var == 1:
                    turn = 0
                else: 
                    turn = 1
            else:
                player_scores[turn] += round_score
            print(f"Round score: {round_score}, Total score: {player_scores[turn]}")
        else:
            if turn_var == 0:
                turn = 1 
            else:
                 turn = 0



while(True):
    roll(turn_var)
    if player_scores[0]>= 20 or player_scores[1] >=20:
        break
    if player_scores[0] >=10:
        print("PLAYER 1 WINS!!!")
    else:
        print("PLAYER 2 WINS!!!")

''' 
#Two player game
def player_turn():
    
    return 

#create a random generated dice
def dice():
    import random
    val = random.randint(1,6)
    return val

#input 'r' to roll the dice
#if the dice lands on 1, player loses their turn and loses all their points 
#Each time the player gets any other number, the points add up
#h to hold your turn and passes the turn onto the second player
#first player to 21 first wins
current_score1 = 0
current_score2 = 0
total_score1 = 0
total_score2 = 0
player1 = input("Enter Player 1s name: ")
player2 = input("Enter Player 2s name: ")
roll = ''
turn = [0,1]


while total_score1 < 10: or total_score2 < 10:
        if dice() == 1:
            turn == 1
            total_score1 = 0
            print("Sorry, you lost your turn and your points. Player 2 starts.")
        if roll == 'h':
            turn == 1
            print("Player 2's turn.")
        if roll == 'r':
            print(dice())
        if dice() != 1:
            current_score1 = current_score1 + dice()
            total_score1 = current_score1
            print(input("Do you want to continue?" ))
    ######################################################
    print()
    print(input("Hit 'r' to roll the dice, 'h'to hold your turn. ")
        if dice() != 1:
            total_score1 = current_score1 + dice()
            print("You rolled a",total_score1)
            print("What would you like to do next? 'r' or 'h' ")
    if dice == 1:
'''
        