# temp-wrap-up
to save time

## Usage of corpus
```python
!pip install -U pip setuptools wheel > /dev/null
!pip install -U spacy > /dev/null
!python -m spacy download en_core_web_sm > /dev/null

!pip install datasets > /dev/null
!pip install clean-text > /dev/null
!pip install Unidecode > /dev/null

!rm -rf temp-wrap-up; git clone https://github.com/cestwc/temp-wrap-up.git; cp temp-wrap-up/* ./

from corpus import build_corpus
corpus_file = build_corpus(drivePath + 'corpus.json', 100000)
```

## Usage of transfer
```python
!git clone https://github.com/google-research-datasets/sentence-compression.git; gzip -d sentence-compression/data/comp-data.eval.json.gz
```
```python
from transfer import fromSentenceCompression
transfer_file = fromSentenceCompression('sentence-compression/data/comp-data.eval.json')

transfer_data, = data.TabularDataset.splits(
                            path = '.',
                            train = transfer_file,
                            format = 'json',
                            fields = fields
)
```

## Usage of stemstop
```python
import json
with open(drivePath + 'nlg-datasets/' + 'corrupt-3s.json', 'r') as f:
dataset = [json.loads(x) for x in f.readlines()]

from tqdm.notebook import tqdm
from stemstop import stemming

for i in tqdm(range(len(dataset))):
    dataset[i]['long'] = stemming(dataset[i]['long'])

with open(drivePath + 'nlg-datasets/' + 'corrupt-3s3.json', 'w') as f:
    f.writelines([json.dumps(x) + '\n' for x in dataset])
```

## Usage of bart generate
```python
!pip install transformers

from bartgen import loadmodel, bartGenerate
from sss import stemming, synRep
concisemodel = loadmodel(drivePath + 'tut6-netG.pt')
```
