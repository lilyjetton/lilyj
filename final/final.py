import random
import turtle 

def readboard(filename):
    # Open the file and read all lines without newline characters
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    board = [list(row) for row in lines]  # Convert each string to a list
    return board
def menu():
    print("\n--- MENU ---")
    print("1. Play Game")
    print("2. How to play")
    print("3. Quit")
    choice = input("Choose an option: ")
    return choice

    board = [list(row) for row in lines]  # Convert each string to a list
    return board
def printboard(board):
    # Print each row with spaces between numbers
    for rows in board:
        print(" ".join(str(num) for num in rows))

def print_hidden_board(board):
    # Hide enemy ships (1), reveal hits (+) and misses (x)
    for row in board:
        display_row = []
        for cell in row:
            if cell == "1": # Hide ships 
                display_row.append("0")
            else:
                display_row.append(cell)
        print(" ".join(display_row))

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
    x = random.randint(0, len(board) - 1)
    y = random.randint(0, len(board[0]) - 1)
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
def draw_star():
    screen = turtle.Screen()
    screen.bgcolor("black")

    star = turtle.Turtle()
    star.color("yellow")
    star.speed(3)
    star.width(3)
    
    # Move to better position 
    star.penup()
    star.setheading(30)
    star.backward(150)
    star.setheading(0)
    star.pendown()
    
    # Draw the star
    for _ in range(5):
        star.forward(300)
        star.right(144)

    turtle.done()

def gamefunction(playerboard,computerboard):
    
    while True:
       print("Your Ships:")
       printboard(playerboard)
       
       print("Enemy Ships:")
       print_hidden_board(computerboard)
       
        # Player move
       print("\nYour turn:")
       playermakemove(computerboard)
       
        # Check if player won
       if checkWin(computerboard):
           print("You sank all the enemy ships!")
           draw_star()
           break
        
        # Computer move
       print("\nEnemy turn:")
       computermakemove(playerboard)
       
        # Check if computer won
       if checkWin(playerboard):
           print("The Enemy destroyed all your ships!")
           break
def main():
     # Read the game board from the text file
    playerBoard = readboard("battleship.txt")
    computerBoard = readboard("computerboard.txt")
    
    while True:
        choice = menu()

        if choice == "1":
           gamefunction(playerBoard,computerBoard) 
            # Call game function
        elif choice == "2":
            print("Choose two points to decide where you are going to shoot. plus is a win, x is a miss.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# board = [ [0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0],
#           [0, 0, 0] ]
#board[1][1] = 1
    # Print the board
    

if __name__ == "__main__":
        main()

        

   
