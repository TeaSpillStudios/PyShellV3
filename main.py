import os

def handle_command(user_input):
    command = user_input.split(" ")[0]
    args = user_input.split(" ")[1:]

    try:
        if command == "exit":
            exit()
        else:
            os.system(f"{command} {''.join(args)}")
    except Exception as exception:
        print(f"Error command!\n    {exception}")

while True:
    handle_command(input(f"{os.getcwd()} > "))
