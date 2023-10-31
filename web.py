import streamlit as st
from modules import helper_functions

# streamlit run web.py
FILE_SOURCE = "todos.txt"
currentList = helper_functions.get_current_list(FILE_SOURCE)


def add_item():
    if len(st.session_state["todo_item"]):
        todo = st.session_state["todo_item"] + "\n"
        currentList.append(todo)
        helper_functions.write_current_list(currentList, FILE_SOURCE)
        st.session_state["todo_item"] = ""


def remove_item():
    print(f"something ")


st.title("My Web Page")
st.subheader("To-do list app")
st.write("Check the item to remove")

for index, todo in enumerate(currentList):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        currentList.pop(index)
        helper_functions.write_current_list(currentList, FILE_SOURCE)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add a to-do item",
              label_visibility="hidden",
              on_change=add_item,
              placeholder="Add a to-do item",
              key="todo_item")

# st.session_state
