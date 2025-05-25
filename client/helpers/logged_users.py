import platform
from util.logged_users import get_logged_user_windows, get_logged_user_linux_mac


def get_logged_user():
    os = platform.system().lower()
    
    try:
        if os == "windows":
            return get_logged_user_windows()
        elif os == "linux" or os == "darwin":
            return get_logged_user_linux_mac()
        else:
            print(f"Unsupported OS: {os}")
            return []
    except Exception as e:
        print(f"Error retrieving logged users: {e}")
        return []