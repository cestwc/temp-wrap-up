import spacy
spacyNLP = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
nltkSTOP  = stopwords.words()

from nltk.stem.snowball import SnowballStemmer
nltkSTEMMER = SnowballStemmer("english")

def stemming(sentence, nlp = spacyNLP, stop = nltkSTOP, stemmer = nltkSTEMMER):
	doc = nlp(sentence)
	tokens = [stemmer.stem(token.lemma_) for token in doc if token.text not in stop]
	return ' '.join(tokens)

def rmStop(sentence, nlp = spacyNLP, stop = nltkSTOP):
	doc = nlp(sentence)
	tokens = [token.text for token in doc if token.text not in stop and token.lemma_ not in stop]
	return ' '.join(tokens)

import random
with open('wordnet-synonyms.txt', 'r') as f:
	syns = [[w.replace('_', ' ') for w in t.split()] for t in f.readlines()]
	
words = {}
for i in range(len(syns)):
	for j in range(len(syns[i])):
		words[syns[i][j]] = syns[i]
		
def synRep(sentence, nlp = spacyNLP, syn = words):
	doc = nlp(sentence)
	tokens = [random.choice(syn[token.lemma_]) if token.text in syn else random.choice(syn[token.lemma_]) if token.lemma_ in syn else token.text for token in doc]
	return ' '.join(tokens)
