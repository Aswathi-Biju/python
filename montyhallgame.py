import random
def monty_hall_single_game():
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    player_choice = int(input("Choose a door (1, 2, or 3): ")) - 1
    available_doors = [i for i in range(3) if i != player_choice and doors[i] != 'car']
    host_opens = random.choice(available_doors)
    print(f"The host opens door {host_opens + 1}, revealing a goat.")
    switch = input("Do you want to switch your choice? (yes/no): ").strip().lower() == 'yes'
    if switch:
        player_choice = next(i for i in range(3) if i != player_choice and i != host_opens)
    if doors[player_choice] == 'car':
        print("Congratulations! You won the car!")
    else:
        print("Sorry, you got a goat.")
    print(f"The car was behind door {doors.index('car') + 1}.")
print("Welcome to the Monty Hall Game!")
monty_hall_single_game()
