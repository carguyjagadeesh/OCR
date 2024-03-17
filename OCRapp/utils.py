from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')   
      
def sentiment(text):   
      sid = SentimentIntensityAnalyzer()
      score = sid.polarity_scores(text)
      if score['neg']!=0:
        text = "SentimentAnalysis of this text is NEGATIVE"
        return text
      else:
        text = "SentimentAnalysis of this text is POSTIVE"
        return text