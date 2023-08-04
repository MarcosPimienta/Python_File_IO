
from pathlib import Path


def analyze_logs(file_path: Path):
    try:
        with open(file_path, 'r') as file:
            log_dict = {}
            error_logs = []

            for line in file.readlines():
                parts = line.split(" - ")
                log_level = parts[1]

                if log_level in log_dict:
                    log_dict[log_level] += 1
                else:
                    log_dict[log_level] = 1

                if "error" in log_level.lower():
                    error_logs.append(line)

        # Print out the results
        print("Log levels count:")
        for level, count in log_dict.items():
            print(f"{level}: {count}")

        print("\nError logs:")
        for log in error_logs:
            print(log)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
