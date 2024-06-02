import sys


def main():
    
    # Wait for user input 
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        userInput = input()
        print(f'{userInput}: command not found')
       


if __name__ == "__main__":
    main()
