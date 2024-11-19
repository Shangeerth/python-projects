def start_game():
    print("Welcome to the Adventure Game!")
    print("You will be presented with scenarios where you can choose 'yes' or 'no'.")
    first_choice()

def first_choice():
    print("\nYou find yourself at a fork in the road.")
    choice = input("Do you want to go left or right? (left/right): ").strip().lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        first_choice()

def left_path():
    print("\nYou encounter a friendly dragon!")
    choice = input("Do you want to talk to the dragon? (yes/no): ").strip().lower()
    
    if choice == "yes":
        print("The dragon shares its treasure with you. You win!")
    elif choice == "no":
        print("The dragon gets sad and flies away. You lose!")
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        left_path()

def right_path():
    print("\nYou stumble upon a dark cave.")
    choice = input("Do you want to enter the cave? (yes/no): ").strip().lower()
    
    if choice == "yes":
        print("Inside, you find a hidden treasure chest! You win!")
    elif choice == "no":
        print("You decide to leave, but a wild beast appears! You lose!")
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        right_path()

# Start the game
start_game() 
def start_game(): 
    print("Welcome to the Adventure Game!")
    print("You will be presented with scenarios where you can choose 'yes' or 'no'.")
    first_choice()

def first_choice():
    print("\nYou find yourself at a fork in the road.")
    choice = input("Do you want to go left or right? (left/right): ").strip().lower()
    
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        first_choice()

def left_path():
    print("\nYou encounter a friendly dragon!")
    choice = input("Do you want to talk to the dragon? (yes/no): ").strip().lower()
    
    if choice == "yes":
        print("The dragon shares its treasure with you. You win!")
    elif choice == "no":
        print("The dragon gets sad and flies away. You lose!")
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        left_path()

def right_path():
    print("\nYou stumble upon a dark cave.")
    choice = input("Do you want to enter the cave? (yes/no): ").strip().lower()
    
    if choice == "yes":
        print("Inside, you find a hidden treasure chest! You win!")
    elif choice == "no":
        print("You decide to leave, but a wild beast appears! You lose!")
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        right_path()

# Start the game
start_game()