import subprocess
import time
import os
import sys

def init_function():
    # Your initialization logic here
    version_number = str(3.1)
    print(version_number)

def main_function():
    name = input('What is your name? \n')

    if name.lower() == 'exit':
        sys.exit()

    else:
        print(f"Wow {name} really sucks.")
        time.sleep(0.5)

if __name__ == "__main__":
    # Check if a command-line argument is provided to determine the mode
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        init_function()
    elif len(sys.argv) > 1 and sys.argv[1] == "main":
        main_function()
    else:
        print("Usage: python script.py [init | main]")
