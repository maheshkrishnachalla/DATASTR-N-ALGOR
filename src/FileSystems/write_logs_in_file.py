# write the logs into file

log_file_path = "sample_log.txt"

def write_logs(log_file_path):
    # sample logs
    sample_logs = [
        "1234567:ERROR:2025-08-11 12:12:20:this is a exception",
        "1234568:ERROR:2025-08-11 12:14:10:database connection failed",
        "1234569:INFO:2025-08-11 12:15:00:system running normally",
        "1234570:ERROR:2025-08-11 12:16:45:file not found",
        "1234571:ERROR:2025-08-11 12:18:05:timeout while connecting to API",
        "1234580:INFO:2025-08-11 12:30:00:system running normally",
        "1234585:INFO:2025-08-11 12:40:00:system running normally",
        "1234589:INFO:2025-08-11 12:50:00:system running normally"
    ]

    # write to file
    with open(log_file_path, "w") as file:
        for log in sample_logs:
            file.write(log + "\n")
    print(f"sample log file {log_file_path} created successfully")

write_logs(log_file_path=log_file_path)