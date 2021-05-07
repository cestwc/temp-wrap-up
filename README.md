# temp-wrap-up
to save time

## Usage of corpus
```python
!pip install datasets
!pip install clean-text > /dev/null
!pip install Unidecode > /dev/null

!rm -rf temp-wrap-up; git clone https://github.com/cestwc/temp-wrap-up.git; cp temp-wrap-up/* ./

from corpus import build_corpus
corpus_file = build_corpus(drivePath + 'corpus.json')
```

## Usage of transfer
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
