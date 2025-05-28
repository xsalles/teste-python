import platform 
import subprocess

def get_logged_user_windows():
    os = platform.system().lower()
    try:
        if os == "windows":
            whoami = subprocess.run(['whoami'], capture_output=True, text=True)
            username = whoami.stdout.strip().split('\\')[-1]  # Remove domain if present

            result = subprocess.run(['query', 'user'], capture_output=True, text=True)
            
            for line in result.stdout.splitlines():
                if username in line:
                    parts = line.split()

                    logon_time = " ".join(parts[-2:])
                    return [{"username": username, "logon_time": logon_time}]
            return [{"username": username, "logon_time": None}]
        
    except Exception as e:
        print(f"Error retrieving logged users: {e}")
        return []

print(get_logged_user_windows())