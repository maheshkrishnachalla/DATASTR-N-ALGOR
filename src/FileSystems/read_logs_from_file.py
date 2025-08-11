from datetime import datetime, timedelta

from src.FileSystems.write_logs_in_file import log_file_path

#current time in local time
now = datetime.now()

# define time window (for last 5 mins)
time_window_start = now - timedelta(minutes=5)

error_count = 0

with open(log_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(":")
        if len(parts) >=4 and parts[1] == 'ERROR':
            # extract timestamp part (format : YYYY-MM-DD HH:MM:SS)
            timestamp_str = f"{parts[2]}:{parts[3]}:{parts[4]}"
            try:
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                if time_window_start <= timestamp <= now:
                    error_count += 1
            except ValueError:
                pass #skip line with incorrect format

print(f"Number of errors in the last 5 mins: {error_count}")