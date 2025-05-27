import psutil

def get_network_info():
    try:
        net_if_addrs = psutil.net_if_addrs()
        for interface, addresses in net_if_addrs.items():
            for addr in addresses:
                if addr.family == psutil.AF_INET:  # IPv4
                    return {
                        "name": interface,
                        "ip_address": addr.address,
                        "mac_address": addr.address if addr.family == psutil.AF_LINK else "Unknown"
                    }
        return {"name": "Unknown", "ip_address": "0.0.0.0", "mac_address": "Unknown"}
    except Exception as e:
        print(f"Error getting Network info: {e}")
        return {"name": "Unknown", "ip_address": "0.0.0.0", "mac_address": "Unknown"}