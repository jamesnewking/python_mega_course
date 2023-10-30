FILEPATH = "todos.txt"
def get_current_list(filepath=FILEPATH):
    """ Get list from text file"""
    with open(filepath, 'r') as todo_file:
        current_list = todo_file.readlines()
    return current_list


def write_current_list(todo_list, filepath=FILEPATH):
    """ Write list to text file"""
    with open(filepath, 'w') as todoFile:
        todoFile.writelines(todo_list)


if __name__ == "__main__":
    print("You will only see this if this file is run directly")
    print("You will not see this when this module is imported")
    print("Good for debugging")
    print(get_current_list("../todos.txt"))
