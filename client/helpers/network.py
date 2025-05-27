import psutil
import socket

def get_network_info():
    try:
        net_if_addrs = psutil.net_if_addrs()
        for interface, addresses in net_if_addrs.items():
            ip_address = None
            mac_address = None
            for addr in addresses:
                if addr.family == socket.AF_INET:  # IPv4
                    ip_address = addr.address
                # AF_LINK for macOS/BSD, AF_PACKET for Linux
                if hasattr(socket, "AF_PACKET") and addr.family == socket.AF_PACKET:
                    mac_address = addr.address
                elif hasattr(psutil, "AF_LINK") and addr.family == psutil.AF_LINK:
                    mac_address = addr.address
            if ip_address:
                return {
                    "name": interface,
                    "ip_address": ip_address,
                    "mac_address": mac_address or "Unknown"
                }
        return {"name": "Unknown", "ip_address": "0.0.0.0", "mac_address": "Unknown"}
    except Exception as e:
        print(f"Error getting Network info: {e}")
        return {"name": "Unknown", "ip_address": "0.0.0.0", "mac_address": "Unknown"}

