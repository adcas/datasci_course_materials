import json
from collections import defaultdict
import re

DEBUG = True

def log(str):
	if DEBUG:
		print str

class LineAnalysis(object):
	
	def __init__(self, line_words, line_score, unmatched_words):
		self.words= line_words
		self.score = line_score
		self.unmatched_words = unmatched_words


class LineSentimentAnalyzer(object):

	def __init__(self, sent_file):
		self.sents, self.long_sents = self.parse_sentiments(sent_file)

	def handle_long_sents(self, sents, long_sents):
		pass

	def parse_sentiments(self, sent_file):
		sents = dict()
		long_sents = defaultdict(list)

		for l in sent_file.readlines():
			key, score = l.split('\t')
			key, score = key.strip(), int(score.strip())

			key_words = key.split(' ')
			if len(key_words) > 1:
				first_key_word = key_words[0] 
				long_sents[first_key_word].append((key_words, score))
			else:
				sents[key] = score

		return sents, long_sents

	def match_long_sent(self, line_words, match_candidates):
		s = None
		for key_words, score in match_candidates:
			if line_words[:len(key_words)] == key_words:
				return (key_words, score)
		return None

	def match_sent(self, words):
		w = words[0]
		long_sent_candidate = self.long_sents.get(w)
		if long_sent_candidate:
			match = self.match_long_sent(words, long_sent_candidate)
			if match:
				return match
		if w in self.sents:
			log('Match %s' % w)
			return ([w], self.sents.get(w))
		else:
			return None

	def compute_line_sentiment(self, line):
		i = line_score = 0
		line_words = line.split()
		line_words = [re.sub(r'\W+', '', w) for w in line_words]
		line_words = filter(None, line_words)
		unmatched_words = []
		while i < len(line_words):
			match = self.match_sent(line_words[i:])
			if match:
				key, score = match
				line_score += score
				i += len(key)
			else:
				unmatched_words.append(line_words[i])
				i += 1
		return LineAnalysis(line, line_score, unmatched_words)

	def compute_sentiments(self, lines):
		sentiments = []
		for line in lines:
			sentiments.append(self.compute_line_sentiment(line))
		return sentiments

	def print_analysis_complete(self, analysis):
		for a in analysis:
			print a.words, '-->', a.score

	def print_analysis_scores(self, analysis):
		for a in analysis:
			print a.score


def parse_tweets(tweet_file):
	tweets = []
	for l in tweet_file.readlines():
		tweet = json.loads(l)
		text = tweet.get('text')
		if text:
			text = text.strip().lower()
			tweets.append(text)

	return tweets
