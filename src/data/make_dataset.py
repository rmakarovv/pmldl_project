import os
import zipfile
import gdown
import argparse

def download_data(url, output_path):
    """
    Downloads data from the given URL and saves it to the specified output path.

    Parameters:
    - url (str): The URL of the data file.
    - output_path (str): The path where the downloaded data should be saved.
    """
    if not os.path.exists(output_path):
        gdown.download(url, output_path, quiet=False)

def extract_data(zip_path, extract_path):
    """
    Extracts data from the given zip file to the specified extraction path.

    Parameters:
    - zip_path (str): The path to the zip file.
    - extract_path (str): The path where the data should be extracted.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def main():
    parser = argparse.ArgumentParser(description='Download and extract raw data for the project.')
    parser.add_argument('--data-url', type=str, default="https://drive.google.com/uc?id=13BRcVe9gkiwTFInNi5HBTUYX57NCUL4j",
                        help='URL to download the data file')
    parser.add_argument('--output-path', type=str, default="pmldl_project/data/raw/nlp-getting-started.zip",
                        help='Path to save the downloaded data file')
    parser.add_argument('--extract-path', type=str, default="pmldl_project/data/interim/",
                        help='Path to extract the data to')

    args = parser.parse_args()

    # Download data
    download_data(args.data_url, args.output_path)

    # Extract data
    extract_data(args.output_path, args.extract_path)

if __name__ == "__main__":
    main()
