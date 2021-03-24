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


def printItem(item):
    statusUi = "[ ]"
    if item.status == True:
        statusUi = "[x]"
    print(statusUi + " " + item.title)
    print("--------------------------")    