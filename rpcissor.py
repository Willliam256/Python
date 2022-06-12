import random 

#Rock vs paper->paper wins
#Rock vs scissor->Rock wins
#paper vs scissor->scissor wins

# possible choices
selections = ("Rock", "Paper", "Scissor")
user_choice = input("Enter Your Choice: ")
computer_choice = random.choice(selections)

#if the game is a Tie
if user_choice == computer_choice:
    print(f"\nYou Show >>> {computer_choice}")
    print(f"Computer Shows >>> {computer_choice}")
    print("-----------------------\n")
    print("*** Its a Tie ***\n")
    print(f"You all Show ->>  {computer_choice}")

elif user_choice == "Rock":
    if computer_choice == "Scissor":
        print(f"\nYou Show >>> {user_choice}")
        print(f"Computer Shows >>> {computer_choice}")
        print("-----------------------\n")
        print(f"{user_choice} crushes {computer_choice}\n")
        print("*** You Win!!!! ***\n")
    else:
        print(f"You Show >>> {user_choice}")
        print(f"Computer Shows >>> {computer_choice}")
        print("-----------------------\n")
        print(f"{computer_choice} Covers {user_choice}\n")
        print("*** You Lose!!!!***\n")    


elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"\nYou Show >>> {user_choice}")
            print(f"Computer Shows >>> {computer_choice}")
            print("-----------------------\n")
            print(f"{user_choice} Covers {computer_choice}\n")
            print("*** You Win!!!! ***\n")
        else:
            print(f"You Show >>> {user_choice}")
            print(f"Computer Shows >>> {computer_choice}")
            print("-----------------------\n")
            print(f"{computer_choice} Cuts {user_choice}\n")
            print("*** You Lose!!!!***\n")    
    
elif user_choice == "Scissor":
    if computer_choice == "Paper":
            print(f"\nYou Show >>> {user_choice}")
            print(f"Computer Shows >>> {computer_choice}")
            print("-----------------------\n")
            print(f"{user_choice} Cuts {computer_choice}\n")
            print("*** You Win!!!! ***\n")
    else:
        print(f"You Show >>> {user_choice}")
        print(f"Computer Shows >>> {computer_choice}")
        print("-----------------------\n")
        print(f"{computer_choice} Crushes {user_choice}\n")
        print("*** You Lose!!!!***\n")

else:{
    print("Invalid Entry")
}