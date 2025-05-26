import psutil
import platform

def get_cpu():
    try:
        cpu_name = platform.processor() or "Unknown CPU"
        cores = psutil.cpu_count(logical=True)
        usage_percent = psutil.cpu_percent(interval=1)

        return { "cpu_name": cpu_name, "cores": cores, "usage_percent": usage_percent }
    except Exception as e:
        print(f"Error retrieving CPU information: {e}")
        return { "cpu_name": "Unknown", "cores": 0, "usage_percent": 0 }
    
