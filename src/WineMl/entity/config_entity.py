from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for the data ingestion stage.
    """
    root_dir: Path  # Root directory where data ingestion artifacts are stored
    source_URL: str  # URL to the source data file
    local_data_file: Path  # Local path to save the downloaded data file
    unzip_dir: Path  # Directory where the data will be unzipped


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict




@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path