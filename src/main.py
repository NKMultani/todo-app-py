import os
import todoClass
import helper
import data

def main():
    os.system("clear")

    helper.printHeader()

    todoManager = data.ToDoManager()

    todoManager.addTodoItem("Learn python")
    todoManager.addTodoItem("Write code in python")
    todoManager.addTodoItem("Learn SQL")
    todoManager.changeTodoItemStatus("Learn python")
    #todoManager.removeTodoItem("apple")

    todoManager.printTodoItems()

    helper.printMainMenu()
    op = helper.getUserInputForMainMenu()


    if op == "1":
        print("You selected to add a new item.")
    elif op == "2":
        print("You selected to remove an item.")
    elif op == "3":
        print("You selcted to toggle an item.")
    elif op == "4":
        print("Exiting the main menu.")        

    helper.printFooter()

main()    