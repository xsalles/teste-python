import platform
import subprocess

def get_bios_info():
    try:
        os_name = platform.system().lower()
        if os_name == "windows":
            ps_cmd = (
                "Get-CimInstance -ClassName Win32_BIOS | "
                "Select-Object -Property SMBIOSBIOSVersion, ReleaseDate | "
                "ForEach-Object { $_.SMBIOSBIOSVersion + ';' + $_.ReleaseDate }"
            )
            output = subprocess.check_output(
                ["powershell", "-Command", ps_cmd],
                shell=False
            ).decode().strip()

            if ";" in output:
                version, release_date_raw = output.split(";")
                release_date_raw = release_date_raw.strip()
                
                release_date = release_date_raw.split()[0] if " " in release_date_raw else release_date_raw
            else:
                version = "Unknown"
                release_date = "Unknown"

        elif os_name == "linux":
            with open("/sys/class/dmi/id/bios_version") as f:
                version = f.read().strip()
            with open("/sys/class/dmi/id/bios_date") as f:
                release_date = f.read().strip()

        elif os_name == "darwin":
            output = subprocess.check_output(
                "system_profiler SPHardwareDataType | grep 'SMC Version'",
                shell=True
            ).decode()
            version = output.split(":")[1].strip() if ":" in output else "Unknown"
            release_date = "Unknown"

        else:
            version = "Unknown"
            release_date = "Unknown"

        return {"version": version, "release_date": release_date}

    except Exception as e:
        print(f"Error getting BIOS info: {e}")
        return {"version": "Unknown", "release_date": "Unknown"}

print(get_bios_info())
