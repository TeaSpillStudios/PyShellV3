import os

aliases = {
    "ls"    :    "dir",
    "rm"    :    "del",
    "mv"    :    "move",
    "clear" :    "cls",
    "py"    :    "python",
}

def handle_command(user_input):
    command = user_input.split(" ")[0]
    args = user_input.split(" ")[1:]

    try:
        if command == "exit":
            exit()
        elif command in aliases:
            os.system(f"{aliases[command]} {''.join(args)}")
        else:
            os.system(f"{command} {''.join(args)}")
    except Exception as exception:
        print(f"Error command!\n    {exception}")

while True:
    handle_command(input(f"{os.getcwd()} > "))
