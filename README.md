# keras-sentiment-analysis
A simple python implementation of sentiment analysis using Keras and TensorFlow.

In this project we use the Twitter Sentiment Analysis Training Corpus Dataset from http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip.

Make sure that the csv is saved as ./s-a-d.csv (in the same directory as sent-a.py and sent-predict.py)

Instructions:
  1. If you want to generate the model on your local machine, run sent-a.py to generate the dictionary and the model. Be warned that this could take a decent amount of time- it took me an hour to train the model on a Google Cloud Compute VM with 6 cores and 25GB RAM. Otherwise (if you don't want to train the model yourself) download dictionary.json, 1000w-model.json, and 1000w-model.h5 and save them in the same folder as sent-predict.py.
  2. You can now run sent-predict.py and input test tweets/sentences
  
From this point you could easily change sent-predict to read in a file of sentences (a Twitter scrape, product or company reviews, etc) and iterate through them, predicting the sentiment for each and returning the overall ratio of positive/negative sentiments, etc. I did this, however I have chosen to move on to a different method which should allow much higher accuracy and so I am not uploading that part as it is not as well implemented as I'd like. The new project will have this capability.
  
This model attains ~76% accuracy. Not bad for the relatively simple approach and the low word count (this model only uses the most popular 1000 words from the Twitter Sentiment Analysis Training Corpus Dataset). The logical evolution from here would be to train a model using word embeddings (such as GloVe or Google's Word2Vec). I will have such a repository up soon.
