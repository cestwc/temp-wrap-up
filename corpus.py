import json
import spacy
from tqdm.notebook import tqdm

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")

from datasets import load_dataset
dataset = load_dataset('wikitext', 'wikitext-103-v1', split='train')

from cleantext import clean
import re

def build_corpus(destiny = 'corpus.json', num = len(dataset)):
	corpus = []
	for i in tqdm(range(num)):
		datum = dataset[i]
		if i == num:
			break
		datum['text'] = clean(re.sub("\s@.{,3}@\s", ' ', datum['text']).replace('<unk>', 'unknown'), no_urls=True, no_emails=True, replace_with_url='URL', replace_with_email='EMAIL')
		if len(datum['text'].split()) < 25 or len([c for c in datum['text'] if c.isalpha()]) / len(datum['text']) < 0.7:
			pass
		else:
			doc = nlp(datum['text'])
			for sent in doc.sents:
				corpus.append(sent.text)
				
	with open(destiny, 'w') as f:
		json.dump(corpus, f)
	return destiny
