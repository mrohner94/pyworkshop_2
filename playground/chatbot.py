import random
import string
import nltk
nltk.download('punkt')
from sklearn.feature_extraction.text import TfidfVectorizer

# Define a list to store the conversation history
conversation_history = []

# Define a function to preprocess the user input
def preprocess(text):
    text = text.lower()  # Convert text to lowercase
    text = "".join([char for char in text if char not in string.punctuation])  # Remove punctuation
    tokens = nltk.word_tokenize(text)  # Tokenize text into words
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  # Remove stopwords
    return " ".join(tokens)

# Define a function to update the conversation history
def update_conversation_history(user_input, chatbot_response):
    preprocessed_input = preprocess(user_input)
    preprocessed_response = preprocess(chatbot_response)
    conversation_history.append(preprocessed_input)
    conversation_history.append(preprocessed_response)

# Define a function to generate responses based on the TF-IDF weighted frequency of words used by the user
def chatbot_response(user_input):
    # Preprocess user input
    preprocessed_input = preprocess(user_input)

    # Add user input to conversation history
    conversation_history.append(preprocessed_input)

    # Use TF-IDF to weigh the importance of words based on their frequency across all user inputs
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(conversation_history)
    feature_names = vectorizer.get_feature_names()
    feature_weights = vectorizer.idf_

    # Generate a response based on the weighted frequency of words used by the user
    word_scores = {}
    for word in preprocessed_input.split():
        if word in feature_names:
            word_scores[word] = feature_weights[feature_names.index(word)]
    if not word_scores:
        return "I'm sorry, I didn't understand. Can you please rephrase?"
    max_word = max(word_scores, key=word_scores.get)
    return f"I see you're interested in {max_word}. Can you tell me more?"

# Start the conversation
print("Chatbot: Hello, how can I assist you?")
while True:
    user_input = input("User: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    update_conversation_history(user_input, response)
