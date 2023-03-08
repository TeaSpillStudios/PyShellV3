import os

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

aliases = {
    "ls"    :    "dir",
    "rm"    :    "del",
    "mv"    :    "move",
    "clear" :    "cls",
    "py"    :    "python",
}

shell_commands = {
    "banner" : banner,
}

def handle_command(user_input):
    command = user_input.split(" ")[0]
    args = user_input.split(" ")[1:]

    try:
        if command == "exit":
            exit()
        elif command in aliases:
            os.system(f"{aliases[command]} {''.join(args)}")
        elif command in shell_commands:
            shell_commands[command](args)
        else:
            os.system(f"{command} {''.join(args)}")
    except Exception as exception:
        print(f"Error command!\n    {exception}")

banner([])

while True:
    handle_command(input(f"{os.getcwd()} > "))
