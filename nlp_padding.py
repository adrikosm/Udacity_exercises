# -*- coding: utf-8 -*-
"""NLP_padding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eD3bANeOSzczMXfr4J7HryxuzwH4bKCA

# Imports
"""

import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

"""# Sentence"""

sentences = [
    'My favorite food is ice cream',
    'do you like ice cream too?',
    'My dog likes ice cream!',
    "your favorite flavor of icecream is chocolate",
    "chocolate isn't good for dogs",
    "your dog, your cat, and your parrot prefer broccoli"
]
print(sentences)

"""# Create the tokenizer and define an out of vocabulary token"""

tokenizer = Tokenizer(num_words=len(sentences),oov_token="<OOV>")

tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)

sequences = tokenizer.texts_to_sequences(sentences)
print(sequences)

"""# Add padding"""

padded = pad_sequences(sequences)
print("\n Word Index = ",word_index)
print("\n Sequences =",sequences)
print("\n Padded Sequences: \n",padded)

# Specify a max lenght for the padded sequene
padded = pad_sequences(sequences,maxlen=15)
print(padded)

# Put the padding at the end of the sequences
padded = pad_sequences(sequences,maxlen=15,padding="post")
print(padded)

# Limit the lenght of the sequences , you will see some sequences get truncated
padded = pad_sequences(sequences,maxlen=3)
print(padded)

# Try turning sentences that contain words that
# aren't in the word index into sequences.
# Add your own senteces to the test_data
test_data = [
    "my best friend's favorite ice cream flavor is strawberry",
    "my dog's best friend is a manatee"
]
print(test_data)
# Remind ourselves which number corresponds to the
# out of vocabulary token in the word index
print("<OOV> has the number", word_index['<OOV>'], "in the word index.")

# Convert the test sentences to sequences
test_seq = tokenizer.texts_to_sequences(test_data)
print("\nTest Sequence = ", test_seq)

# Pad the new sequences
padded = pad_sequences(test_seq, maxlen=10)
print("\nPadded Test Sequence: ")

# Notice that "1" appears in the sequence wherever there's a word 
# that's not in the word index
print(padded)