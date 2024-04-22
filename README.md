# Log Analysis and Monitoring Script v0.5

This project is a log analysis and monitoring script that helps analyze and monitor log files. <br>
This version of the script focuses on log monitoring capabilities. It allows you to specify a log file and helps in live monitoring the log data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/BANZOM/Log-Analysis-and-Monitoring-Script.git
    ```

2. Change to the project directory:

    ```bash
    cd Log-Analysis-and-Monitoring-Script
    ```



## Usage

1. Run the script:

    ```bash
    python log_monitor.py /path/to/log/file.log
    ```

2. Follow the prompts to specify the log file and the analysis options.


## Generating Logs

To generate logs for testing purposes, you can use the `generate_logs.py` file included in the project. 

1. Run the script:

    ```bash
    # To generate a specific number of logs
    python generate_logs.py <number_of_logs>
    ```

    or

    ```bash
    # To generate infinite logs
    python generate_logs.py
    ```

2. Follow the prompts to specify the log file name and the number of logs to generate.