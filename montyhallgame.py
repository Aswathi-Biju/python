import random
def monty_hall_game():
    print("Welcome to the Monty Hall Game!")
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    player_choice = -1
    while player_choice not in range(3):
        player_input = input("Choose a door (1, 2, or 3): ")
        if player_input.isdigit():
            player_choice = int(player_input) - 1
            if player_choice not in range(3):
                print("Invalid choice. Please choose a door numbered 1, 2, or 3.")
        else:
            print("Invalid input. Please enter a number (1, 2, or 3).")
    available_doors = [i for i in range(3) if i != player_choice and doors[i] != 'car']
    host_opens = random.choice(available_doors)
    print(f"The host opens door {host_opens + 1}, revealing a goat.")
    switch = input("Do you want to switch your choice? (yes/no): ").strip().lower() == 'yes'
    if switch:
        new_choice = -1
        while new_choice not in range(3) or new_choice == host_opens or new_choice == player_choice:
            print(f"Your current choice is door {player_choice + 1}.")
            new_input = input(f"Choose a new door (1, 2, or 3), excluding door {host_opens + 1}: ")
            if new_input.isdigit():
                new_choice = int(new_input) - 1
                if new_choice not in range(3) or new_choice == host_opens or new_choice == player_choice:
                    print(f"Invalid choice. Choose a door other than {host_opens + 1} and your current choice.")
            else:
                print("Invalid input. Please enter a number (1, 2, or 3).")
        player_choice = new_choice
    if doors[player_choice] == 'car':
        print("Congratulations! You won the car!")
    else:
        print("Sorry, you got a goat.")
    print(f"The car was behind door {doors.index('car') + 1}.")
monty_hall_game()
