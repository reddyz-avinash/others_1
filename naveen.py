import subprocess

def get_git_user_info():
    try:
        # Get local Git user name
        name = subprocess.check_output(['git', 'config', 'user.name']).decode().strip()
