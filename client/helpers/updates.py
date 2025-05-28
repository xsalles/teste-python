import platform
from client.util.updates.get_updates_linux import get_updates_linux
from client.util.updates.get_updates_macOs import get_updates_mac
from client.util.updates.get_updates_windows import get_updates_windows

def get_updates():
    os = platform.system().lower()
    
    try:
        if os == "windows":
            return get_updates_windows()
        elif os == "linux":
            return get_updates_linux()
        elif os == "darwin": 
            return get_updates_mac()
        else:
            print(f"Unsupported OS: {os}")
            return []
    except Exception as e:
        print(f"Error retrieving updates: {e}")
        return []