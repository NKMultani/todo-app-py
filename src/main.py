import os
import todoClass
import helper
import data

os.system("clear")

helper.printHeader()

data.addTodoItem("apple")
data.changeTodoItemStatus("apple")
#data.removeTodoItem("apple")

for todoItem in data.todoItems:
    todoItem.print()

helper.printFooter()