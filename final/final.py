def readboard(filename):
    # Open the file and read all lines without newline characters
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    board = [list(row) for row in lines]  # Convert each string to a list
    return board
def menu():
    print("\n--- MENU ---")
    print("1. View Board")
    print("2. Make a Move")
    print("3. Quit")
    choice = input("Choose an option: ")
    return choice

    board = [list(row) for row in lines]  # Convert each string to a list
    return board
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
     # Read the game board from the text file
    playerBoard = readboard("battleship.txt")
    while True:
        choice = menu()

        if choice == "1":
            printboard(playerBoard)

        elif choice == "2":
            playermakemove(playerBoard)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

# board = [ [0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0] ]
#board[1][2] = 1
    # Print the board
    

if __name__ == "__main__":
        main()

        

   
