from scripts.extract import fetch_data
from scripts.transform import clean_data
from scripts.load import upload_to_database
import logging

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    logging.info("Extracting data...")
    raw_data = fetch_data()

    logging.info("Transforming data...")
    clean_data = clean_data(raw_data)

    logging.info("Loading data into database...")
    upload_to_database(clean_data)

    logging.info("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
