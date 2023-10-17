# todo list writing to a local .txt file
prompt = "Your options are: Show, Add, Edit, Complete, Exit: "
cycle = True


def get_current_list(filepath):
    with open(filepath, 'r') as todo_file:
        current_list = todo_file.readlines()
    return current_list


def write_current_list(filepath, todo_list):
    with open(filepath, 'w') as todoFile:
        todoFile.writelines(todo_list)


while cycle:
    usrInput = input(prompt)
    usrInput = usrInput.strip().title()
    match usrInput:
        case "Show":
            currentList = get_current_list('todos.txt')
            filteredList = [item.strip("\n") for item in currentList]
            # list comprehension
            for index, item in enumerate(filteredList):
                print(f"{index + 1}) {item}")
            if len(currentList) <= 0:
                print("Empty list")
        case "Add":
            addItem = input("Add this to list: ") + "\n"
            currentList = get_current_list('todos.txt')
            currentList.append(addItem)
            write_current_list('todos.txt', currentList)
            # todoFile = open('todos.txt', 'w')
            # todoFile.writelines(currentList)
            # todoFile.close()
        case "Edit":
            currentList = get_current_list('todos.txt')
            editIndex = int(input("Edit index number: ")) - 1
            newItem = input("New item name: ") + "\n"
            currentList[editIndex] = newItem
            write_current_list('todos.txt', currentList)
            # with open('todos.txt', 'w') as todoFile:
            #     todoFile.writelines(currentList)
        case "Complete":
            currentList = get_current_list('todos.txt')
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
            write_current_list('todos.txt', currentList)
            # with open('todos.txt', 'w') as todoFile:
            #     todoFile.writelines(currentList)
        case "Exit":
            cycle = False
print("Bye!")
