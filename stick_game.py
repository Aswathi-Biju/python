"""
Date: 06/12/2024
Author by: Aswathi Biju
Description: Write a program to play a sticks game in which there are 16 sticks.
Two players take turns to play the game. Each player picks one set of sticks
(needn’t be adjacent) during his turn.
A set contains 1, 2, or 3 sticks.
The player who takes the last stick is the loser.
The number of sticks in the set is to be input.
"""
def stickgame():
    print("!!! Welcome to the Stick Game !!!")
    print(
        "RULES:\n There are two players take turns to play the game.\n Player needs to pick either 1 or 2 or 3 sticks (needn’t be adjacent).\n 16 sticks are on the table. \n A player can chose one at a time. \n The player who takes the last stick is the loser. ")
    confirm = input("Are you ready? (yes/no): ")
    player1 = input("Enter player1's name: ")
    player2 = input("Enter player2's name: ")
    count_of_sticks = 16
    player = player1 or player2
    while count_of_sticks != 0:
        if count_of_sticks > 0:
            choice = int(input(f"{player1},enter the no. of sticks:"))
            count_of_sticks = count_of_sticks - choice
            print(f"Remaining sticks are {count_of_sticks}")
            player = player1

        if count_of_sticks > 0:
            choice = int(input(f"{player2},enter the no. of sticks:"))
            count_of_sticks = count_of_sticks - choice
            print(f"Remaining sticks are {count_of_sticks}")
            player = player2
    if count_of_sticks == 0:
        print(f"{player}, LOOSE")
stickgame()
