import subprocess
import json

def get_updates_windows():
    cmd = [
        "powershell",
        "Get-HotFix | Select-Object Description, HotFixID, InstalledOn | ConvertTo-Json"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    try:
        updates = json.loads(result.stdout)
        
        if isinstance(updates, dict):
            updates = [updates]
        
        return [
            {
                'description': update.get('Description', 'Unknown'),
                'hotfix_id': update.get('HotFixID', 'Unknown'),
                'installed_on': update.get('InstalledOn', None)
            }
            
            for update in updates
        ]
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return []
    
print(get_updates_windows())