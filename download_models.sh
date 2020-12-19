#!/bin/bash

id=0B7BsN5f2F1fZZ2ZXd3R0dEh6NDA
name=INTERSPEECH-T-BRNN.pcl

mkdir punctuator
rm ./punctuator/$name

curl -L -c cookies.txt 'https://docs.google.com/uc?export=download&id='$id \
       | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt

curl -L -b cookies.txt -o $name \
       'https://docs.google.com/uc?export=download&id='$id'&confirm='$(<confirm.txt)

mv $name ./punctuator

rm -f confirm.txt cookies.txt

# Download models for sentence_similarity_segmentizer.py
poetry run python3 -c "
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

from transformers import BartTokenizer, BartForConditionalGeneration
BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
BartTokenizer.from_pretrained('facebook/bart-large-cnn')
"
