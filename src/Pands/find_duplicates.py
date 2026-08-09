import  pandas as pd
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

input_csv = "./inputs/input_data.csv"
cleaned_output_csv = "./outputs/cleaned_output_data.csv"


def process_and_deduplicates(input_csv, cleaned_output_csv):
    try:
        logging.info("Reading csv file: %s",input_csv)
        df = pd.read_csv(input_csv)

        intial_row_count = len(df)
        logging.info("Total rows loaded: %d", intial_row_count)

        duplicates_count = df.duplicated().sum()
        logging.info("Duplicated rows count: %d", duplicates_count)

        cleaned_df = df.drop_duplicates(keep="first")
        final_row_count = len(cleaned_df)
        removed_row_count =   intial_row_count- len(cleaned_df)
        logging.info("Deduplication completed Cleaned df rows: %d (Removed rows: %d)",
                     final_row_count,
                     removed_row_count)

        cleaned_df.to_csv(cleaned_output_csv, index=False)
        logging.info("Successfully loaded Cleaned csv into %s", cleaned_output_csv)

    except FileNotFoundError as e:
        logging.error("Input file not found at path %s", input_csv)

    except Exception as e:
        logging.error("Error occured during processing: %s, ",str(e))


if __name__ == "__main__":
    process_and_deduplicates(input_csv=input_csv, cleaned_output_csv=cleaned_output_csv)

