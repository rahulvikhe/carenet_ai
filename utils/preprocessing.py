import re
import string

def clean_text(text):
    """
    Basic text preprocessing: lowercasing, removing punctuation,
    and unwanted characters.
    """
    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    # Remove user mentions and hashtags
    text = re.sub(r'\@\w+|\#','', text)

    # Remove punctuations
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove extra spaces
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)

    return text

