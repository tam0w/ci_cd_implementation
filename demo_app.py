import requests
v = 1.1
def check_for_update(current_version):
    # Query GitHub API to get the latest release version
    url = "https://api.github.com/repos/tam0w/ci_cd_implementation/releases/latest"
    response = requests.get(url)
    latest_version = float(response.json()["tag_name"])
    print(latest_version)

    # Compare versions and return True if an update is available
    return latest_version > current_version


while True:

    check_for_update(v)

    name = input('What is your name? \n')


    if name.lower() == 'exit':
        exit()

    else:
        print(f"\nWow {name} really sucks.\n")






''' 
Command to run:

pyinstaller --noconfirm --onedir --console --name "ci_cd_test"  "D:/PROJECTS/ci_cd_implementation/demo_app.py" 

'''