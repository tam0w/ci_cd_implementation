import time
import os
import sys

#
# def validate_launch_script():
#
#     parent_cmdline = ""
#     try:
#         parent_pid = os.getppid()
#         parent_cmdline = open(f"/proc/{parent_pid}/cmdline", "rb").read().decode("utf-8")
#     except Exception as e:
#         print(f"Error getting parent process command line: {e}")
#         sys.exit(1)
#
#     # Check if the authorized launch script is in the parent process command line
#     authorized_script = "launch_script.py"  # Change this to the actual name of your launch script
#     if authorized_script not in parent_cmdline:
#         print("User not logged in. Please use the launcher.exe to login.")
#         sys.exit(1)
#
# # Validate the launch script before executing the main logic
# validate_launch_script()

# Your main script logic goes here
# ...


while True:

    name = input('What is your name? \n')

    if name.lower() == 'exit':
        exit()

    else:
        print(f"Wow {name} really sucks.")
        time.sleep(0.5)



