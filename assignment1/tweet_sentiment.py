import sys
from utils import *

'''
Usage: python tweet_sentiment.py <sentiment_file> <tweet_file>

Derive the sentiment of each tweet
'''

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    analyzer = LineSentimentAnalyzer(sent_file)
    tweets = parse_tweets(tweet_file)
    lines_sentiment_analysis = analyzer.compute_sentiments(tweets)
    if DEBUG:
	    analyzer.print_analysis_complete(lines_sentiment_analysis)    	
    else:
	    analyzer.print_analysis_scores(lines_sentiment_analysis)


if __name__ == '__main__':
    main()