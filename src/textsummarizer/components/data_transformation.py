import os
from textsummarizer.logging import logger
from transformers import AutoTokenizer 
from datasets import load_dataset, load_from_disk
from textsummarizer.entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, config):
        self.config = config

        self.tokenizer = AutoTokenizer.from_pretrained(
            config.tokenizer_name,
            use_fast=False

        )

    def convert_examples_to_features(self, example_batch):

        # Tokenize dialogue
        input_encodings = self.tokenizer(
            example_batch['dialogue'], # Converts input conversation into tokens.
            max_length=1024, 
            truncation=True,
            padding='max_length'
        )

        # Tokenize summary
        target_encodings = self.tokenizer(
            text_target=example_batch['summary'], # Converts target summary into labels.
            max_length=128,
            truncation=True,
            padding='max_length' # Makes all sequences same length.Needed for batching during training.
        )

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def convert(self):

        print("Loading dataset...")

        dataset_samsum = load_from_disk(
            self.config.data_path
        )

        print("Transforming dataset...")

        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features,
            batched=True
        )

        print("Saving transformed dataset...")

        dataset_samsum_pt.save_to_disk(
            self.config.root_dir
        )

        print("Transformation completed successfully.")