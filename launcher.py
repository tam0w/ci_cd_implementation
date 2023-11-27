"""
Command to run:

pyinstaller --noconfirm --onedir --console --name "ci_cd_test"  "D:/PROJECTS/ci_cd_implementation/launcher.py"

pyinstaller --noconfirm --onedir --console --name "ci_cd_test"  "/workspaces/ci_cd_implementation/launcher.py"

pyinstaller --noconfirm --onefile --console --name "ci_cd.exe" --icon "update.ico" "launcher.py"
"""
import os
import subprocess
import time
import traceback
import zipfile

import requests

current_version = 3.0

def check_for_update(this_version):
    # Query GitHub API to get the latest release version
    url = "https://api.github.com/repos/tam0w/ci_cd_implementation/releases/latest"

    github_token = "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"
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(url, headers=headers)
    print(response.json())
    latest_version = float(response.json()["tag_name"])
    print("Update Checker:")
    print("Latest Version:", latest_version)
    print("Current Version:", this_version)
    print("------------------------------------")
    time.sleep(0.5)

    return [latest_version > this_version, response.json()]


def run_updater():
    # Your update logic here
    print("Running updater...")


def download_app(resp):
    print("Downloading app...")
    assets = resp["assets"][0]
    print(assets)
    download_url = assets.get("browser_download_url")

    local_filename = os.path.join(os.getcwd(), "ci_cd.exe")

    response = requests.get(download_url)

    if response.status_code == 200:
        with open(local_filename, "wb") as f:
            f.write(response.content)
        print(f"Download successful.")


def run_script():

    script_path = os.path.join(os.path.dirname(__file__), "ci_cd.exe")
    if os.path.exists(script_path):
        subprocess.run([script_path])
    else:
        try:
            download_app(resp)
            subprocess.run([script_path])
        except Exception as e:
            traceback.print_exc()
            print(f"Error downloading the file: {e}")
            return False


update, resp = check_for_update(current_version)

if update:
    run_updater()
else:
    run_script()