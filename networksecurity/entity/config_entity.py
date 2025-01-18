from datetime import datetime
import os
from networksecurity.constant import trainning_pipeline

print(trainning_pipeline.PIPELINE_NAME)
print(trainning_pipeline.ARTIFACT_DIR)

class TrainnigPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name=trainning_pipeline.PIPELINE_NAME
        self.artifact_name=trainning_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp: str=timestamp

class DataIngestionConfig:
    def __init__(self,trainning_pipeline_config:TrainnigPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            trainning_pipeline_config.artifact_dir,trainning_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, trainning_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,trainning_pipeline.FILE_NAME
        )
        self.trainning_file_path: str = os.path.join(
            self.data_ingestion_dir, trainning_pipeline.DATA_INGESTION_INGESTED_DIR, trainning_pipeline.TRAIN_FILE_NAME
        )
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir, trainning_pipeline.DATA_INGESTION_INGESTED_DIR, trainning_pipeline.TEST_FILE_NAME
        )
        self.train_test_split_ratio: float  = trainning_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name : str = trainning_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = trainning_pipeline.DATA_INGESTION_DATABASE_NAME