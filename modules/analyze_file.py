
from pathlib import Path


def get_log_level(line):
    return line.split(" - ")[1]


def is_error_line(line):
    return "error" in get_log_level(line).lower()


def analyze_logs(file_path: Path):
    try:
        with open(file_path, 'r') as file:
            log_dict = {}
            lines = file.readlines()

            log_levels = list(map(get_log_level, lines))
            error_logs = list(filter(is_error_line, lines))

            for log_level in log_levels:
                if log_level in log_dict:
                    log_dict[log_level] += 1
                else:
                    log_dict[log_level] = 1

        # Print out the results
        print("Log levels count:")
        for level, count in log_dict.items():
            print(f"{level}: {count}")

        print("\nError logs:")
        for log in error_logs:
            print(log)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
