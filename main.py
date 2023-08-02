from modules import file_creation, analyze_file
from pathlib import Path


def main():

    file_creation.generate_logs(Path("logs/mylogfile.log"), 1000)

    analyze_file.analyze_logs(Path("logs/mylogfile.log"))


if __name__ == "__main__":
    main()
