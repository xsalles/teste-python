import subprocess
import json
from datetime import datetime

def get_updates_windows():
    cmd = [
        "powershell",
        "Get-HotFix | Select-Object Description, HotFixID, InstalledOn | ConvertTo-Json"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    def parse_datetime(installed_on):
        if isinstance(installed_on, dict):
            dt_str = installed_on.get('DateTime')
            if dt_str:
                try:
                    return datetime.strptime(dt_str, "%A, %B %d, %Y %I:%M:%S %p")
                except Exception:
                    return None
            return None
        
    try: 
        
        updates = json.loads(result.stdout)
        if isinstance(updates, dict):
            updates = [updates]
        return [
            {
                'description': update.get('Description', 'Unknown'),
                'hotfix_id': update.get('HotFixID', 'Unknown'),
                'installed_on': parse_datetime(update.get('InstalledOn', None)).isoformat()
            }
            for update in updates
        ]
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return []