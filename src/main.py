import os
import helper
import todoManager

def mainMenuFunctionality():
    helper.printMainMenu()
    op = helper.getUserInputForMainMenu()
    print(op)
    if op == "1":
        item = helper.getUserInputForNewItem()
        todoManager.addTodoItem(item)
        todoManager.printTodoItems()
        mainMenuFunctionality()
    elif op == "2":
        item = helper.getUserInputForRemoveItem()
        todoManager.removeTodoItem(item)
        todoManager.printTodoItems()
        mainMenuFunctionality()
    elif op == "3":
        item = helper.getUserInputForChangeStatusItem()
        todoManager.changeTodoItemStatus(item)
        todoManager.printTodoItems()
        mainMenuFunctionality()
    elif op == "4":
        print("\nExiting the main menu.")  


def main():
    os.system("clear")

    helper.printHeader()

    global todoManager
    todoManager = todoManager.ToDoManager()

    todoManager.printTodoItems()

    mainMenuFunctionality()      

    helper.printFooter()

main()    
