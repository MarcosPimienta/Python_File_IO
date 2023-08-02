import datetime
import random
from pathlib import Path


def generate_logs(log_file: Path, number_logs: int):

    log_levels = ['INFO', 'WARNING', 'DEBUG', 'ERROR', 'CRITICAL']
    log_messages = ['System started', 'Process completed successfully',
                    'An error occurred']

    path = Path('logs')

    if not path.exists():
        print(f'Creating directory {str(path)}...')
        path.mkdir(parents=True, exist_ok=True)

    with log_file.open('a', encoding="utf-8") as file:
        for _ in range(number_logs):
            level = random.choice(log_levels)
            ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            msg = random.choice(log_messages)

            line_message = ts + " - " + level + " - " + msg + '\n'
            file.write(line_message)
