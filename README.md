# section-8

Vocab basics, one-hot encodings, word embeddings.

## Setup

```bash
# 1. Download 50-dimensional GloVe vectors from Canvas (glove.6B.50d.txt)
#    and save to this directory.

# 2. Setup a Python 3 (I used 3.7) virtual environment using your method
#    of choice (conda, pyenv)

# 3. Install requirements (torch, tqdm)
pip3 install torchvision tqdm
```

## 1. Check out the corpus

```bash
# check out the file
cat corpus.txt

# the rest of the commands build up to count-words.sh

# turn spaces into newlines -- look at one word per line
cat corpus.txt | tr " " "\n"

# sort all of the words
cat corpus.txt | tr " " "\n" | sort

# collapse consecutive duplicates to get total vocab
cat corpus.txt | tr " " "\n" | sort | uniq

# note: you can do the same thing, but tally how often each word occurred
cat corpus.txt | tr " " "\n" | sort | uniq -c

# now, we can simply count how many unique words there were total
cat corpus.txt | tr " " "\n" | sort | uniq | wc -l
```

## One-hot encodings

```bash
# 1. Check out the code in `one_hot.py`
# 2. Run the code and play with the variables it gives when it pauses for interactions
python one_hot.py
```

## Playing with word embeddings

```bash
# 1. Check out the code in `word_embedding_demo.py`
# 2. Run the code and play with the variables it gives when it pauses for interactions
python word_embedding_demo.py
```
