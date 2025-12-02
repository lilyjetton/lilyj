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
    
    
def printboard(board):
    # Print each row with spaces between numbers
    for rows in board:
        print(" ".join(str(num) for num in rows))

def playermakemove(board):
    print("enter point(x,y)")
    x = int(input("x "))
    y = int(input("y "))
    if board[x][y] == "1": # checking if its a hit
        board[x][y] = "+"
    if board[x][y] == "0": # checking if theres a miss 
        board[x][y] = "x"

def main():
    keepRunning = True

    while keepRunning:
        choice = menu()

        if choice == "1":
            playerBoard = readboard("battleship.txt")
            print("\n--- GAME START ---")
            printboard(playerBoard)

            # Game loop
            while True:
                playermakemove(playerBoard) # shows updated board each turn

        elif choice == "2":
            print("Instructions")
            keepRunning = False

        else:
            print("Invalid choice. Try again.")

    # Read the game board from the text file
    playerBoard = readboard("battleship.txt")
# board = [ [0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0] ]
#board[1][2] = 1
    # Print the board
    keepRunning = True
    while(keepRunning == True):
        printboard(playerBoard)
        playermakemove(playerBoard)
    

if __name__ == "__main__":
        main()

        

   
