import os
from WineMl import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from WineMl.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

    def train_test_spliting(self):
        data = pd.read_csv("artifacts/data_ingestion/winequality-red.csv")

        #split the data into traning and test sets (0.75, 0.25)
        train, test = train_test_split(data, test_size=0.25)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index =False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index =False)


        logger.info("split data into traning and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
