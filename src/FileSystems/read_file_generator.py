from datetime import datetime
import pandas as pd

def read_large_file(file_path):
    """
    Generator to read a large file lazily, one line at a time
    :param file_path: file path
    :return: list
    """
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                line_part = line.strip("\n").split(":")
                timestamp_str = f"{line_part[2]}:{line_part[3]}:{line_part[4]}"
                date_time = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            yield 'ERROR', date_time


file_path = "./input/sample_log.txt"
gen = read_large_file(file_path=file_path)

df = pd.DataFrame()
for i in gen:
    df = pd.DataFrame(gen, columns=["log_type","datetime"])

print(df.to_string(index=False))

csv_df = df.to_csv(index=False, path_or_buf='./output/logs_output.csv')


