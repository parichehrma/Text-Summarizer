from textsummarizer.config.configuration import ConfigurationManager # Import ConfigurationManager to load paths/settings from config.yaml
from transformers import AutoTokenizer # Import tokenizer loader from Hugging Face
from transformers import pipeline # Import Hugging Face pipeline for easy inference/prediction



# This class handles prediction/summarization for new user input
class PredictionPipeline:

    # Initialize prediction pipeline
    def __init__(self):
        # Load model evaluation configuration (model path, tokenizer path, etc.)
        self.config = ConfigurationManager().get_model_evaluation_config()


    # Function to generate summary from input text
    def predict(self, text):

        # Load tokenizer from saved tokenizer path
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        # Generation settings for summarization
        gen_kwargs = {
            "length_penalty": 0.8,  # controls summary length (Less than 1 → shorter summaries, Greater than 1 → longer summaries)
            "num_beams": 8,         # beam search for better summaries (8 beams means 8 candidate summaries are generated and the best one is chosen)
            "max_length": 128       # maximum summary length(length of output summary- default is 128)
        }

        # Create summarization pipeline using trained model + tokenizer
        pipe = pipeline(
            "summarization",
            model=self.config.model_path,
            tokenizer=tokenizer
        )

        # Print original input text
        print("Dialogue:")
        print(text)

        # Generate summary using the model
        output = pipe(text, **gen_kwargs)[0]["summary_text"] # The pipeline returns a list of dictionaries, where each dictionary contains the generated summary under the key "summary_text". Since we are summarizing one input text, we access the first element of the list (index 0) and then get the summary text from the dictionary.

        # Print generated summary
        print("\nModel Summary:")
        print(output)

        # Return generated summary
        return output