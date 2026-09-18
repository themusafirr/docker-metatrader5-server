import time
import subprocess
import datetime

CONTAINER = "hermes_pepperstone_mt5"

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        return res.stdout.strip()
    except Exception as e:
        return str(e)

def is_mt5_running():
    out = run_cmd(f"docker exec {CONTAINER} pgrep -f terminal64.exe")
    return bool(out)

def restart_mt5():
    print(f"[{datetime.datetime.now()}] MT5 not running! Restarting with C:\Program Files\MetaTrader 5\startup.ini...")
    cmd = f'docker exec -d {CONTAINER} env DISPLAY=:1 WINEPREFIX=/config/.wine su -c "wine \\"/config/.wine/drive_c/Program Files/MetaTrader 5/terminal64.exe\\" /config:C:\Program Files\MetaTrader 5\startup.ini" abc'
    run_cmd(cmd)
    time.sleep(15)
    # Enable algo trading
    enable_algo()

def is_algo_enabled():
    date_str = datetime.datetime.now().strftime("%Y%m%d")
    cmd = f'docker exec {CONTAINER} bash -c "tail -n 15 \\"/config/.wine/drive_c/Program Files/MetaTrader 5/logs/{date_str}.log\\""'
    out = run_cmd(cmd)
    lines = [line.strip() for line in out.splitlines() if "automated trading is" in line]
    if lines:
        last_state = lines[-1]
        if "enabled" in last_state:
            return True
        elif "disabled" in last_state:
            return False
    return True # default assume ok if not logged yet

def enable_algo():
    print(f"[{datetime.datetime.now()}] Toggling Algo Trading to ENABLED...")
    cmd = f'docker exec {CONTAINER} bash -c "xdotool windowactivate 16777217; sleep 1; xdotool key --clearmodifiers ctrl+e"'
    run_cmd(cmd)

def main():
    print(f"[{datetime.datetime.now()}] 24/7 MT5 Watchdog started.")
    while True:
        try:
            if not is_mt5_running():
                restart_mt5()
            else:
                if not is_algo_enabled():
                    print(f"[{datetime.datetime.now()}] Algo trading detected DISABLED. Enabling...")
                    enable_algo()
        except Exception as e:
            print(f"Watchdog error: {e}")
        time.sleep(30)

if __name__ == "__main__":
    main()