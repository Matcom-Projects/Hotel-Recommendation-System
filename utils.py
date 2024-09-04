import re
import torch 
import string
from typing import Union, List
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


def tokenize(text):
    """ Basic tokenize method that splits text into word characters, non-word characters, and digits. """
    
    # Convert the input to a string in case it's not already a string (e.g., int or float).
    text = re.sub(r" +", " ", str(text))
    
    # Tokenize the text by splitting it into digits, word characters (letters), and non-word characters (punctuation, etc.).
    text = re.split(r"(\d+|[a-zA-ZğüşıöçĞÜŞİÖÇ]+|\W)", text)
    
    # Filter out empty strings and single spaces from the list of tokens.
    # This removes unnecessary tokens created during splitting.
    text = list(filter(lambda x: x != '' and x != ' ', text))
    
    # Join the tokens back into a single string with space separation between each token.
    sent_tokenized = ' '.join(text)
    
    return sent_tokenized

    
def remove_punct(text):
    '''Function to remove punctuation from the given text by replacing it with spaces'''
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    # Use the regex pattern to find and replace all punctuation characters in the text with a space
    text = regex.sub(" ", text)

    return text

def remove_numbers(text):
    '''Function to remove numbers from the given text'''
    return re.sub(r'\d+', '', text)


class Config:

    seed_val = 17
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    epochs = 5 
    batch_size = 6
    seq_length = 512
    lr = 2e-5
    eps = 1e-8
    pretrained_model = 'bert-base-uncased'
    test_size=0.15
    random_state=42
    add_special_tokens=True 
    return_attention_mask=True 
    pad_to_max_length=True 
    do_lower_case=False
    return_tensors='pt'

# label encode
def label_encode(x):
    if x > 0.0 and x < 3.0:
        return int(0)
    if x >= 3.0 and x < 4.0:
        return int(1)
    if x <= 5.0 and x >= 4.0:
        return int(2)

# label to name
def label2name(x):
    if x == 0:
        return "Negative"
    if x == 1:
        return "Neutral"
    if x == 2:
        return "Positive"
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