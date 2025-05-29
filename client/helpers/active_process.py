import psutil

def get_active_processes():
    process_info = []
    for proc in psutil.process_iter(['pid', 'name']):
        process_info.append({'pid': proc.info['pid'], 'name': proc.info['name']})
    return process_info