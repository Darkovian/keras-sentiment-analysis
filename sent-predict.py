import json
import numpy as np
import keras
import keras.preprocessing.text as kpt
from keras.preprocessing.text import Tokenizer
from keras.models import model_from_json

# num_words is the maximum number of words that will be considered by our algorithm
tokenizer = Tokenizer(num_words=1000)

# These are our categories/labels
labels = ['negative', 'positive']

# Load our dictionary file
with open('dictionary.json', 'r') as dict_file:
    dictionary = json.load(dict_file)

def convert_text_to_index_array(text):
    words = kpt.text_to_word_sequence(text)
    wordIndices = []
    for word in words:
        if word in dictionary:
            wordIndices.append(dictionary[word])
        else:
            print("'%s' not in training corpus; ignoring." % (word))

    return wordIndices

# Load model
json_file = open('1000w-model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights('1000w-model.h5')

# Get user input and make a prediction on that input. Then return that prediction to the user.
while 1:
    evalSent = input('Input sentence: ')

    if len(evalSent) == 0:
        break

    testArr = convert_text_to_index_array(evalSent)
    uinput = tokenizer.sequences_to_matrix([testArr], mode='binary')

    pred = model.predict(uinput)

    print("%s sentiment; %f%% confidence" % (labels[np.argmax(pred)], pred[0][np.argmax(pred)] * 100))
