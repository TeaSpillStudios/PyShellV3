import os

# Utility shell commands
def cat(args):
    for arg in args:
        with open(arg, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            line_count_digits = len(str(line_count))

            if line_count > 0 and not lines[0] == "":
                print(f"Loaded {line_count} line.\n")
            else:
                print("Empty file detected")

            for (i, line) in enumerate(lines):
                print("{} | {}".format(str(i + 1).zfill(line_count_digits), line.strip("\n")))

def touch(args):
    for arg in args:
        print("Creating file {arg}")

        with open(arg, "w") as f:
            f.close()

def cd(args):
    for arg in args:
        os.chdir(arg)

# Ascii logo shell commands
def banner(args):
    print("""
 mmmmm          mmmm  #             ''#    ''#                   mmmm 
 #   '# m   m  #'   ' # mm    mmm     #      #           m   m  '   '#
 #mmm#' 'm m'  '#mmm  #'  #  #'  #    #      #           'm m'    mmm'
 #       #m#       '# #   #  #''''    #      #            #m#       '#
 #       '#    'mmm#' #   #  '#mm'    'mm    'mm           #    'mmm#'
         m'                                                           
        ''       
""")

def acat(args):
    print(r"""
   |\__/,|   (`\
   |o o  |__ _)
 _.( T   )  `  /
((_ `^--' /_<  \
`` `-'(((/  (((/

""")

aliases = {
    "ls"    :    "dir",
    "rm"    :    "del",
    "mv"    :    "move",
    "clear" :    "cls",
    "py"    :    "python",
}

shell_commands = {
    "banner" : banner,
    "cat"    : cat,
    "acat"   : acat,
    "touch"  : touch,
    "cd"     : cd,
}

def handle_command(user_input):
    command = user_input.split(" ")[0]
    args = user_input.split(" ")[1:]
    args_as_string = ''.join(args)

    try:
        if command == "exit":
            exit()
        elif command in aliases:
            os.system(f"{aliases[command]} {args_as_string}")
        elif command in shell_commands:
            shell_commands[command](args)
        else:
            os.system(f"{command} {args_as_string}")
    except Exception as exception:
        print(f"Error command!\n    {exception}")

banner([])

while True:
    handle_command(input(f"{os.getcwd()} > "))
