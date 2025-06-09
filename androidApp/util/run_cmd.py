import subprocess

def run_cmd(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True).decode().strip()
        return output
    except Exception as e:
        return f"Error: {e}"