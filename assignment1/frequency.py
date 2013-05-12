import sys
from utils import *

'''
Usage: python frequency.py <tweet_file>

Computes the term frequency for all the terms in the tweets.
The frequency of a term is calculate with the following formula:
[# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]
'''

def compute_term_frequency(lines):
	term_count = defaultdict(int)
	total_count = 0
	for l in lines:
		line_words = l.split()
		line_words = [re.sub(r'\W+', '', w) for w in line_words]
		line_words = filter(None, line_words)

		total_count += len(line_words)
		for w in line_words:
			term_count[w] += 1
					
	total_count = float(total_count)
	term_frequency = dict()
	for term, count in term_count.iteritems():
		term_frequency[term] = count/total_count

	return term_frequency

def main():
    tweet_file = open(sys.argv[1])
    tweets = parse_tweets(tweet_file)
    term_frequency = compute_term_frequency(tweets)

    for term, freq in term_frequency.iteritems():
    	print term.encode('utf-8') + ' ' + str(freq)


if __name__ == '__main__':
    main()