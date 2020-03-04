import kaggle
import os
import logging
import zipfile

DATASET_NAME = "itamarmushkin/israeli-elections-2015-2013"

def fetch_dataset():
	kaggle.api.dataset_download_files(DATASET_NAME, path="./data")
	with zipfile.ZipFile("./data/israeli-elections-2015-2013.zip", 'r') as zip_ref:
		zip_ref.extractall("./data")


def main():
	logging.info("Fetching dataset...")
	fetch_dataset()
