#-------------------------------------------------------------------------------
# Name:        Problem 19.6 Problem 1
# Purpose:
#
# Author:      Lilyj
#
# Created:     13/11/2025
# Copyright:   (c) Lilyj 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def readposint():
    while True:
        try:
            userinput = input("postive integer: ")
            posin = int(userinput)
            if posin < 0:
                my_error = ValueError("Not a postitive integer")
                raise my_error
            return posin
        except (KeyboardInterrupt,EOFError):
            print("Dont try again")
        except ValueError as my_error:
            print(f"{my_error}")
if __name__ == '__main__':
   posint = readposint()
   print(posint)
        
