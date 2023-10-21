# todo list writing to a local .txt file
from modules import helper_functions
import time

prompt = "Your options are: Show, Add, Edit, Complete, Exit: "
cycle = True

while cycle:
    time_now = time.strftime("%b %d, %Y %H:%M:%S")
    print(f"It is now: {time_now}")
    usrInput = input(prompt)
    usrInput = usrInput.strip().title()
    match usrInput:
        case "Show":
            currentList = helper_functions.get_current_list()
            filteredList = [item.strip("\n") for item in currentList]
            # list comprehension
            for index, item in enumerate(filteredList):
                print(f"{index + 1}) {item}")
            if len(currentList) <= 0:
                print("Empty list")
        case "Add":
            addItem = input("Add this to list: ") + "\n"
            currentList = helper_functions.get_current_list()
            currentList.append(addItem)
            helper_functions.write_current_list(currentList)
            # todoFile = open('todos.txt', 'w')
            # todoFile.writelines(currentList)
            # todoFile.close()
        case "Edit":
            currentList = helper_functions.get_current_list()
            editIndex = int(input("Edit index number: ")) - 1
            newItem = input("New item name: ") + "\n"
            currentList[editIndex] = newItem
            helper_functions.write_current_list(currentList)
            # with open('todos.txt', 'w') as todoFile:
            #     todoFile.writelines(currentList)
        case "Complete":
            currentList = helper_functions.get_current_list()
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
            helper_functions.write_current_list(currentList)
            # with open('todos.txt', 'w') as todoFile:
            #     todoFile.writelines(currentList)
        case "Exit":
            cycle = False
print("Bye!")
