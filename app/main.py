import sys


def main():

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
                    print(f'{" ".join(userCommand)}: command not found')
                    continue

            # Handle echo
            if(userCommand[0] == "echo" and len(userCommand) > 1):
                print(" ".join(userCommand[1:]))
                continue

            # Handle type
            if(userCommand[0] == "type" and len(userCommand) == 2):
                if(userCommand[1] in validCommands):
                    print(f'{userCommand[1]} is a shell builtin')
                    continue
                else:
                    print(f'{userCommand[1]} not found')
                    continue

            print(f'{" ".join(userCommand)}: command not found')
        else:
            print(f'{userCommand[0]}: command not found')

       


if __name__ == "__main__":
    main()
