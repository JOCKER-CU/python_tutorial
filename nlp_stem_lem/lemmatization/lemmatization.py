import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download required NLTK resources
nltk.download('punkt')  # For tokenization
nltk.download('averaged_perceptron_tagger')  # For POS tagging
nltk.download('wordnet')  # For lemmatization
nltk.download('omw-1.4')  # Open Multilingual WordNet

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to map POS tags to WordNet POS tags
def get_wordnet_pos(word):
    """Map POS tag to first character used by WordNetLemmatizer"""
    tag = nltk.pos_tag([word])[0][1][0].upper()  # Get the POS tag of the word
    tag_dict = {
        "J": wordnet.ADJ,  # Adjective
        "N": wordnet.NOUN,  # Noun
        "V": wordnet.VERB,  # Verb
        "R": wordnet.ADV  # Adverb
    }
    return tag_dict.get(tag, wordnet.NOUN)  # Default to noun if not found

# List of words to lemmatize
words = ["running", "runs", "ran", "better", "best", "studies", "studying", "fairly"]

# Apply lemmatization
print("Lemmatization:")
for word in words:
    pos = get_wordnet_pos(word)  # Get POS tag
    lemma = lemmatizer.lemmatize(word, pos=pos)
    print(f"{word} ({pos}) -> {lemma}")