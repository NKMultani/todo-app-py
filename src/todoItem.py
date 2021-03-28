class TodoItem():
    def __init__(self, title, status):
        self.title = title
        self.status = status

    def print(self):
        statusUi = "[ ]"
        if self.status == True:
            statusUi = "[x]"
        print(statusUi + " " + self.title)
        print("--------------------------") 
