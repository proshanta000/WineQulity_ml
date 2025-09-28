import os
from pathlib import Path
import zipfile
from WineMl import logger
from WineMl.utils.common import get_size
import requests
from tqdm import tqdm

from WineMl.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        # The file will only be download if it dosn't already exist
        if not os.path.exists(self.config.local_data_file):
            logger.info("Starting file download...")

            # ---- START: Progress Bar IMplementation ----
            url = self.config.source_URL
            local_filename = self.config.local_data_file


            # 1. Initiate the request with streming enabled
            response = requests.get(url, stream=True)
            response.raise_for_status() #Checl for bad status

            # 2. Get the total file size(Content-lenth)
            total_size_in_bytes = int(response.headers.get('content-length', 0))
            block_size = 1024 # 1 kilobyte


            # 3. use tqdm to track progress
            progress_bar = tqdm(
                total=total_size_in_bytes,
                unit='iB',
                unit_scale=True,
                desc = local_filename
            )

            # 4. write to  file and update the progress bar
            with open(local_filename, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)

            progress_bar.close()
            # ------ END: Progress bar Implementation ---

            # Check if download was complete (optional integrity check)
            if total_size_in_bytes !=0 and progress_bar.n != total_size_in_bytes:
                logger.warning("Download integrity check failed. File Size mismatch.")


            logger.info(f"{local_filename} downloaded successfully!")

        else: 
            # Original logic for file already existing
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
    

    def extract_zip_file(self):

        """
        Extracts a zip file into a specified directory.
        
        This method takes the path of a downloaded zip file and extracts its
        contents to the designated `unzip_dir`. It ensures the destination
        directory exists before extraction.
        """
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        
        logger.info(f"Zip file extracted to {unzip_path}")
