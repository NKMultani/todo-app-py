import todoClass

todoItems = []

def addTodoItem(title):
    item = todoClass.TodoItem(title, False)
    todoItems.append(item)

def removeTodoItem(title):
    for item in todoItems:
        if item.title == title:
            todoItems.remove(item)
            break

def changeTodoItemStatus(title):
    for item in todoItems:
        if item.title == title:
            item.status = not item.status
            break

