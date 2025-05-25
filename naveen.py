import subprocess

def get_git_user_info():
    try:
        # Get local Git user name
        name = subprocess.check_output(['git', 'config', 'user.name']).decode().strip()
         # Get local Git user email
        email = subprocess.check_output(['git', 'config', 'user.email']).decode().strip()

        print("✅ Current Git user info (local repo):")
