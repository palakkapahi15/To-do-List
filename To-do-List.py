import functions

while True:
    user_action = input("Type add, show, edit, completed or exit: ")
    user_action - user_action.strip("")

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos(todo)
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todos()
            new_todos = input("Enter new todo: ")
            todos[number] = new_todos + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith("completed"):
        try:
            number = int(user_action[10:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that index number.")
            continue

    elif user_action.startswith("exit"):
        break
    
    else:
        print("Command is not valid.")

