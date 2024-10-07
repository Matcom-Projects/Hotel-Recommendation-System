import torch
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
import re
import string
from typing import Union, List

<<<<<<< Updated upstream

tokenizer = BertTokenizer.from_pretrained("model_Hotel-Recommendation")


model = BertForSequenceClassification.from_pretrained(
    "model_Hotel-Recommendation",
    num_labels=3,
    output_attentions=False,
    output_hidden_states=False
)
# Change fine_tuned_model to cpu
model.to("cpu")



def sentiment_analysis(comment):
    # Tokenizar el comentario
    inputs = tokenizer(comment, return_tensors='pt', padding=True, truncation=True, max_length=512)

    # Mover los tensores al dispositivo adecuado (CPU o GPU)
    device = torch.device("cpu")
    model.to(device)
    inputs = {key: val.to(device) for key, val in inputs.items()}

    with torch.no_grad():  # Desactivar cálculo de gradientes
        outputs = model(**inputs)  # Obtener las salidas del modelo

    logits = outputs.logits  # Extraer los logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1).cpu().numpy()  # Calcular probabilidades

    predicted_label = np.argmax(probabilities)  # Etiqueta predicha (índice)
    confidence_score = probabilities[0][predicted_label]  # Score de confianza

    # Mapear índice a etiqueta (ajusta según tus etiquetas)
    label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}  # Cambia esto según tus etiquetas reales
    label_mapping = {   0 : -0.5, 1 : 1.0, 2 : 2.5  }
    sentiment_label = label_map[predicted_label]

    return sentiment_label, confidence_score,(label_mapping[predicted_label] * confidence_score)

class CleanText():
    """ clearing text except digits () . , word character """ 

    def __init__(self, clean_pattern = r"[^A-ZĞÜŞİÖÇIa-zğüı'şöç0-9.\"',()]"):
        self.clean_pattern =clean_pattern

    def __call__(self, text: Union[str, list]) -> List[List[str]]:

        if isinstance(text, str):
            docs = [[text]]

        if isinstance(text, list):
            docs = text

        text = [[re.sub(self.clean_pattern, " ", sent) for sent in sents] for sents in docs]

        return text
    
def remove_emoji(data):
    '''Compile a regular expression pattern that matches emojis and special symbols in the Unicode range.'''
        
=======
#modellocation = "src/Models/model_Hotel-Recommendation"
modellocation = "maympersonal/sri"
# Load pre-trained tokenizer from the specified path
tokenizer = BertTokenizer.from_pretrained(modellocation)

# Load pre-trained model for sequence classification from the specified path
model = BertForSequenceClassification.from_pretrained(
    modellocation,
    num_labels=3,  # Number of labels/classes for classification
    output_attentions=False,  # Do not return attention scores
    output_hidden_states=False  # Do not return hidden states
)

# Move the model to CPU (Change this if using GPU)
model.to("cpu")


def sentiment_analysis(comment: str):
    """
    Perform sentiment analysis on the input comment using the BERT model.
    
    Args:
        comment (str): The text comment to analyze.
    
    Returns:
        tuple: The predicted sentiment label, confidence score, and calculated score.
    """
    # Tokenize the input comment for the BERT model
    inputs = tokenizer(comment, return_tensors='pt', padding=True, truncation=True, max_length=512)

    # Ensure the model and inputs are on the correct device (CPU or GPU)
    device = torch.device("cpu")  # Using CPU here
    model.to(device)
    inputs = {key: val.to(device) for key, val in inputs.items()}  # Move inputs to device

    # Perform inference without calculating gradients (for efficiency)
    with torch.no_grad():
        outputs = model(**inputs)  # Get model outputs

    # Extract logits from model output
    logits = outputs.logits
    # Calculate softmax probabilities
    probabilities = torch.nn.functional.softmax(logits, dim=-1).cpu().numpy()

    # Get predicted label (index of the highest probability)
    predicted_label = np.argmax(probabilities)
    # Get the confidence score of the predicted label
    confidence_score = probabilities[0][predicted_label]

    # Map the predicted index to a sentiment label
    label_map = {0: 'negative', 1: 'neutral', 2: 'positive'}  # Adjust these labels based on your model
    label_mapping = {0: -0.5, 1: 1.0, 2: 2.5}  # Mapping for score calculation

    sentiment_label = label_map[predicted_label]  # Final sentiment label

    # Return the sentiment label, confidence score, and calculated sentiment score
    return sentiment_label, confidence_score, (label_mapping[predicted_label] * confidence_score)


class CleanText:
    """
    Class for cleaning text by removing characters that do not match a certain pattern.
    
    Args:
        clean_pattern (str): Regular expression pattern for cleaning text. Defaults to removing non-alphanumeric and punctuation characters.
    """
    def __init__(self, clean_pattern=r"[^A-ZĞÜŞİÖÇIa-zğüı'şöç0-9.\"',()]"):
        self.clean_pattern = clean_pattern

    def __call__(self, text: Union[str, list]) -> List[List[str]]:
        """
        Apply the cleaning process to the input text.
        
        Args:
            text (Union[str, list]): The text or list of texts to clean.
        
        Returns:
            List[List[str]]: A list of cleaned sentences.
        """
        # If input is a single string, wrap it in a list
        if isinstance(text, str):
            docs = [[text]]
        # If input is a list, assume it contains multiple texts
        if isinstance(text, list):
            docs = text

        # Apply regex to clean each sentence in the input text
        text = [[re.sub(self.clean_pattern, " ", sent) for sent in sents] for sents in docs]

        return text


def remove_emoji(data: str) -> str:
    """
    Remove emojis and special symbols from the input text.
    
    Args:
        data (str): The input text.
    
    Returns:
        str: The cleaned text without emojis or special symbols.
    """
>>>>>>> Stashed changes
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons (e.g., smiley faces)
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # various symbols
        u"\U00002702-\U000027B0"  # other symbols
        u"\U000024C2-\U0001F251"  # enclosed characters
        u"\U0001f926-\U0001f937"  # additional emoticons
        u"\U00010000-\U0010ffff"  # supplemental characters
        u"\u2640-\u2642"          # gender symbols (e.g., male/female)
        u"\u2600-\u2B55"          # miscellaneous symbols
        u"\u200d"                 # zero-width joiner
        u"\u23cf"                 # eject symbol
        u"\u23e9"                 # fast-forward button
        u"\u231a"                 # watch symbol
        u"\ufe0f"                 # variation selector
        u"\u3030"                 # wavy dash symbol
<<<<<<< Updated upstream
        "]+", re.UNICODE)  # Ensure the pattern is treated as Unicode.
    
    # Use re.sub() to replace all matched emojis and symbols in the input data with an empty string.
    return re.sub(emoj, '', data)
    
def remove_punct(text):
    '''Function to remove punctuation from the given text by replacing it with spaces'''
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    # Use the regex pattern to find and replace all punctuation characters in the text with a space
=======
        "]+", re.UNICODE)  # Compile the regex pattern as Unicode

    # Remove emojis and symbols from the text
    return re.sub(emoj, '', data)


def remove_punct(text: str) -> str:
    """
    Remove punctuation from the input text.
    
    Args:
        text (str): The text to clean.
    
    Returns:
        str: The text without punctuation.
    """
    # Create a regex pattern to match punctuation characters
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    # Replace all punctuation characters with a space
>>>>>>> Stashed changes
    text = regex.sub(" ", text)

    return text

<<<<<<< Updated upstream
def remove_numbers(text):
    '''Function to remove numbers from the given text'''
    return re.sub(r'\d+', '', text)
=======

def remove_numbers(text: str) -> str:
    """
    Remove numeric characters from the input text.
    
    Args:
        text (str): The text to clean.
    
    Returns:
        str: The text without numbers.
    """
    return re.sub(r'\d+', '', text)


# Example usage:
comment = "it is very bad."  # Example comment for sentiment analysis
result = sentiment_analysis(comment)
print(result)  # Output should be something like ('negative', 0.9)
>>>>>>> Stashed changes
