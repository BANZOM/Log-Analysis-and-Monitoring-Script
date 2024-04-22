import os
import time

class LogMonitor:
    """
    A class to monitor logs

    Attributes:
        log_file: A string representing the log file path.
    
    Methods:
        monitor_logs: Monitors logs for new entries.
    """
    def __init__(self, log_file: str = 'sample.log'):
        self.log_file = log_file
    def monitor_logs(self):
        """
        Monitors logs for new entries.
        """
        try:
            with open(self.log_file, 'r') as f:
                f.seek(0, os.SEEK_END)
                while True:
                    line = f.readline()
                    if line:
                        print(line.rstrip())
                    else:
                        time.sleep(1)
        except FileNotFoundError:
            print(f"Log file '{self.log_file}' not found.")
            return
        except KeyboardInterrupt:
            print("\nLog monitoring stopped.")
            return
        


if __name__ == "__main__":
    log_monitor = LogMonitor()
    log_monitor.monitor_logs()
