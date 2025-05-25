import subprocess
import json

def get_installed_software_windows():
    cmd = [
         "powershell",
        "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | "
        "Select-Object DisplayName, DisplayVersion, InstallDate | ConvertTo-Json"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    try:
        installed_software = json.loads(result.stdout)
        
        return installed_software
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return []
    
print(get_installed_software_windows())