#Import textblob library for sentiment analysis
from textblob import TextBlob

#Asks user to input text to be analysed
text_to_analyse = input('Enter text for sentiment analysing: ')

#Print analysed text
print(text_to_analyse)

#Analyse and input into variable
AI_analysis = TextBlob(text_to_analyse)

#Print analysis using polarity to measure positive or negative sentiment
print(AI_analysis.sentiment)

#Prints out result definitions
print("Polarity: 1 = Very positive / 0 = Neutral / -1 = Very negative")
print("Subjectivity: 1 = very subjective / 0 = Very Objective")

