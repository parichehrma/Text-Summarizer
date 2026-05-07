from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

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