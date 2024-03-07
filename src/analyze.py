from textblob import TextBlob
import pandas as pd


def sentiment(text):
	""" Quick and Dirty Sentiment """

	value = 'Neutral'
	sentiment = 0
	try:
		sentiment = TextBlob(text).sentiment.polarity
	except:
		pass
	if sentiment < 0:
		value = 'Bad'
	elif sentiment > 0:
		value = 'Good'
	return value

def star_rating(stars):
	rating = float(stars)
	if rating >= 4.0:
		return "Good"
	elif rating <= 2.0:
		return "Bad"

	return "Neutral"

def quantify(ratings):
	sum = 3
	for r in ratings:
		if r == "Bad":
			sum = sum - 1
	return sum

def interprete(df, thresh):
        rating = analyze(df)
        interpretation = "Neutral"
        if rating >= thresh[1]:
                interpretation = "Good"
        elif rating <= thresh[0]:
                interpretation = "Bad"
        return interpretation, rating

def analyze(data):
	i = 0
	total = 0
	for row in data.itertuples(index=False):
		ratings  = [star_rating(row.rating), sentiment(row.title), sentiment(row.content) ]
		rating = quantify(ratings)
		print("Review %d: %s, %s, %s: Score: %d" % (i, ratings[0], ratings[1], ratings[2], rating ) )
		total = total + rating
		i = i+1
	verdict = float(total/i)
	return verdict

if __name__ == '__main__':
    analyze()
