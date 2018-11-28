# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np
def sentiment(a):
        with open(a) as file:

                sid = SentimentIntensityAnalyzer()


# the variable 'message_text' now contains the text we will analyze.
                print(file.read())
                message_text =file.read()

        #print(message_text)

# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
        scores = sid.polarity_scores(message_text)
# Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen

        #for key in sorted(scores):
                #print('{0}: {1}, '.format(key, scores[key]), end='')

        print(scores["compound"])
        return scores["compound"]



# y_pos = np.arange(len(counts.keys()))
# performance = counts.values()
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, counts.keys())
# plt.ylabel('Sentiment')
#
# plt.show()