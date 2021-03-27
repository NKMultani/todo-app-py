def printHeader():
    print("--------------------------")
    print("-------- Todo App --------")
    print("--------------------------")

def printFooter():
    print("\n--------------------------")
    print("--- Created by Navdeep ---")
    print("--------------------------")   

def printMainMenu():
    print("\n*** Main Menu ***")
    print("1: Add new item")
    print("2: Remove item")
    print("3: Toggle item status")
    print("4: Exit")

def getUserInputForMainMenu():
    op = input("\nPlease enter your choice: ") 
    if(op == "1" or op == "2" or op == "3" or op == "4"):
        return op
    print("Your option is not valid. Please try again.")
    return getUserInputForMainMenu() 

def getUserInputForNewItem():
    item = input("\nPlease enter your item: ")    
    return item

def getUserInputForRemoveItem():
    item = input("\nPlease enter the item you would like to remove: ")    
    return item    

def getUserInputForChangeStatusItem():
    item = input("\nPlease enter the item you would like to change status for: ")    
    return item    