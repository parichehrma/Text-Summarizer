from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textsummarizer.logging import logger

# This code runs the data ingestion pipeline:
STAGE_NAME = "Data Ingestion stage"  # Stores the name of the pipeline stage (just for labeling/logging).
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # logs that the data ingestion stage has started.
   data_ingestion = DataIngestionTrainingPipeline() # Creates an object of the pipeline class.
   data_ingestion.main() # Runs the main function (executes data ingestion steps).
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x") # Logs that the stage finished successfully.
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e     