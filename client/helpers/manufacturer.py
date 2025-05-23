import platform
import subprocess

def get_manufacturer():
    os = platform.system()

    try:
        if os == 'Windows':
            try:
                output = subprocess.check_output(
                    'powershell -Command "Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty Manufacturer"',
                    shell=True
                )
                manufacturer = output.decode().strip()
                if manufacturer:
                    return manufacturer
            except Exception:
                pass
        elif os == "Linux":
            try:
                with open("/sys/class/dmi/id/sys_vendor") as f:
                    manufacturer = f.read().strip()
                if manufacturer:
                    return manufacturer
            except Exception:
                pass
        elif os == "Darwin":
            try:
                output = subprocess.check_output("system_profiler SPHardwareDataType | grep 'Manufacturer'", shell=True)
                manufacturer = output.decode().split(":")[1].strip()
                if manufacturer:
                    return manufacturer
            except Exception:
                pass
        return None
    except Exception as e:
        print(f"Error getting manufacturer: {e}")
        return None