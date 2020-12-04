#!/bin/bash

id=0B7BsN5f2F1fZZ2ZXd3R0dEh6NDA
name=INTERSPEECH-T-BRNN.pcl

mkdir /app/punctuator
rm ./punctuator/$name

curl -L -c cookies.txt 'https://docs.google.com/uc?export=download&id='$id \
       | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt

curl -L -b cookies.txt -o $name \
       'https://docs.google.com/uc?export=download&id='$id'&confirm='$(<confirm.txt)

mv $name ./punctuator

rm -f confirm.txt cookies.txt
