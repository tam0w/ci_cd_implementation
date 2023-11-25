import time
import requests

v = 1.3

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

check_for_update(v)

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

pyinstaller --noconfirm --onedir --console --name "ci_cd_test"  "demo_app.py" 

'''