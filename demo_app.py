import time
import requests

current_version = 2.5

def run_updater():

    print('Update in progress.')

def check_for_update(current_version):
    # Query GitHub API to get the latest release version
    url = "https://api.github.com/repos/tam0w/ci_cd_implementation/releases/latest"
    response = requests.get(url)
    latest_version = float(response.json()["tag_name"])
    print("Update Checker:")
    print("Latest Version:", latest_version)
    print("Current Version:", current_version)
    print("------------------------------------")
    time.sleep(0.5)

    return latest_version > current_version

if check_for_update(current_version):

    run_updater()

while True:

    name = input('What is your name? \n')

    if name.lower() == 'exit':
        exit()

    else:
        print(f"Wow {name} really sucks.")
        time.sleep(0.5)


''' 
Command to run:

pyinstaller --noconfirm --onedir --console --name "ci_cd_test"  "D:/PROJECTS/ci_cd_implementation/demo_app.py" 

pyinstaller --noconfirm --onedir --console --name "ci_cd_test"  "/workspaces/ci_cd_implementation/demo_app.py" 

pyinstaller --noconfirm --onefile --console --name "ci_cd.exe" --icon "update.ico" "demo_app.py"
'''