import random

choice_list = ["R", "P", "S"]

choice_name = {"R" : "Rock", "P" : "Paper", "S" : "Scissors"}
               
#   PRS
winning_choice = {"PR" : {"P" : "won", "R" : "losed"}, 
"RS" : {"R" : "won", "S" : "losed"},
"PS" : {"P" : "losed", "S" : "won"}}
compare_choice = {}

while True:
    player_choice = input("Enter your choice [R or P or S]: ").upper()

    if player_choice not in choice_list:
        print("Invalid choice, try again!")
    
    else:
        computer_choice = random.choice(choice_list)

        if player_choice == computer_choice:
    
            print(f"\nPlayer ({choice_name[player_choice]}) : CPU ({choice_name[computer_choice]})\n")
            print("It's a Tie - Try again\n")

        else:
            print(f"Player ({choice_name[player_choice]}) : CPU ({choice_name[computer_choice]})")

            merge_choice = "".join(sorted(player_choice + computer_choice))

            compare_choice = winning_choice[merge_choice]

            print(f"Computer {compare_choice[computer_choice]}, Player {compare_choice[player_choice]}")

            break
