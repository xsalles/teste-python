import platform
import subprocess

def get_model():
    os = platform.system()

    try:
        if os == 'Windows':
            try:
                output = subprocess.check_output(
                    'powershell -Command "Get-WmiObject Win32_ComputerSystem | Select-Object -ExpandProperty Model"',
                    shell=True
                )
                model = output.decode().strip()
                if model:
                    return model
            except Exception:
                pass
        elif os == "Linux":
            try:
                with open("/sys/class/dmi/id/product_name") as f:
                    model = f.read().strip()
                if model:
                    return model
            except Exception:
                pass
        elif os == "Darwin":
            try:
                output = subprocess.check_output("system_profiler SPHardwareDataType | grep 'Model Name'", shell=True)
                model = output.decode().split(":")[1].strip()
                if model:
                    return model
            except Exception:
                pass
    except Exception as e:
        print(f"Error getting model: {e}")
        return None