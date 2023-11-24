import requests
v = 1.0
def check_for_update(current_version):
    # Query GitHub API to get the latest release version
    url = "https://api.github.com/repos/your_username/your_repository/releases/latest"
    response = requests.get(url)
    latest_version = response.json()["tag_name"]

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