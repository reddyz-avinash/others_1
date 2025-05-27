import subprocess

def get_git_user_info():
    try:
        # Get local Git user name
        name = subprocess.check_output(['git', 'config', 'user.name']).decode().strip()
         # Get local Git user email
        email = subprocess.check_output(['git', 'config', 'user.email']).decode().strip()

        print("✅ Current Git user info (local repo):")
        print(f"  Name : {name}")
        print(f"  Email: {email}")
        except subprocess.CalledProcessError:
        print("❌ Git user info not found in local config.")

# Run it
get_git_user_info()


output:
