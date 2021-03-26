import todoClass

class ToDoManager():
    def __init__(self):
        self.__todoItems = []

    def addTodoItem(self, title):
        item = todoClass.TodoItem(title, False)
        self.__todoItems.append(item)

    def removeTodoItem(self, title):
        for item in self.__todoItems:
            if item.title == title:
                self.__todoItems.remove(item)
                break

    def changeTodoItemStatus(self, title):
        for item in self.__todoItems:
            if item.title == title:
                item.status = not item.status
                break

    def printTodoItems(self):
        for todoItem in self.__todoItems:
            todoItem.print()          

