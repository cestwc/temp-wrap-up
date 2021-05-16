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
