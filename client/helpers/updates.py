import platform
from util.updates import get_updates_windows, get_updates_linux, get_updates_macOs

def get_updates():
    os = platform.system().lower()
    
    try:
        if os == "windows":
            return get_updates_windows()
        elif os == "linux":
            return get_updates_linux()
        elif os == "darwin": 
            return get_updates_macOs()
        else:
            print(f"Unsupported OS: {os}")
            return []
    except Exception as e:
        print(f"Error retrieving updates: {e}")
        return []