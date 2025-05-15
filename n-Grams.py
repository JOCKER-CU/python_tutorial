import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Set the NLTK data path
# nltk.data.path.append('C:\\Users\\hanna\\AppData\\Roaming\\nltk_data')

# Download necessary NLTK resources
# nltk.download('punkt', download_dir='C:\\Users\\hanna\\AppData\\Roaming\\nltk_data')

# Example sentence
sentence = "N-grams enhance language processing tasks."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Generate n-grams
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

# Display the results
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
from nltk.tokenize import word_tokenize
import nltk

# Ensure NLTK uses the correct data path
# nltk.data.path.append(r'D:\python\python_tutorial\nltk_env\Lib\site-packages')

# Example sentence
sentence = "N-grams enhance language processing tasks."

# Tokenize the sentence
tokens = word_tokenize(sentence)

print("Tokens:", tokens)
