# todo list locally in memory
prompt = "Your options are: Show, Add, Edit, Complete, Exit: "
cycle = True
usrList = []
while cycle:
    usrInput = input(prompt)
    usrInput = usrInput.strip().title()
    match usrInput:
        # case "Show":
        #     for items in usrList:
        #         print(usrList.index(items) + 1, ")", items)
        case "Show":
            for index, items in enumerate(usrList):
                # print((index + 1), ")", items)
                outputString = f"{(index+1)}) {items}"
                print(outputString)
        case "Add":
            addItem = input("Add this to list: ")
            usrList.append(addItem)
        case "Edit":
            editIndex = int(input("Edit index number: ")) - 1
            newItem = input("New item name: ")
            usrList[editIndex] = newItem
        case "Complete":
            removeItem = input("Which index to remove?(number or item name)")
            if(str.isdigit(removeItem)):
                removeItem = int(removeItem)
                if(removeItem > len(usrList) or removeItem < 1):
                    print("Index is out of bounds. Index is between 1 to", len(usrList))
                else:
                    removeIndex = removeItem - 1
                    print("Removed:", usrList.pop(removeIndex))
            else:
                usrList.remove(removeItem)
        case "Exit":
            cycle = False
print("Bye!")





