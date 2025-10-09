


### Code Explanation
#The following Python program provides functionality to:
#1. Monitor currently running processes.
#2. Detect when new applications are launched.
#3. Detect when applications are closed.
#4. Log the launch and close times of detected applications.

### Full Python Program

import psutil
import time
from datetime import datetime, timedelta

def log_event(event_type, process_name, pid, timestamp):
    """Logs the events (launch or close) to the console or a file."""
    log_message = f"[{timestamp}] {event_type}: {process_name} (PID: {pid})"
    print(log_message)
    
    # Optional: Write the event to a log file
    with open("application_monitor_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")

def monitor_processes():
    """Monitor running applications and log launch and close times."""
    known_processes = {}
    """Ignore the system and other applications logs."""
    ignore_processes = ["dllhost.exe","git.exe","AsusSystemAnalysis.exe","ShellHost.exe","conhost.exe","RuntimeBroker.exe","HYPHelper.exe","svchost.exe",
                        "LockApp.ex","ArmouryCrate.UserSessionHelper.exe","WmiPrvSE.exe","FileCoAuth.exe","LockApp.exe","updater.exe","SearchFilterHost.exe",
                        "powershell.exe","msedgewebview2.exe","msedge.exe","mc-extn-browserhost.exe","AsusUpdateChecker.exe","appidcertstorecheck.exe","backgroundTaskHost.exe",
                        "MicrosoftEdgeUpdate.exe","ChsIME.exe","StoreDesktopExtension.exe","AsusUpdate.exe","rundll32.exe"]
    
    print("Monitoring applications. Press Ctrl+C to stop.")
    try:
        while True:
            current_time = datetime.now()
            yesterday_time = current_time - timedelta(days=1)

            current_processes = {proc.pid: proc.info for proc in psutil.process_iter(['pid', 'name', 'create_time'])}
            
            # Detect new processes (launched)
            new_pids = set(current_processes.keys()) - set(known_processes.keys())
            for pid in new_pids:
                process_info = current_processes[pid]
                process_name = process_info.get('name', 'Unknown')
                launch_time = datetime.fromtimestamp(process_info.get('create_time', time.time()))
                if(process_name in ignore_processes): 
                    continue
                if(launch_time > yesterday_time):
                    log_event("LAUNCHED", process_name, pid, launch_time)
                

            # Detect terminated processes (closed)
            closed_pids = set(known_processes.keys()) - set(current_processes.keys())
            for pid in closed_pids:
                process_info = known_processes[pid]
                process_name = process_info.get('name', 'Unknown')
                close_time = current_time
                if(process_name in ignore_processes): 
                    continue
                if(launch_time > yesterday_time) :
                    log_event("CLOSED", process_name, pid, close_time)

            # Update known processes
            known_processes = current_processes
            
            # Sleep for a short period to avoid high CPU usage
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_processes()