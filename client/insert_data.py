from backend.models.model import SystemInfo
from backend.models.location import Location
from backend.models.hardware.disk import Disk
from backend.models.hardware.bios import BIOS
from backend.models.hardware.cpu import CPU
from backend.models.hardware.network import Network
from backend.models.hardware.ram_memory import RamMemory
from backend.models.software.installed_softwares import InstalledSoftware
from backend.models.software.logged_users import LoggedUser
from backend.models.software.updates import Updates
from client.helpers.model import get_model
from client.helpers.bios import get_bios_info
from client.helpers.cpu import get_cpu
from client.helpers.disk import get_disk_info
from client.helpers.location import get_location
from client.helpers.manufacturer import get_manufacturer
from client.helpers.ram_memory import get_ram_info
from client.helpers.network import get_network_info
from client.helpers.logged_users import get_logged_user
from client.helpers.updates import get_updates
from client.helpers.installed_softwares import get_installed_softwares
from client.helpers.local_users import get_local_users
from client.helpers.active_process import get_active_processes
from backend.db_config import db
from backend.models.software.local_users import LocalUsers
from backend.models.software.active_process import ActiveProcess



from datetime import datetime
import platform

def collect_and_insert_device_info():
    # 1. Collect hardware/software info
    hostname = platform.node()
    equipment_name = hostname  # or customize as needed
    model = get_model()
    manufacturer = get_manufacturer()
    os_name = platform.system()
    os_version = platform.version()
    location_str = get_location()  # e.g., "City, State, Country"
    bios_info = get_bios_info()
    cpu_info = get_cpu()
    ram_info = get_ram_info()
    disk_info_list = get_disk_info()
    network_info = get_network_info()
    logged_users = get_logged_user()
    updates = get_updates()
    installed_softwares = get_installed_softwares()
    local_users = get_local_users()
    active_processes = get_active_processes()
    

    # 2. Insert or get related tables
    # BIOS
    bios = BIOS(version=bios_info['version'], release_date=bios_info['release_date'])
    db.session.add(bios)
    db.session.flush()  # get bios.id

    # CPU
    cpu = CPU(name=cpu_info['cpu_name'], cores=cpu_info['cores'], usage_percent=str(cpu_info['usage_percent']))
    db.session.add(cpu)
    db.session.flush()

    # RAM
    ram = RamMemory(
        name=ram_info['name'],
        size=ram_info['total'],
        usage_percent=float(ram_info['usage_percent'].replace('%', '').replace('GB', '').strip()),
    )
    db.session.add(ram)
    db.session.flush()

    # Disk (insert all disks, link first to device)
    disk_objs = []
    for d in disk_info_list:
        disk_obj = Disk(
            name=d['name'],
            size=d['size'],
            type=d['type'],
            usage_percent=d['usage_percent'],
        )
        db.session.add(disk_obj)
        disk_objs.append(disk_obj)
    db.session.flush()

    # Network
    network = Network(
        name=network_info['name'],
        ip_address=network_info['ip_address'],
        mac_address=network_info['mac_address'],
    )
    db.session.add(network)
    db.session.flush()

    # Location (parse city/state/country if possible)
    city, loc, state, *_ = location_str.split(',') if location_str else ("Unknown", "Unknown")
    location = Location(
        city=city.strip(),
        state=state.strip() if state else None,
        loc=loc.strip() if loc else None,
    )
    db.session.add(location)
    db.session.flush()

    # 3. Insert main device
    device = SystemInfo(
        hostname=hostname,
        equipment_name=equipment_name,
        model=model,
        manufacturer=manufacturer,
        os=os_name,
        os_version=os_version,
        location=location_str,
        cpu_id=cpu.id,
        ram_memory_id=ram.id,
        disk_id=disk_objs[0].id if disk_objs else None,
        network_id=network.id,
        bios_id=bios.id,
        running_processes=None,
        active_services=None,
        apps_installed=None
    )
    db.session.add(device)
    db.session.flush()


    # 4. Insert related hardware/software info
    for sw in installed_softwares:
        db.session.add(InstalledSoftware(
            name=sw.get('DisplayName'),
            version=sw.get('DisplayVersion'),
            installation_date=sw.get('InstallDate'),
            device_id = device.id
        ))

    # Updates
    for up in updates:
        db.session.add(Updates(
            description=up.get('description'),
            hotfix_id=up.get('hotfix_id'),
            installed_on=up.get('installed_on'),
            device_id = device.id
        ))

    # Logged Users
    for user in logged_users:
        db.session.add(LoggedUser(
            username=user.get('username'),
            logon_time=user.get('logon_time'),
            device_id = device.id
        ))
        
    for user in local_users:
        db.session.add(LocalUsers(
            username=user['username'],
            device_id=device.id
        ))
    
    for proc in active_processes:
        db.session.add(ActiveProcess(
            pid=proc['pid'],
            name=proc['name'],
            device_id=device.id,
        ))

    db.session.commit()
    print("Device info inserted successfully.")