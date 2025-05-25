import platform
import subprocess

def get_logged_user_linux_mac():
    os = platform.system().lower()
    try:
        if os == "linux" or os == "darwin":
            result = subprocess.run(['who'], capture_output=True, text=True)
            users = set()
            for line in result.stdout.splitlines():
                if line:
                    users.add(line.split()[0])
            return list(users)
        else:
            print(f"Unsupported OS: {os}")
            return []
    except Exception as e:
        print(f"Error retrieving logged users: {e}")  
        return []      
    
print(get_logged_user_linux_mac())
    