""" user_prompt = "Enter a todo: "
text1 = input(user_prompt)
text2 = input(user_prompt)
text3 = input(user_prompt)

todos = [text1, text2, text3]

print(todos) """

# todos = []
# what_ToDo = "Enter a todo: "



# while True:
#     todo = input(what_ToDo)
#     todos.append(todo)
#     print(todos)

#improved version of MATCH CASE integrating FOR LOOp
todos = []

while True:
    user_action = input("Select action: Add, Show, or Exit: ")

    match user_action:
        case 'add':
            todo = input("Enter todo item: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Bye!")
