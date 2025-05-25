import platform
import subprocess

def get_logged_user_linux_mac():
    os = platform.system().lower()
    try:
        if os == "linux" or os == "darwin":
            result = subprocess.run(['who'], capture_output=True, text=True)
            users = []
            for line in result.stdout.splitlines():
                if line:
                    parts = line.split()
                    
                    if len(parts) >= 4:
                        username = parts[0]
                        login_time = f"{parts[2]} {parts[3]}"
                        users.append({"username": username, "login_time": login_time})
            return users
        else:
            print(f"Unsupported OS: {os}")
            return []
    except Exception as e:
        print(f"Error retrieving logged users: {e}")  
        return []

