# todo list writing to a local .txt file
prompt = "Your options are: show, add, new, edit, complete, exit: "
cycle = True

while cycle:
    usrInput = input(prompt)
    usrInput = usrInput.strip()
    if "show" in usrInput:
        with open('todos.txt', 'r') as todoFile:
            currentList = todoFile.readlines()
        filteredList = [item.strip("\n") for item in currentList]
        for index, item in enumerate(filteredList):
            print(f"{index + 1}) {item}")
        if len(currentList) <= 0:
            print("Empty list")
    elif "add" in usrInput or "new" in usrInput:
        if len(usrInput) > 4:
            addItem = usrInput[4:]
            addItemWithNewLine = addItem + "\n"
            with open('todos.txt', 'r') as todoFile:
                currentList = todoFile.readlines()
                currentList.append(addItemWithNewLine)
            with open('todos.txt', 'w') as todoFile:
                todoFile.writelines(currentList)
                print(f"Added {addItem} to the list.")
        else:
            addItem = input("Add this to list: ") + "\n"
            todoFile = open('todos.txt', 'r')
            currentList = todoFile.readlines()
            # todoFile.close()
            currentList.append(addItem)
            todoFile = open('todos.txt', 'w')
            todoFile.writelines(currentList)
            todoFile.close()
    elif "edit" in usrInput:
        if len(usrInput) > 5:
            editIndex = int(usrInput[5:]) - 1
            with open('todos.txt', 'r') as todoFile:
                currentList = todoFile.readlines()
                currentListLength = len(currentList)
            if (editIndex + 1) > currentListLength or editIndex < 1:
                print(f"Index out of bounds, {editIndex + 1} needs to be greater than 0 and less than {currentListLength + 1}")
            else:
                newItem = input("New item name: ") + "\n"
                currentList[editIndex] = newItem
                with open('todos.txt', 'w') as todoFile:
                    todoFile.writelines(currentList)
                print(f"Updated item #{editIndex + 1} to {newItem[0:-1]}")
        else:
            with open('todos.txt', 'r') as todoFile:
                currentList = todoFile.readlines()

            editIndex = int(input("Edit index number: ")) - 1
            newItem = input("New item name: ") + "\n"
            currentList[editIndex] = newItem
            # todoFile = open('todos.txt', 'w')
            with open('todos.txt', 'w') as todoFile:
                todoFile.writelines(currentList)

    elif "complete" in usrInput:
        # todoFile = open('todos.txt', 'r')
        with open('todos.txt', 'r') as todoFile:
            currentList = todoFile.readlines()
        # todoFile.close()
        removeItem = input("Which index to remove?(number or item name)")
        if str.isdigit(removeItem):
            removeItem = int(removeItem)
            if removeItem > len(currentList) or removeItem < 1:
                print("Index is out of bounds. Index is between 1 to", len(currentList))
            else:
                removeIndex = removeItem - 1
                print("Removed:", currentList.pop(removeIndex))
        else:
            currentList.remove(removeItem)
        # todoFile = open('todos.txt', 'w')
        with open('todos.txt', 'w') as todoFile:
            todoFile.writelines(currentList)
        # todoFile.close()
    elif "exit" in usrInput:
        cycle = False
    else:
        print(f"<{usrInput}> is not a valid command")
print("Bye!")





