import json
from tqdm.notebook import tqdm

from datasets import load_dataset
dataset = load_dataset('wikitext', 'wikitext-103-v1', split='train')

from cleantext import clean

def build_corpus(destiny = 'corpus.json'):
	corpus = []
	for i, datum in enumerate(tqdm(dataset)):
		datum['text'] = clean(datum['text'].replace('<unk>', 'unknown'), no_urls=True, no_emails=True, replace_with_url='URL', replace_with_email='EMAIL')
		if len(datum['text'].split()) < 25 or len([c for c in datum['text'] if c.isalpha()]) / len(datum['text']) < 0.7:
			pass
		else:
			corpus.append(datum['text'])
	with open(destiny, 'w') as f:
		json.dump(corpus, f)
	return destiny
