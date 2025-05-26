import platform
import subprocess

def get_disk_type(device):
    try:
        os_name = platform.system().lower()
        if os_name == "windows":
            command = f'powershell -Command "Get-PhysicalDisk | Where-Object {{$_.DeviceID -eq {device[-1]}}} | Select-Object MediaType"'
            output = subprocess.check_output(command, shell=True).decode().strip()
            if "SSD" in output:
                return "SSD"
            elif "HDD" in output:
                return "HDD"
        elif os_name == "linux":

            rotational_path = f"/sys/block/{device.split('/')[-1]}/queue/rotational"
            with open(rotational_path, "r") as f:
                rotational = f.read().strip()
                return "SSD" if rotational == "0" else "HDD"
        elif os_name == "darwin":

            command = f"diskutil info {device} | grep 'Solid State'"
            output = subprocess.check_output(command, shell=True).decode().strip()
            return "SSD" if "Yes" in output else "HDD"
        return "Unknown"
    except Exception as e:
        print(f"Error determining disk type for {device}: {e}")
        return "Unknown"
    
