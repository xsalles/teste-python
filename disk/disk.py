import platform
import psutil
import subprocess

def get_disk_info():
    try:
        disk = psutil.disk_usage('/')
        percent_used = int(disk.percent)

        return percent_used
        
    except Exception as e:
        print(f"Error getting disk info: {e}")
        return None