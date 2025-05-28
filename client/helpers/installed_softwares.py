import platform
from client.util.installed_softwares.get_installed_software_windows import get_installed_software_windows
from client.util.installed_softwares.get_installed_software_linux import get_installed_software_linux
from client.util.installed_softwares.get_installed_software_mac import get_installed_software_mac

def get_installed_softwares():
    os = platform.system().lower()
    
    try:
        if os == "windows":
            return get_installed_software_windows()
        elif os == "linux":
            return get_installed_software_linux()
        elif os == "darwin": 
            return get_installed_software_mac()
        else:
            print(f"Unsupported OS: {os}")
            return []
    except Exception as e:
        print(f"Error retrieving installed software: {e}")
        return []