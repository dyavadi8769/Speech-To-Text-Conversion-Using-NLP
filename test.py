from STT.entity.config_entity import DataIngestionConfig, DataPreprocessingConfig, ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig
from STT.components.data_ingestion import DataIngestion
from STT.components.data_preprocessing import DataPreprocessing
from STT.components.model_trainer import ModelTrainer
from STT.entity.artifact_entity import ModelTrainerArtifacts
from STT.components.model_evaluation import ModelEvaluation
from STT.components.model_pusher import ModelPusher

from STT.pipeline.prediction_pipeline import Prediction




di_ins=DataIngestion(DataIngestionConfig)
di_art=di_ins.initiate_data_ingestion()
dp_ins=DataPreprocessing(DataPreprocessingConfig, di_art)
dp_art=dp_ins.initiate_data_preprocessing()
mt_ins=ModelTrainer(dp_art,ModelTrainerConfig)
mt_art=mt_ins.initiate_model_trainer()







