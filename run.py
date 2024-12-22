def welcome():
    import time

    """
    Add welcome page
    Display game name
    """
print(" ")
print(" ")
print(" _____                                   _       ___ ___                           ")
print("/  __ \                                 | |     |   ____|                   __     ")
print("| /  \/  ___   _ __   _ __    ___   ___ | |_    |  |____    ___            |   \   ")
print("| |     / _ \ |  _ \ |  _ \  / _ \ / __|| __|   |   ____|  / _ \  ||    || | () \  ")
print("| \__/\| (_) || | | || | | ||  __/| (__ | |_    |  |      | (_) | ||    || |   _|  ")
print(" \____/ \___/ |_| |_||_| |_| \___| \___| \__|   |__|       \___/  \\___//  |   \   ")
print(" ")
print(" ")
print(" ")
print(" ")

print ("Game Rules")
print ("The objective of the game is to Connect Four tiles in the collums, they should either be connect vertically,diagonally or horizontally ") 
print ("The collums will be numberd from 1 to 7, you will have to write the number of the collum you want to drop your piece. ")
print("Good luck and enjoy!!!")  

def select_game():
    """
    the program will first show two possible options
    u can select a game to play versus a friend or the computer
    """
    print("Select game option:")

    game_options = "1) 2 Players 2) Player vs. Computer"
    game_selected = input(game_options)
           
    if game_selected == "1":
        print("Player vs Player")
    elif game_selected == "2":
        print("Player vs computer")
    else:
        print("Not a valid option, please try again")
        print("Select game option:")
        game_selected = input(game_options)


def main():
    """
    Run all program functions
    """
    welcome()
    select_game()
if __name__ == "__main__":
    main()