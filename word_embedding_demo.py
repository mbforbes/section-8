"""
Demo of word embedding (Glove) representations of words.

Setup:
- pip3 install torchvision tqdm
- glove.6B.50d.txt must be in this directory
"""

import code

import torch
from tqdm import tqdm


emb = torch.zeros(400000, 50)
idx2word = []
word2idx = {}

with open("glove.6B.50d.txt", "r") as f:
    for i, line in tqdm(enumerate(f.readlines()), total=400000):
        # break apart the line
        pieces = line.strip().split(" ")
        word = pieces[0]
        nums = pieces[1:]

        # build the word vector, save to matrix
        emb[i] = torch.FloatTensor([float(num) for num in nums])

        # add it to our vocab bookkeeping
        idx2word.append(word)
        assert idx2word[i] == word
        word2idx[word] = i

print("Play with `emb` and `word2idx`")
code.interact(local=dict(globals(), **locals()))


# ideas
# ---
#
# hotel, motel
# hotel, aquarium
#
# tuesday, wednesday
# tuesday, zebra
# tuesday, tuesday
#
# happy, delighted
# happy, zebra
# happy, sad


def sim(word1, word2):
    vec1 = emb[word2idx[word1]]
    norm1 = vec1 / vec1.dot(vec1).sqrt()

    vec2 = emb[word2idx[word2]]
    norm2 = vec2 / vec2.dot(vec2).sqrt()

    return norm1.dot(norm2)


print("Play with `sim(word1, word2)`")
code.interact(local=dict(globals(), **locals()))
