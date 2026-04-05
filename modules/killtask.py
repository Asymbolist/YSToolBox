import subprocess

def kill_all_not_responding():
    try:
        subprocess.run("taskkill /f /fi \"status eq not responding\"", shell=True)
        return 1
    except:
        return 0