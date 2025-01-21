from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.expection.expection import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainnigPipelineConfig
from networksecurity.components.data_transformation import DataTransformation
import sys


if __name__=="__main__":
    try:
        trainnigpipelineconfig=TrainnigPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainnigpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("Data Intiation Completed")
        print(dataingestionartifact)
        datavalidationconfig=DataValidationConfig(trainnigpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Intiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation Completed")
        logging.info("Data Transformation Started")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainnigpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")


    except Exception as e:
        raise NetworkSecurityException(e,sys)
