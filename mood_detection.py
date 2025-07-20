from textblob import TextBlob

def get_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return "Happy"
    elif polarity > 0.1:
        return "Calm"
    elif polarity < -0.3:
        return "Sad"
    else:
        return "Neutral"
