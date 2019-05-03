# keras-sentiment-analysis
A simple python implementation of sentiment analysis using Keras and TensorFlow.

In this project we use the Twitter Sentiment Analysis Training Corpus Dataset from http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip.

Make sure that the csv is saved as ./s-a-d.csv

Instructions:
  1. Run sent-a.py to generate the dictionary and the model
  2. You can now run sent-predict.py and input test tweets/sentences
  
 This implementation is very basic, the logical evolution from here would be to train a model using word embeddings (such as GloVe or Google's Word2Vec). I will have such a repository up soon.
