import nltk

from nltk.stem import PorterStemmer

from nltk.stem import WordNetLemmatizer


# Sample email content for lemmatization

email_content_lemma = "The team members are working on their tasks diligently. Please ensure that every report is submitted promptly."


nltk.download('wordnet')


# Create a WordNet Lemmatizer instance

lemmatizer = WordNetLemmatizer()


# Apply lemmatization to each word in the email content

lemmatized_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(email_content_lemma)]


# Print the original and lemmatized text

print("Original Email Content:", email_content_lemma)

print("Lemmatized Email Content:", " ".join(lemmatized_words))

# # Output: khara@Ajay MINGW64 ~/OneDrive/Desktop/AI Prompt engineering/python
# $ python toDo3.py
# [nltk_data] Downloading package wordnet to
# [nltk_data]     C:\Users\khara\AppData\Roaming\nltk_data...
# Original Email Content: The team members are working on their tasks diligently. Please ensure that every report is submitted promptly.
# Lemmatized Email Content: The team member are working on their task diligently . Please ensure that every report is submitted promptly .