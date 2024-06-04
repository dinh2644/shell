import sys
import os
import subprocess as sp

#import pdb; pdb.set_trace()

def main():

    PATH = os.environ["PATH"]
     
    
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Get user's input/command
        userInput = input()
        userCommand = userInput.split()

        if(userInput.strip().lower() != ""):
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

                # loop through PATH to find path of command
                for path in paths:
                    if os.path.isfile(f'{path}/{userCommand[1]}'):
                        whichPath = f'{path}/{userCommand[1]}'
                        break

                validCommands = ["exit","echo","type"]

                if(userCommand[1] in validCommands):
                    sys.stdout.write(f'{userCommand[1]} is a shell builtin\n')
                    continue
                elif(whichPath):
                    sys.stdout.write(f'{userCommand[1]} is {whichPath}\n')
                    continue
                else:
                    sys.stdout.write(f'{userCommand[1]}: not found\n')
                    continue

            # Handle PWD
            if userCommand[0] == "pwd" and len(userCommand) == 1:
                sys.stdout.write(f'{os.getcwd()}\n')
                continue


            # Handle executables
            if len(userCommand) > 1:
                exe = userCommand[0]
                result = sp.run([exe,userCommand[1]],capture_output=True,text=True)
                if result.returncode == 0:
                    #sys.stdout.write(f'{result.stdout}\n')
                    os.system(userInput)
                    continue
                else:
                    sys.stdout.write(f'{" ".join(userCommand)}: command not found\n')
                    continue
                #if os.path.isfile(userCommand[0]):
                #    os.system(userInput)
                #else:
                #    sys.stdout.write(f'{" ".join(userCommand)}: command not found\n')
            else:
                sys.stdout.write(f'{" ".join(userCommand)}: command not found\n')
                continue
        else:
            sys.stdout.write(f'{userInput}: command not found\n')
            continue
                
       
if __name__ == "__main__":
    main()
