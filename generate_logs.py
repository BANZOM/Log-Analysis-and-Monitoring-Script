import time
import random

class GenerateLogs:
    """
    A class for generating logs.
    This class provides generate logs to test the log analysis and monitoring script.

    Attributes:
        levels: A list of log levels.
        messages: A list of log messages.
        log_file: A string representing the log file path.

    Methods:
        generate_logs: Generates logs based on specified parameters.
        generate_log_entry: Generates a log entry.
    """
    def __init__(self):
        self.levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING', 'CRITICAL', 'FATAL']
        self.messages = [
            "Application started",
            "Connection timeout",
            "Database connection failed",
            "User logged in",
            "Processing data",
            "Data saved successfully",
            "Low disk space",
            "Server crashed",
            "Server restarted",
            "Application stopped",
            "Invalid request",
            "User logged out",
            "Data processing failed",
        ]
        self.log_file = 'sample.log'

    
