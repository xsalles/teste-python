import subprocess
import json

def get_installed_software_mac():
    result = subprocess.run([
        'system_profiler',
        'SPApplicationsDataType',
        '-json'
    ], capture_output=True, text=True)

    try:
        data = json.loads(result.stdout)
        apps = data['SPApplicationsDataType']
        
        return [
            {
                'name': app.get('_name', 'Unknown'),
                'version': app.get('version', 'Unknown'),
                'installation_date': app.get('install_date', None)
            }
            for app in apps
        ]
    except Exception as e:
        print(f"Error retrieving installed software: {e}")
        return []
        