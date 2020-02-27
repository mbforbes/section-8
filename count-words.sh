#!/bin/bash

#
# Gets the size of vocab in a corpus.
# Uses naive whitespace tokenization.
# Try playing with each step individually!
#

cat corpus.txt | tr " " "\n" | sort | uniq | wc -l
