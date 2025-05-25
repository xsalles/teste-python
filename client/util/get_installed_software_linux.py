import subprocess

def get_installed_software_linux():
    try:
        result = subprocess.run(
            ["dpkg-query", "-W", "-f='${Package} ${Version}\n'"],
            capture_output=True,
            text=True,
        )
        
        packages = []
        
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                package = {
                    "name": parts[0].strip("'"),
                    "version": parts[1].strip("'"),
                }
                packages.append(package)
        return packages
    except Exception as e:
        print(f"Error retrieving installed software: {e}")
        return []