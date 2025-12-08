import random


def readboard(filename):
    # Open the file and read all lines without newline characters
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    board = [list(row) for row in lines]  # Convert each string to a list
    return board
def menu():
    print("\n--- MENU ---")
    print("1. Play Game")
    print("2. Quit")
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
def computermakemove(board):
# Generate a random integer between 0 and 5
    x = random.randint(0, 5)
    y = random.randint(0, 5)
    if board[x][y] == "1": # checking if its a hit
        board[x][y] = "+"
    if board[x][y] == "0": # checking if theres a miss 
        board[x][y] = "x"

def checkWin(board):
    endGame = True
    for row in board:
        if "1" in row:
            endGame = False

    return endGame

def gamefunction(playerboard,computerboard):
    
    while True:
        
        printboard(computerboard)
        playermakemove(computerboard)
        printboard(computerboard)
        #call check win and see if player won
        #if player won, break out of loop
        
        printboard(playerboard)
        computermakemove(playerboard)
        printboard(playerboard)
        #call checkwin and see if computer won
        #if computer won, break out of loop
       
def main():
     # Read the game board from the text file
    playerBoard = readboard("battleship.txt")
    computerBoard = readboard("computerboard.txt")
    
    while True:
        choice = menu()

        if choice == "1":
           gamefunction(playerBoard,computerBoard) 
            #call game function

        elif choice == "2":
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

        

   
