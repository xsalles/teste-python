import platform
from client.util.logged_users.get_logged_user_linux_mac import get_logged_user_linux_mac
from client.util.logged_users.get_logged_user_windows import get_logged_user_windows


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