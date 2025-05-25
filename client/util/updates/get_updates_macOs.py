import subprocess
import json
from datetime import datetime

def get_updates_mac():
    try:
        result = subprocess.run(
            ["system_profiler", "SPInstallHistoryDataType", "-json"],
            capture_output=True, text=True
        )
        data = json.loads(result.stdout)
        updates = data.get("SPInstallHistoryDataType", [])
        formatted_updates = []
        for u in updates:
            # Example install_date: '2024-05-14T10:15:42Z'
            install_date = u.get("install_date")
            try:
                installed_on = datetime.fromisoformat(install_date.replace("Z", "+00:00")).isoformat() if install_date else None
            except Exception:
                installed_on = None
            formatted_updates.append({
                "description": u.get("_name"),
                "hotfix_id": u.get("version"),
                "installed_on": installed_on
            })
        return formatted_updates
    except Exception as e:
        print(f"Error parsing macOS updates: {e}")
        return []