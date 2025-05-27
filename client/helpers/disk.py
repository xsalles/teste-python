import psutil
import platform
import subprocess
import re

def get_disk_type(device):
    try:
        os_name = platform.system().lower()
        if os_name == "windows":
            drive_letter = device[0] if ':' in device else device
            ps_cmd = (
                f"$drive = Get-WmiObject Win32_LogicalDisk | Where-Object {{$_.DeviceID -eq '{drive_letter}:'}};"
                f"$partition = Get-WmiObject Win32_LogicalDiskToPartition | Where-Object {{$_.Dependent -like '*{drive_letter}:*'}};"
                f"$diskIndex = ($partition.Antecedent -split 'Disk #')[1] -split ',' | Select-Object -First 1;"
                f"Get-PhysicalDisk | Where-Object {{$_.DeviceID -eq $diskIndex}} | Select-Object MediaType"
            )
            command = ["powershell", "-Command", ps_cmd]
            output = subprocess.check_output(command, shell=False).decode(errors="ignore")
            if "SSD" in output:
                return "SSD"
            elif "HDD" in output:
                return "HDD"
        elif os_name == "linux":
            dev_name = device.split('/')[-1]
            rotational_path = f"/sys/block/{dev_name}/queue/rotational"
            try:
                with open(rotational_path, "r") as f:
                    rotational = f.read().strip()
                    return "SSD" if rotational == "0" else "HDD"
            except Exception:
                return "Unknown"
        elif os_name == "darwin":
            match = re.search(r"(disk\d+)", device)
            if match:
                disk = match.group(1)
                command = ["diskutil", "info", disk]
                output = subprocess.check_output(command, shell=False).decode(errors="ignore")
                for line in output.splitlines():
                    if "Solid State" in line:
                        return "SSD" if "Yes" in line else "HDD"
            return "Unknown"
        return "Unknown"
    except Exception as e:
        print(f"Error determining disk type for {device}: {e}")
        return "Unknown"

def get_disk_info():
    try:
        partitions = psutil.disk_partitions()
        disk_info_list = []
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            total_size = round(usage.total / (1024 ** 3), 2)
            usage_percent = usage.percent
            disk_type = get_disk_type(partition.device)
            disk_info_list.append({
                "name": partition.device,
                "size": f"{total_size}GB",
                "type": disk_type,
                "usage_percent": f"{usage_percent}%"
            })
        return disk_info_list if disk_info_list else [{"name": "Unknown", "size": "0GB", "type": "Unknown", "usage_percent": "0%"}]
    except Exception as e:
        print(f"Error getting Disk info: {e}")
        return [{"name": "Unknown", "size": "0GB", "type": "Unknown", "usage_percent": "0%"}]

print(get_disk_info())