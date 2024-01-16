from random import randint      # Use to generate computer choice

introduction = '''
<<<<<<<<<<<<<{| Snake - Water - Gun |}>>>>>>>>>>>>
                {Game-Based Project}

What is this ?
	Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. 
How it works ?
	The gun beats the snake, the water beats the gun, and the snake beats the water

'''
print(introduction)



# >> GAME WILL START WHEN CALLING THIS WITH ITS PARAMETERS
# Game mode selecton --> it calls game mode inside itself   
def game_mode_selection(single_player_mode , multiplayer_mode):
    # game mode : Single-player | Multiplayer 
    while True:   # Run until get required values
        # Take input from user choice that which game mode He/She want to play
        game_mode_input = input("Enter which game mode you want to play\n 1 for Single-player(first user, second computer) \n 2 for Multiplayer(both user) \nEnter here : ")
        print("\n")     # blank line for better interface
        
        # Call and return single_player_mode
        if game_mode_input == "1":    
            return single_player_mode()
        
        # Call and return multiplayer_mode
        elif game_mode_input == "2" :     
            return multiplayer_mode()
        
        # For unexpected input 
        else :
            print("\n", "( Wrong Input ! )".center(50, "~"), "\nPlease enter a valid input to select game mode")
            # because of while True it will ask again for value



# Game round selecton : Finite(input from user) OR Infinty(a big value)
def game_round_selection():
    # round mode : Finite(input from user{odd number only}) | Infinty(return a big value 10**99)
    # Take input from user choice that which round mode He/She want to play
    finite_or_infinity = input("Enter 1 for finite round or 2 for infinite rounds : ")
    
    # For finite rounds --> take rounds number that (>= 3 and odd only)
    if (finite_or_infinity == "1"):
        while True:     # Run until get required values
            # Take round number input
            no_of_rounds = input("Enter how many rounds you want to play(minimum round is 3) and rounds number must be odd(e.g: 3,5,7,11...)\nEnter rounds number here : ")

            # Check that input(str) contain number only 
            if (no_of_rounds.isdigit() == True):
                # if number only turn str into int (for int operation to check required value)
                no_of_rounds = int(no_of_rounds)    # Turn input(str) into int
                
                # (Adviced by Sir.Zain Javed)
                # Check that minimun number is 3 and only odd 
                if (no_of_rounds >= 3 and no_of_rounds % 2 != 0):
                    return no_of_rounds 
            
            # If input(str) not contain only int 
            else:
                print("\n","( Wrong Input ! )".center(50, "~"),"\nEnter a valid number that greater than or equal to 3 and must be odd(e.g: 3,5,7,11...)")
                # because of while True it will ask again for value

    # For Infinity rounds     
    elif (finite_or_infinity == "2"):
        # Return a big value as infinite rounds
        return 10**99   
    
    # For unexpected input
    else:
        print("\n")     # blank line for better interface
        print("( Wrong Input ! )".center(50, "~") , "\nSelect game round mode by enter 1 and 2 only")
        # Recursion (for asking values again)
        game_round_selection()      




# Game logic that checks the players choices and then return 0 if Draw, 1 for player 1 wins, 2 for player 2 wins
def game_logic(player1_name, player1_ans, player2_name, player2_ans):
    # Both are same --> Draw
    if player1_ans == player2_ans:
        print("\nBoth has same choice \n  So, the game is --> Draw")
        return 0
    
    # Snake - Water --> Snake wins(player 1)
    elif player1_ans == 1 and player2_ans == 2:
        print(f"\nSnake drinks the water \n  {player1_name} Win")
        # return 1
    
    # Snake - Gun --> Gun wins(player 2)
    elif player1_ans == 1 and player2_ans == 3:
        print(f"\nGun kills the snake \n  {player2_name} win")
        return 2
    
    # Water - Snake --> Snake wins(player 2)
    elif player1_ans == 2 and player2_ans == 1:
        print(f"\nSnake drinks the water \n  {player2_name} win")
        return 2
    
    # Water - Gun -->  Water wins(player 1)
    elif player1_ans == 2 and player2_ans == 3:
        print(f"\nWater drowns the gun \n  {player1_name} Win")
        return 1
    
    # Gun - Snake --> Gun wins(player 1)
    elif player1_ans == 3 and player2_ans == 1:
        print(f"\nGun kills the snake \n  {player1_name} Win")
        return 1
    
    # Gun - Water --> Water wins(player 2)
    elif player1_ans == 3 and player2_ans == 2:
        print(f"\nWater drowns the gun \n  {player2_name} Win")
        return 2



# For prevent errors
# Players choices take and check that player input are valid or not 
# also take game mode because different of different players in each mode 
def players_choice_take_and_check(player1_name, player2_name, game_mode):
    # This returns answers in tuple form, break returned values by indexing, Call this function in variable, [0] for player 1 and [1] for player 2(OR for computer if single-player)

    # Single player code
    if (game_mode == "single_player_mode"):
        # For single-player(player1)
        while True:
            single_player_ans = input(f"\n{player1_name} enter your choice: \n  1 for Snake \n  2 for Water \n  3 for Gun \nEnter Here you Choice : ")
            
            # These our needed answers
            if (single_player_ans == "1") or (single_player_ans == "2") or (single_player_ans == "3"):
                break   # Then break while True(loop)
            
            # When needs not satisfied
            else:
                print("\n","( Wrong Input ! )".center(50, "~"),"\nChoose between 1 to 3")
                # because of while True it will ask again for value
                
        # For Computer(no need to check because it is get by random function randint())
        computer_ans = randint(1, 3)

        # When get single-player(player 1) and computer ansewer(randomnumber 1 to 3) --> return their answers
        # Converting answers into int because they are initialize as str to handle type casting error(data that not change its data type such as True into int)
        return int(single_player_ans) , int(computer_ans)
    
    # Multiplayer code 
    elif (game_mode == "multiplayer_mode"):
        # For player 1
        while True:
            player1_ans = input(f"\n{player1_name} enter your choice: \n  1 for Snake \n  2 for Water \n  3 for Gun \nEnter Here you Choice : ")
            
            # These our needed answers
            if (player1_ans == "1") or (player1_ans == "2") or (player1_ans == "3"):
                break   # Then break while True(loop)
            
            # When needs not satisfied
            else:
                print("\n","( Wrong Input ! )".center(50, "~"),"\nChoose between 1 to 3")
                # because of while True it will ask again for value

        # 50 new lines to hide other's choice
        for i in range(50):
            print("    new lines for hiding other choice   ")
        
        # For player 2
        while True:
            player2_ans = input(f"\n{player2_name} enter your choice: \n  1 for Snake \n  2 for Water \n  3 for Gun \nEnter Here you Choice : ")
            
            # These our needed answers
            if (player2_ans == "1") or (player2_ans == "2") or (player2_ans == "3"):
                break   # Then break while True(loop)
            
            # When needs not satisfied
            else:
                print("\n","( Wrong Input ! )".center(50, "~"),"\nChoose between 1 to 3") 
                # because of while True it will ask again for value

        # When get both player answers --> return their anaswers
        # Converting answers into int because they are initialize as str to handle type casting error(data that not change its data type such as True into int)
        return int(player1_ans)  , int(player2_ans)
    


# Single player mode 
def single_player_mode():
    single_player_points_lst = []   # Single-player answer list
    computer_points_lst = []    # Computer answer list

    # Call game_round_selection() for asking for round mode(explained in game_round_selection() function)
    round_number = game_round_selection()
    
    # Take name of single-player for better expereince 
    single_player_name = input("\nEnter Your/Player name : ")

    # Run loop every time according to roun_number
    for i in range(round_number):
        # Show round number for better expereince
        print(f"{{ ROUND {i+1} }}".center(50, "-"))

        # Call players_choice_take_and_check that take and check answer to prevent error and then return answers
        players_answers = players_choice_take_and_check(single_player_name, "Computer", "single_player_mode")
       
        # Returned values are packed as tuple , we break it
        single_player_ans = players_answers[0]      # single-player(player 1)
        computer_ans = players_answers[1]       # computer(by random's randint function)

        # Show player's answers
        print(f"\n{single_player_name} choice is : {single_player_ans}")
        print(f"\nComputer choice is : {computer_ans}")

        # Call game_logic() to check who wins, it return int according to result
        result = game_logic(single_player_name, single_player_ans, "Computer", computer_ans)
        # 0 for Draw but we not add 0 in list because its equal to add or not
        # 1 if player 1 win (single-player)
        if (result == 1):
          single_player_points_lst.append(1)
        # 2 if player 2 wins (computer)
        elif (result == 2):
          computer_points_lst.append(1)
        
        # At the end of each round
        # Ask that player want to play more or quit
        stay_or_leave = input("Press 'ENTER' to continue game OR enter Q for quit game : ")
        # if Q, so break the loop and show the results
        if stay_or_leave.upper() == "Q":
          break
        # Don't need to use more condition becasue second condition are enter only to run loop again 

    # When rounds are compelete or quit game --> show final results
    return Results(single_player_name, single_player_points_lst, "Computer", computer_points_lst)



# Multiplayer mode
def multiplayer_mode():
    player1_points_lst = []     # player1 answers list
    player2_points_lst = []     # player2 answers list
    
    # Call game_round_selection() for asking for round mode(explained in game_round_selection() function)
    round_number = game_round_selection()

    # Take names of players for better expereince
    player1_name = input("\nEnter First Player name : ")
    player2_name = input("\nEnter Second Player name : ")
    
    # Run loop every time according to roun_number
    for i in range(round_number):
        # Show round number for better expereince
        print(f"{{ ROUND {i+1} }}".center(50, "-"))
        
        # Call players_choice_take_and_check that take and check answer to prevent error and then return answers
        players_answers = players_choice_take_and_check(player1_name , player2_name, "multiplayer_mode")
        # Returned values are packed as tuple , we break it
        player1_ans = players_answers[0]
        player2_ans = players_answers[1]
        
        # Show player's answers
        print(f"\n{player2_name} choice is : {player2_ans}")
        print(f"{player1_name} choice is : {player1_ans}")
        
        # Call game_logic() to check who wins, it return int according to result
        result = game_logic(player2_name, player1_ans, player2_name, player2_ans)
        # 0 for Draw but we not add 0 in list because its equal to add or not
        # 1 if player 1 win (single-player)        
        if (result == 1):
          player1_points_lst.append(1)
        # 2 if player 2 wins (computer)
        elif (result == 2):
          player2_points_lst.append(1)
        
        # At the end of each round
        # Ask that player want to play more or quit
        stay_or_leave = input("Press 'ENTER' to continue game OR enter Q for quit game : ")
        # if Q, so break the loop and show the results
        if stay_or_leave.upper() == "Q":
          break
        # Don't need to use more condition becasue second condition are enter only to run loop again

    # When rounds are compelete or quit game --> show final results
    return Results(player1_name, player1_points_lst, player2_name, player2_points_lst)



# Results according to gameplay --> Call when all round compelete OR quit game
def Results(player1_name, player1_points_lst, player2_name, player2_points_lst):
    # Total of player's point list 
    player1_total_points = sum(player1_points_lst)
    player2_total_points = sum(player2_points_lst)

    # Player 1 wins
    if (player1_total_points > player2_total_points):
        print("\n")     # blank line for better interface
        print(f" {player1_name} Wins the Game! ".center(50, "|"))
    
    # Player 2 wins
    elif (player2_total_points > player1_total_points):
        print("\n")     # blank line for better interface
        print(f" {player2_name} Wins the Game! ".center(50, "|"))
    
    # Draw
    else:
        print("\n")     # blank line for better interface
        print("{ Both play well, Draw }".center(50, ":"))



# GAME IS STARTED BY CALLING THIS FUNCTION >> ENJOY GAME =) :) !
game_mode_selection(single_player_mode , multiplayer_mode )


# END - Credits 
credits = '''\n
<<<< SAAD-ULLAH KHAN >>>>  
      He is developer of this program =)  
    I hope you like this game/program so much :)
    Thank You for using!
'''
print(credits)

        