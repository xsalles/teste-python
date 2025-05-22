import platform
import socket
from system.os import get_serial_number
from manufacturer.manufacturer import get_manufacturer
from model.model import get_model
from location.location import get_location
from ram.ram import get_ram_usage
from disk.disk import get_disk_info

hostname = socket.gethostname()
serie_number = get_serial_number()
manufacturer = get_manufacturer()
model = get_model()
location = get_location()
os = platform.system()
os_version = platform.version()
ram = get_ram_usage()
disk = get_disk_info()


def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "serie_number": serie_number,
        "equipament_name": f"{manufacturer} {model}",
        "ram_memory": ram,
        "os": os,
        "os_version": os_version,
        "disk": disk,
        "model": model,
        "manufacturer": manufacturer,
        "location": location,
    }