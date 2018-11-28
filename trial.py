# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# the variable 'message_text' now contains the text we will analyze.
with open('341-408-Navidson_new.txt', 'r') as file:
    message_text = '''I think we are making great progress on the systems side.  I would like to
set a deadline of November 10th to have a plan on all North American projects
(I'm ok if fundementals groups are excluded) that is signed off on by
commercial, Sally's world, and Beth's world.  When I say signed off I mean
that I want signitures on a piece of paper that everyone is onside with the
plan for each project.  If you don't agree don't sign. If certain projects
(ie. the gas plan) are not done yet then lay out a timeframe that the plan
will be complete.  I want much more in the way of specifics about objectives
and timeframe.

Thanks for everyone's hard work on this.'''

print(message_text)

# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
scores = sid.polarity_scores(message_text)

# Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen

for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')