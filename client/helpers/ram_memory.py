import psutil

def get_ram_info():
    try:
        virtual_memory = psutil.virtual_memory()
        total = round(virtual_memory.total / (1024 ** 3), 2)
        usage_percent = virtual_memory.percent

        return { "name": "Memória Ram", 
                 "total": f"{total} GB", 
                 "usage_percent": f"{usage_percent}%" }
    except Exception as e:
        print(f"Error retrieving RAM information: {e}")
        return { "name": "Memória Ram", "total": 0, "usage_percent": 0 }
    
