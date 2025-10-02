import os
from WineMl import logger
from WineMl.pipeline.stage_01_data_ingestion_pipline import DataIngestionPipeline
from WineMl.pipeline.stage_02_data_validation_pipline import DataValidationgPipeline
from WineMl.pipeline.stage_03_data_transformation import DataTransformationPipeline
from WineMl.pipeline.stage_04_model_trainer_pipline import ModelTrainerPipeline
from WineMl.pipeline.stage_05_model_evaluation_pipline import ModelEvaluationPipeline


os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/proshanta000/WineQulity_ml.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="proshanta000"
os.environ["MLFLOW_TRACKING_PASSWORD"]="1d2afccec4c7566b7e8d9ed3f00a41e1e86ae8fd"

STAGE_NAME = "Data Ingestion Stage"


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>  stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Data Validation Stage"


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>  stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataValidationgPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Data Transformation Stage"


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>  stage {STAGE_NAME} started <<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "Model Trainer Stage"


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>  stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Evaluation Stage"


if __name__=='__main__':
    try:
        logger.info(f"**********************")
        logger.info(f">>>>>>>>>>  stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nX============X")
    except Exception as e:
        logger.exception(e)
        raise e