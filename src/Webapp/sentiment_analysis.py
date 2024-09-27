import torch
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np
import re
import string
from typing import Union, List


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
        "]+", re.UNICODE)  # Ensure the pattern is treated as Unicode.
    
    # Use re.sub() to replace all matched emojis and symbols in the input data with an empty string.
    return re.sub(emoj, '', data)
    
def remove_punct(text):
    '''Function to remove punctuation from the given text by replacing it with spaces'''
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    # Use the regex pattern to find and replace all punctuation characters in the text with a space
    text = regex.sub(" ", text)

    return text

def remove_numbers(text):
    '''Function to remove numbers from the given text'''
    return re.sub(r'\d+', '', text)