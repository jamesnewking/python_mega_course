# todo list writing to a local .txt file to a Window
from modules import helper_functions
import PySimpleGUI as sg

cycle = True
currentList = helper_functions.get_current_list()
appTitle = "To-do App"
prompt = "Type in a to-do item:"
todoListPrompt = "To-do list"
label = sg.Text(prompt)
labelList = sg.Text(todoListPrompt)
list_box = sg.Listbox(values=currentList, key="todos",
                      enable_events=True, size=[45,10])
input_box = sg.InputText(tooltip=prompt, key="todo")
add_button = sg.Button("Add")
clear_button = sg.Button("X")
edit_button = sg.Button("Edit", key="Edit")
done_button = sg.Button("Done", key="Done")
exit_button = sg.Button("Exit")
layout = [
    [label],
    [input_box, clear_button, add_button],
    [labelList],
    [list_box, edit_button, done_button],
    [exit_button]
]
font = ('Helvetica', 12)
window = sg.Window(appTitle, layout=layout, font=font)
# layout needs to be a list of lists of pysimple widgets
while cycle:
    event, values = window.read()
    # print(f"event: {event}")
    # print(f"values: {values}")
    if values['todos']:
        selected_todo_filtered = values['todos'][0].strip('\n')
    else:
        selected_todo_filtered = ""
    # print(f"selected: {selected_todo_filtered}")
    match event:
        case "Add":
            if len(values['todo']):
                addItem = values['todo'] + '\n'
                currentList.append(addItem)
                helper_functions.write_current_list(currentList)
                currentList = helper_functions.get_current_list()
                window['todo'].update(value="")
                window['todos'].update(values=currentList)
        case "Edit":
            newList = [item.replace(selected_todo_filtered,values['todo']) for item in currentList]
            helper_functions.write_current_list(newList)
            currentList = helper_functions.get_current_list()
            window['todos'].update(values=currentList)
            window['todo'].update(value="")
            window['todos'].update(values=currentList)
        case "Done":
            if len(selected_todo_filtered):
                remove_item = selected_todo_filtered + "\n"
                currentList.remove(remove_item)
                helper_functions.write_current_list(currentList)
                currentList = helper_functions.get_current_list()
                window['todo'].update(value="")
                window['todos'].update(values=currentList)
        case "todos":
            window['todo'].update(value=selected_todo_filtered)
        case "X":
            window['todo'].update(value="")
            window['todos'].update(values=currentList)
        case "Exit" | sg.WIN_CLOSED:
            cycle = False
window.close()
