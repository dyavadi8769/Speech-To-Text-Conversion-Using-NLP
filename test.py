from STT.entity.config_entity import DataIngestionConfig
from STT.components.data_ingestion import DataIngestion

di_ins=DataIngestion(DataIngestionConfig)
di_art=di_ins.initiate_data_ingestion()