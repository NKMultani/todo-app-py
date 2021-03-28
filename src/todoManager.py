import todoItem

class ToDoManager():
    def __init__(self):
        self.__todoItems = []

    def addTodoItem(self, title):
        if title == "":
            print("\nThe item is not valid. Please try again.")
            return
        item = todoItem.TodoItem(title, False)
        self.__todoItems.append(item)

    def removeTodoItem(self, title):
        for item in self.__todoItems:
            if item.title.lower() == title.lower():
                self.__todoItems.remove(item)
                break

    def changeTodoItemStatus(self, title):
        for item in self.__todoItems:
            if item.title.lower() == title.lower():
                item.status = not item.status
                break

    def printTodoItems(self):
        print("")
        if len(self.__todoItems) == 0:
            print("You have no items.")
            return 
        for todoItem in self.__todoItems:
            todoItem.print()          

