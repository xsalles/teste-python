import psutil
import socket

def get_network_info():
    try:
        net_if_addrs = psutil.net_if_addrs()
        for interface, addresses in net_if_addrs.items():
            ip = None
            mac = None
            for addr in addresses:
                if addr.family == socket.AF_INET:
                    ip = addr.address

                elif hasattr(psutil, "AF_LINK") and addr.family == psutil.AF_LINK:
                    mac = addr.address
                elif addr.family == -1:  
                    mac = addr.address
            if ip and mac:
                return {
                    "name": interface,
                    "ip_address": ip,
                    "mac_address": mac
                }
        return {"name": "Unknown", "ip_address": "0.0.0.0", "mac_address": "Unknown"}
    except Exception as e:
        print(f"Error getting Network info: {e}")
        return {"name": "Unknown", "ip_address": "0.0.0.0", "mac_address": "Unknown"}

print(get_network_info())
