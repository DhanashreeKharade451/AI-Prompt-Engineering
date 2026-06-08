import nltk

from nltk.stem import PorterStemmer


# Download NLTK resources (tokenizers)

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

# Sample email content for stemming

email_content = "Our team will be working on the upcoming project deadlines. Please ensure that all deliverables are submitted before the end of the week."


# Create a Porter Stemmer instance

porter_stemmer = PorterStemmer()


# Apply stemming to each word in the email content

stemmed_words = [porter_stemmer.stem(word) for word in nltk.word_tokenize(email_content)]


# Print the original and stemmed text

print("Original Email Content:", email_content)

print("Stemmed Email Content:", " ".join(stemmed_words))

# output:
# [nltk_data]     C:\Users\khara\AppData\Roaming\nltk_data...
# [nltk_data]   Package wordnet is already up-to-date!
# Original Email Content: Our team will be working on the upcoming project deadlines. Please ensure that all deliverables are submitted before the end of the week.
# Stemmed Email Content: our team will be work on the upcom project deadlin . pleas ensur that all deliver are submit befor the end of the week .
