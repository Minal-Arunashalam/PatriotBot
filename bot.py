import nltk
nltk.download('punkt')
nltk.download('wordnet')
import numpy as py
import random
import string
import warnings

import bs4 as bs
import urllib.request
import re

# warnings.filterwarnings("ignore")
# warnings.filterwarnings("default")

link = urllib.request.urlopen("https://www.gmu.edu/student-life/where-eat")
link = link.read()

data = bs.BeautifulSoup(link, 'lxml')
# print(data)

data_paragraphs = data.find_all('p')
data_text = ''
for para in data_paragraphs:
    data_text += para.text

# print(data_text)
data_text = data_text.lower()

data_text = re.sub(r'\[[0-9]*\]', ' ', data_text)
data_text = re.sub(r'\s+', ' ', data_text)
# print(data_text)

sentence = nltk.sent_tokenize(data_text)
words = nltk.word_tokenize(data_text)
# print(words)

lem = nltk.stem.WordNetLemmatizer()

def perform_lem(tokens):
    return [lem.lemmatize(token) for token in tokens]

#punctuation removal
pr = dict((ord(punctuation), None) for punctuation in string.punctuation)

#tokenizer
def get_processed_text(page):
    return perform_lem(nltk.word_tokenize(page.lower().translate(pr)))

greeting_inputs = ("hi", "hey", "hello", "yo", "good morning", "morning", "good evening", "evening", "whats up", "what's up", "hey there")
greeting_responses = ["hello"]
def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_response(user_input):
    bot_response = ''
    sentence.append(user_input)

    word_vectorizer = TfidfVectorizer(tokenizer = get_processed_text, stop_words = 'english')
    word_vectors = word_vectorizer.fit_transform(sentence)

    similar_vector_values = cosine_similarity(word_vectors[-1], word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        bot_response = bot_response + "Sorry, I don't understand"
        return bot_response
    else:
        bot_response = bot_response + sentence[similar_sentence_number]
        return bot_response
    
continue_flag = True
print("Hey there, I'm PatriotBot. Ask me a question!")
while (continue_flag == True):
    person = input()
    person = person.lower()
    if person != 'bye':
        if person == 'thanks' or person == 'thank you':
            continue_flag = False
            print("You're welcome!")
        else:
            if generate_greeting_response(person) != None:
                print("PatriotBot" + generate_greeting_response(person))
            else:
                print("Patriot Bot", end=" ")
                print(generate_response(person))
                sentence.remove(person)
    else:
        continue_flag = False
        print("Bye!")

     
    


