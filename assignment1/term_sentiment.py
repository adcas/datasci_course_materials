import sys
from utils import *

'''
Usage: python term_sentiment.py <sentiment_file> <tweet_file>

Computes the sentiment for the terms in the tweets that do not appear in the file AFINN-111.txt
'''

def compute_terms_sentiments(lines_sentiment_analysis):
	term_score_lists = defaultdict(list)
	non_zero_analysis = filter(lambda a: a.score != 0, lines_sentiment_analysis)

	for a in non_zero_analysis:
		for w in a.unmatched_words:
			term_score_lists[w].append(a.score)

	term_scores = defaultdict(int)
	for term, score_list in term_score_lists.iteritems():
		if DEBUG:
			print term, '-->', score_list
		term_scores[term] = sum(score_list)/float(len(score_list))

	return term_scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    analyzer = LineSentimentAnalyzer(sent_file)
    tweets = parse_tweets(tweet_file)
    lines_sentiment_analysis = analyzer.compute_sentiments(tweets)
    terms_sentiments = compute_terms_sentiments(lines_sentiment_analysis)
    for term, score in terms_sentiments.iteritems():
    	print term, score


if __name__ == '__main__':
    main()
