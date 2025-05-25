import subprocess
from datetime import datetime

def get_updates_linux():
    updates = []
    try:
        # Try parsing dpkg logs (Debian/Ubuntu)
        result = subprocess.run(
            ["grep", "install ", "/var/log/dpkg.log"],
            capture_output=True, text=True
        )
        for line in result.stdout.splitlines():
            # Example line: 2024-05-14  10:15:42 install python3:amd64 3.8.2-0ubuntu2
            parts = line.split()
            if len(parts) >= 6:
                date_str = f"{parts[0]} {parts[1]}"
                try:
                    installed_on = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").isoformat()
                except Exception:
                    installed_on = None
                updates.append({
                    "description": parts[4],  # package name
                    "hotfix_id": None,
                    "installed_on": installed_on
                })
        return updates
    except Exception:
        # Try rpm logs (RedHat/Fedora)
        try:
            result = subprocess.run(
                ["rpm", "-qa", "--last"],
                capture_output=True, text=True
            )
            for line in result.stdout.splitlines():
                # Example: bash-5.0.17-2.fc32.x86_64    Tue 14 May 2024 10:15:42 AM UTC
                if line.strip():
                    pkg, *date_parts = line.split()
                    date_str = " ".join(date_parts)
                    try:
                        installed_on = datetime.strptime(date_str, "%a %d %b %Y %I:%M:%S %p %Z").isoformat()
                    except Exception:
                        installed_on = None
                    updates.append({
                        "description": pkg,
                        "hotfix_id": None,
                        "installed_on": installed_on
                    })
            return updates
        except Exception as e:
            print(f"Error parsing updates: {e}")
            return []