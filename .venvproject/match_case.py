
todos = []

while True:
    user_action = input("Select action: Add, Show, or Exit: ")

    match user_action:
        case 'add':
            todo = input("Enter todo item: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("Bye!")
