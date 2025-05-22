import psutil

def get_ram_usage():
    try:
        ram = psutil.virtual_memory()
        
        percent_used = int(ram.percent)

        return percent_used
    except Exception as e:
        print(f"Error getting RAM usage: {e}")
        return None