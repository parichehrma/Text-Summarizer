from transformers import TrainingArguments, Trainer  
from transformers import DataCollatorForSeq2Seq  
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  
from datasets import load_dataset, load_from_disk 
from textsummarizer.entity import ModelTrainerConfig
import torch  
import os  



class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig): 
        self.config = config  

    
    def train(self):

       
        device = "cuda" if torch.cuda.is_available() else "cpu" 

        
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt) 
        model_t5 = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device) 

        
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_t5) 

        
        dataset_samsum_pt = load_from_disk(self.config.data_path) 

        print(self.config.eval_steps, type(self.config.eval_steps))
        print(self.config.save_steps, type(self.config.save_steps))
        print(self.config.num_train_epochs, type(self.config.num_train_epochs))

        # =========================================================================
        # OPTION 1: CONFIG-BASED (BEST PRACTICE - RECOMMENDED) - USING yaml FILE
        # ==========================================================================
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,  
            num_train_epochs=self.config.num_train_epochs,  
            warmup_steps=self.config.warmup_steps,  
            per_device_train_batch_size=self.config.per_device_train_batch_size,  
            per_device_eval_batch_size=self.config.per_device_train_batch_size,  
            weight_decay=self.config.weight_decay,  
            logging_steps=self.config.logging_steps,  
            #evaluation_strategy=self.config.evaluation_strategy,
            eval_strategy=self.config.evaluation_strategy,  
            # evaluation_strategy=self.config.eval_strategy,
            eval_steps=self.config.eval_steps,  
            save_steps=1e6,  
            gradient_accumulation_steps=self.config.gradient_accumulation_steps  
        )
        # ==========================================================
        # OPTION 2: HARDCODED (ONLY FOR TESTING)
        # ==========================================================
        """
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,  # where model will be saved
            num_train_epochs=1,  # how many times model sees data. model sees dataset only once
            warmup_steps=500,  # slow start for stable training
            per_device_train_batch_size=1,  # training batch size. very small batch (good for weak GPU)
            per_device_eval_batch_size=1,  # evaluation batch size
            weight_decay=0.01,  # prevents overfitting. standard overfitting control
            logging_steps=10,  # show logs every 10 steps
            evaluation_strategy='steps',  # evaluate during training
            eval_steps=500,  # evaluate every 500 steps
            save_steps=1e6,  # save model rarely (almost at end)
            gradient_accumulation_steps=16  # simulate bigger batch using memory efficiency
        )
        """
        
        trainer = Trainer(  
            model=model_t5, 
            args=trainer_args,  
            #tokenizer=tokenizer,  
            data_collator=seq2seq_data_collator,  
            train_dataset=dataset_samsum_pt["test"],  # I use test data for get faster result)
            eval_dataset=dataset_samsum_pt["validation"]  
        )

        # start training process
        trainer.train()

        # save trained model
        model_t5.save_pretrained(
            os.path.join(self.config.root_dir, "t5-samsum-model")
        )

        # save tokenizer for later use
        tokenizer.save_pretrained(
            os.path.join(self.config.root_dir, "tokenizer")
        )