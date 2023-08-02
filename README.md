# Python_File_IO

The Python_File_IO project contains a collection of scripts that generate and analyze log files. The project has three main Python scripts:

1. `main.py`: This is the main script that coordinates the other scripts. It first generates a log file with log entries and then analyzes the created log file.

2. `file_creation.py`: This script generates a log file with a specified number of log entries. Each log entry is generated randomly from a list of log levels and messages.

3. `analyze_file.py`: This script analyzes a given log file. It counts the number of entries for each log level and identifies all the entries that contain the word "ERROR" or "error". The results are printed to the console.

## How to Run the Project

To run the project, navigate to the project directory and run the `main.py` script:

```bash
python main.py