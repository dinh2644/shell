import sys
import os
#import pdb; pdb.set_trace()

def main():

    PATH = os.environ["PATH"]
    
    
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Get user's input/command
        userInput = input()
        userCommand = userInput.split()

        validCommands = ["exit","echo","type"]

        # Check if command is valid
        if(userCommand[0].lower() in validCommands):

            # Handle exit
            if(userCommand[0] == "exit" and len(userCommand) == 2):
                if(userCommand[1] == "0"):
                    break
                else:
                    sys.stdout.write(f'{" ".join(userCommand)}: command not found\n')
                    continue

            # Handle echo
            if(userCommand[0] == "echo" and len(userCommand) > 1):
                sys.stdout.write(f'{" ".join(userCommand[1:])}\n')
                continue

            # Handle type
            if(userCommand[0] == "type" and len(userCommand) == 2):
                paths = PATH.split(":")
                whichPath = None
                # Loop through PATH to find path of command
                for path in paths:
                    if os.path.isfile(f'{path}/{userCommand[1]}'):
                        whichPath = f'{path}/{userCommand[1]}'
                        break

                if(userCommand[1] in validCommands):
                    sys.stdout.write(f'{userCommand[1]} is a shell builtin\n')
                    continue
                elif(whichPath):
                    sys.stdout.write(f'{userCommand[1]} is {whichPath}\n')
                    continue
                else:
                    sys.stdout.write(f'{userCommand[1]}: not found\n')
                    continue

            sys.stdout.write(f'{" ".join(userCommand)}: command not found\n')
        else:
            sys.stdout.write(f'{userCommand[0]}: command not found\n')

       


if __name__ == "__main__":
    main()
