import platform 
import subprocess

def get_logged_user_windows():
    os = platform.system().lower()
    try:
        if os == "windows":
            result = subprocess.run(['whoami'], capture_output=True, text=True)
            return result.stdout.strip()
        
    except Exception as e:
        print(f"Error retrieving logged users: {e}")
        return []

print(get_logged_user_windows())