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

mt_art = ModelTrainerArtifacts(
    model_path=r"C:\Users\DYAVADI\Desktop\Project\Speech-To-Text\artifacts\06_28_2024_16_10_05\model_trainer_artifact\saved_model/",
    model_loss=0.6
)

me_ins = ModelEvaluation(ModelEvaluationConfig, mt_art)

me_art = me_ins.initiate_model_evaluation()

mp_ins=ModelPusher(ModelPusherConfig,me_art)

mp_art=mp_ins.initiate_model_pusher() 






