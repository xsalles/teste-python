import platform;

def get_serial_number():

    system = platform.system()

    try:
        if system == "Windows":
            try:
                import subprocess
                output = subprocess.check_output('powershell -Command "Get-WmiObject win32_bios | Select-Object -ExpandProperty SerialNumber"', shell=True)
                serial_number = output.decode().strip()
                if serial_number:
                    return serial_number
            except Exception:
                pass
        elif system == "Linux":
            import subprocess
            with open("/sys/class/dmi/id/product_serial") as f:
                serial_number = f.read().strip()
        elif system == "Darwin":
            import subprocess
            output = subprocess.check_output("system_profiler SPHardwareDataType | grep Serial", shell=True)
        else:
            serial_number = "Unsupported OS"
            serial_number = None
        return serial_number
    except Exception as e:
        print(f"Error getting serial number: {e}")
        return None