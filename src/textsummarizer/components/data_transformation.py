import os
from textsummarizer.logging import logger
from transformers import AutoTokenizer 
from datasets import load_dataset, load_from_disk
from textsummarizer.entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, config):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):

        input_texts = ["summarize: " + text for text in example_batch['dialogue']]

        input_encodings = self.tokenizer(
            input_texts,
            max_length=1024,
            truncation=True,
            padding='max_length'
        )

        target_encodings = self.tokenizer(
            text_target=example_batch['summary'],
            max_length=128,
            truncation=True,
            padding='max_length'
        )

        labels = target_encodings["input_ids"]

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': labels
        }

    def convert(self):

        print("Loading dataset...")

        dataset_samsum = load_from_disk(self.config.data_path)

        print("Transforming dataset...")

        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features,
            batched=True
        )

        print("Saving transformed dataset...")

        dataset_samsum_pt.save_to_disk(self.config.root_dir)

        print("Transformation completed successfully.")