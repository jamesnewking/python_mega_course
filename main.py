# todo list writing to a local .txt file
prompt = "Your options are: Show, Add, Edit, Complete, Exit: "
cycle = True


def get_current_list():
    with open('todos.txt', 'r') as todo_file:
        current_list = todo_file.readlines()
    return current_list


while cycle:
    usrInput = input(prompt)
    usrInput = usrInput.strip().title()
    match usrInput:
        case "Show":
            currentList = get_current_list()
            filteredList = [item.strip("\n") for item in currentList]
            # list comprehension
            for index, item in enumerate(filteredList):
                print(f"{index + 1}) {item}")
            if len(currentList) <= 0:
                print("Empty list")
        case "Add":
            addItem = input("Add this to list: ") + "\n"
            currentList = get_current_list()
            currentList.append(addItem)
            todoFile = open('todos.txt', 'w')
            todoFile.writelines(currentList)
            todoFile.close()
        case "Edit":
            currentList = get_current_list()
            editIndex = int(input("Edit index number: ")) - 1
            newItem = input("New item name: ") + "\n"
            currentList[editIndex] = newItem
            with open('todos.txt', 'w') as todoFile:
                todoFile.writelines(currentList)
        case "Complete":
            currentList = get_current_list()
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
            with open('todos.txt', 'w') as todoFile:
                todoFile.writelines(currentList)
        case "Exit":
            cycle = False
print("Bye!")
