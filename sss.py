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
		if syns[i][j] not in words:
			words[syns[i][j]] = syns[i]
		else:
			words[syns[i][j]] += syns[i]
		
import csv

with open('shorten-phrases.csv', 'r') as f:
	reader = csv.reader(f)
	data = list(reader)

import re

for datum in data:
	datum[0] = re.split(r'; |, |\[|\]', re.sub(r'\(.*\)', '', datum[0].replace('.', '')))
	datum[1] = re.split(r'; |, |\[|\]', re.sub(r'\(.*\)', '', datum[1].replace('.', '')))

phrases = {}

for i in range(len(data)):
	for j in range(len(data[i][1])):
		if data[i][1][j] not in phrases:
			phrases[data[i][1][j]] = []
		for k in range(len(data[i][0])):
			phrases[data[i][1][j]].append(data[i][0][k])
			
words.update(phrases)
		
def synRep(sentence, nlp = spacyNLP, syn = words):
	doc = nlp(sentence)
	tokens = [random.choice(syn[token.text]) if token.text in syn else random.choice(syn[token.lemma_]) if token.lemma_ in syn else token.text for token in doc]
	return ' '.join(tokens)
