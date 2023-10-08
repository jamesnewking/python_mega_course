# todo list writing to a local .txt file
prompt = "Your options are: Show, Add, Edit, Complete, Exit: "
cycle = True

while cycle:
    usrInput = input(prompt)
    usrInput = usrInput.strip().title()
    match usrInput:
        case "Show":
            # context manager
            with open('todos.txt', 'r') as todoFile:
                currentList = todoFile.readlines()
            # todoFile = open('todos.txt', 'r')
            # currentList = todoFile.readlines()
            # todoFile.close()

            # for index, item in enumerate(currentList):
            #     stripExtraReturn = item.strip('\n')
            #     print(f"{index + 1}) {stripExtraReturn}")
            filteredList = [item.strip("\n") for item in currentList]
            # list comprehension
            for index, item in enumerate(filteredList):
                print(f"{index + 1}) {item}")
            if len(currentList) <= 0:
                print("Empty list")
        case "Add":
            addItem = input("Add this to list: ") + "\n"
            # usrList.append(addItem)
            todoFile = open('todos.txt', 'r')
            currentList = todoFile.readlines()
            # todoFile.close()
            currentList.append(addItem)
            todoFile = open('todos.txt', 'w')
            todoFile.writelines(currentList)
            todoFile.close()
        case "Edit":
            # todoFile = open('todos.txt', 'r')
            with open('todos.txt', 'r') as todoFile:
                currentList = todoFile.readlines()
            # todoFile.close()
            editIndex = int(input("Edit index number: ")) - 1
            newItem = input("New item name: ") + "\n"
            currentList[editIndex] = newItem
            # todoFile = open('todos.txt', 'w')
            with open('todos.txt', 'w') as todoFile:
                todoFile.writelines(currentList)
            # todoFile.close()
        case "Complete":
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
        case "Exit":
            cycle = False
print("Bye!")





