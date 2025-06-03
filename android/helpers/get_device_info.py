from android.util.run_cmd import run_cmd

def get_device_info():
    return {
        "manufacturer": run_cmd("getprop ro.product.manufacturer"),
        "model": run_cmd("getprop ro.product.model"),
        "os_version": run_cmd("getprop ro.build.version.release"),
        "apps": run_cmd("pm list packages"),
        "network": run_cmd("ip addr"),
        "storage": run_cmd("df -h /storage/emulated"),
        "users": run_cmd("pm list users"),
        "timestamp": run_cmd("date")
    }