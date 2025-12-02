def readboard(filename):
    # Open the file and read all lines without newline characters
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        board = [list(row) for row in lines]  # Convert each string to a list
    return board
def start_game():
    print("Starting the game...")
    # Placeholder for game logic
    print("Game is running... (Press Enter to return to menu)")
    input()

def show_instructions():
    print("Instructions:")
    print("1. Place cordinates for ships.")
    print("2. Get all ships.")
    print("3. Press 'q' to quit the game.")
    input("Press Enter to return to menu...")

def show_credits():
    print("Game Credits:")
    print("Developed by: Your Name")
    print("Thanks for playing!")
    input("Press Enter to return to menu...")

def menu():
    while True:
        print("=== MAIN MENU ===")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Credits")
        print("4. Exit")
        return input("Enter your choice (1-4): ").strip()

        if choice == '1':
            start_game()
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            show_credits()
        elif choice == '4':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

        

   
