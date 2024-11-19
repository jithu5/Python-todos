import json
import os

# Check if the file exists, if not, create it with an empty todos list
if not os.path.exists('todos.json'):
    with open('todos.json', 'w') as f:
        json.dump({"todos": []}, f)

try:
    # Load existing todo list from JSON file if it exists, otherwise initialize an empty list
    with open('todos.json', 'r') as f:
        todo_list = json.load(f)['todos']
except Exception as e:
    print(f"Error occurred while loading todo list: {e}")
    todo_list = []

# add todo list with title as unique
def add_todo(title,description):
    for todo in todo_list:
        if todo['title'] == title:
            print("Title already exists. Please choose a unique title.")
            return
    try:
        todo_list.append({'title': title, 'description': description})
        print(f"{title} added successfully")
    except Exception as e:
        print("Error occurred while adding todo",e)

# delete todo list with title as unique
def delete_todo(title):
    # Flag to track if the title is found
    found = False
    
    # Iterate over the todo list
    for todo in todo_list:
        if todo['title'] == title:
            found = True
            try:
                todo_list.remove(todo)  # Remove the todo with the matching title
                print(f"{title} has removed successfully")
            except Exception as e:
                print(f"Error occurred while removing todo: {e}")
            break
    
    if not found:
        print("Title not found. Please check the title and try again.")

# update todo list with title as unique
def update_todo(title, new_title=None, new_description=None):
    for todo in todo_list:
        if todo['title'] == title:
            if new_title:
                todo['title'] = new_title
            if new_description:
                todo['description'] = new_description
            print(f"Todo '{title}' updated successfully.")
            return
    print("Title not found. Please check the title and try again.")

# read todo
def read_todo():
    print(f'Todos length:{len(todo_list)}')
    for todo in todo_list:
        print(f"Title: {todo['title']}, Description: {todo['description']}")

# main loop to handle user inputs
while True:
    option = input("Enter 'add','delete','read','update' for corresponding operation or 'save' to save and 'q' to quit: ")

    match (option.lower()):
        case 'add':
            title = input('Enter title for todo,title should be unique: ')
            description = input('Enter description for todo: ')
            add_todo(title,description)
            continue
        case 'delete':
            title = input('Enter title for todo to delete: ')
            delete_todo(title)
            continue
        case 'update':
            title = input('Enter title of todo to update: ')
            new_title = input('Enter new title (leave empty to keep current): ') or None
            new_description = input('Enter new description (leave empty to keep current): ') or None
            update_todo(title, new_title, new_description)
            continue
        case 'read':
            read_todo()
            continue
        case 'save':
            print("Saving...")
            try:
                with open('todos.json','w') as f:
                    json.dump({"todos": todo_list}, f)
                print("Your todos has been saved succesfully!")
            except Exception as e:
                print(f"An error occurred while saving your todos: {e}")
            continue
        case 'q':
            print("Goodbye!")
            break
        case _:
            print("Invalid option. Please try again.")
            continue