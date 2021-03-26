def printHeader():
    print("--------------------------")
    print("-------- Todo App --------")
    print("--------------------------")
    print("")
    print("")


def printFooter():
    print("")
    print("")
    print("--------------------------")
    print("--- Created by Navdeep ---")
    print("--------------------------")   


def printMainMenu():
    print("")
    print("")
    print("*** Main Menu ***")
    print("1: Add new item")
    print("2: Remove item")
    print("3: Toggle item status")
    print("4: Exit")

def getUserInputForMainMenu():
    op = input("Please enter your choice: ") 
    if(op == "1" or op == "2" or op == "3" or op == "4"):
        return op
    print("Your option is not valid. Please try again.")
    getUserInputForMainMenu() 