# todo list writing to a local .txt file to a Window
from modules import helper_functions
import PySimpleGUI as sg
import os
FILE_SOURCE = "todos.txt"
sg.theme('GreenTan')
if not os.path.exists(FILE_SOURCE):
    with open(FILE_SOURCE, "w") as file:
        pass

cycle = True
currentList = helper_functions.get_current_list(FILE_SOURCE)
appTitle = "To-do App"
prompt = "Type in a to-do item:"
todoListPrompt = "To-do list"
label = sg.Text(prompt)
# imageLogo = sg.Image(source="files/to-do-list-apps.png")
labelList = sg.Text(todoListPrompt)
list_box = sg.Listbox(values=currentList, key="todos",
                      enable_events=True, size=[45,10])
input_box = sg.InputText(tooltip=prompt, key="todo")
add_button = sg.Button("Add", tooltip="add item", mouseover_colors="LightBlue", key="Add")
clear_button = sg.Button("X")
padding1 = sg.Text("", key="padding1")
padding2 = sg.Text("", key="padding2")
padding3 = sg.Text("", key="padding3")
padding4 = sg.Text("", key="padding4")
padding5 = sg.Text("", key="padding5")
spacer = sg.Text("", key="spacer")
edit_button = sg.Button("Edit", key="Edit")
done_button = sg.Button("Done", key="Done")
exit_button = sg.Button("Exit")
col_left_top = sg.Column([
    [input_box],
    [spacer],
    [list_box]
])
col_right_top = sg.Column([
    [clear_button, add_button],
    [padding1],
    [padding2],
    [padding3],
    [padding4],
    [padding5],
    [edit_button],
    [done_button]
])
layout = [
    [label],
    [col_left_top, col_right_top],
    [exit_button]
]
font = ('Helvetica', 12)
window = sg.Window(appTitle, layout=layout, font=font)
# layout needs to be a list of lists of pysimple widgets
while cycle:
    event, values = window.read()
    # print(f"event: {event}")
    # print(f"values: {values}")
    try:
        selected_todo_filtered = values['todos'][0].strip('\n')
    except IndexError:
        selected_todo_filtered = ""
    except TypeError:
        selected_todo_filtered = ""
    # print(f"selected: {selected_todo_filtered}")
    match event:
        case "Add":
            if len(values['todo']):
                addItem = values['todo'] + '\n'
                currentList.append(addItem)
                helper_functions.write_current_list(currentList, FILE_SOURCE)
                currentList = helper_functions.get_current_list(FILE_SOURCE)
                window['todo'].update(value="")
                window['todos'].update(values=currentList)
        case "Edit":
            if len(selected_todo_filtered) and len(values['todo']):
                newList = [item.replace(selected_todo_filtered, values['todo']) for item in currentList]
                helper_functions.write_current_list(newList, FILE_SOURCE)
                currentList = helper_functions.get_current_list(FILE_SOURCE)
                window['todos'].update(values=currentList)
                window['todo'].update(value="")
                window['todos'].update(values=currentList)
        case "Done":
            if len(selected_todo_filtered):
                remove_item = selected_todo_filtered + "\n"
                currentList.remove(remove_item)
                helper_functions.write_current_list(currentList, FILE_SOURCE)
                currentList = helper_functions.get_current_list(FILE_SOURCE)
                window['todo'].update(value="")
                window['todos'].update(values=currentList)
            else:
                sg.popup("Select an item to complete", font=font)
        case "todos":
            window['todo'].update(value=selected_todo_filtered)
        case "X":
            window['todo'].update(value="")
            # window['todos'].update(values=currentList)
        case "Exit" | sg.WIN_CLOSED:
            cycle = False
            # window.close()
window.close()
