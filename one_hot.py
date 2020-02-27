"""
Demo of one-hot representations of words.

Setup:
- pip3 install torchvision
- corpus.txt must be in this directory
"""

import code

import torch


with open("corpus.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


print("Let's check out `lines`")
code.interact(local=dict(globals(), **locals()))

vocab = set()
for line in lines:
    words = line.split(" ")
    for word in words:
        vocab.add(word)


print("Let's check out `vocab`")
code.interact(local=dict(globals(), **locals()))

idx2word = list(vocab)
word2idx = {word: idx for idx, word in enumerate(idx2word)}

print("Let's check out `word2idx and idx2word`")
code.interact(local=dict(globals(), **locals()))


def encode_word(word, word2idx):
    vec = torch.zeros(len(word2idx))
    vec[word2idx[word]] = 1
    return vec


print("Let's check out `encode_word(word, word2idx)`")
code.interact(local=dict(globals(), **locals()))
