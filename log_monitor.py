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
        with open(self.log_file, 'r') as f:
            while True:
                new_log = f.readline()
                if new_log:
                    print(new_log)
                else:
                    time.sleep(1)


if __name__ == "__main__":
    log_monitor = LogMonitor()
    try:
        log_monitor.monitor_logs()
    except KeyboardInterrupt:
        print("Exiting log monitor")
