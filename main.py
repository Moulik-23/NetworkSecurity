from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.expection.expection import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainnigPipelineConfig
import sys


if __name__=="__main__":
    try:
        trainnigpipelineconfig=TrainnigPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainnigpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
