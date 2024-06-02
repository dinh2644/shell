import sys


def main():
    
    # Wait for user input 
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        userInput = input()

        if(userInput == "exit 0"):
            break

        print(f'{userInput}: command not found')

       


if __name__ == "__main__":
    main()
