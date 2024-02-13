""" user_prompt = "Enter a todo: "
text1 = input(user_prompt)
text2 = input(user_prompt)
text3 = input(user_prompt)

todos = [text1, text2, text3]

print(todos) """

todos = []
what_ToDo = "Enter a todo: "



while True:
    todo = input(what_ToDo)
    todos.append(todo)
    print(todos)
