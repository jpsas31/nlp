from collections import defaultdict
from typing import Dict, List
import math
from preprocessing import preprocessing
class BigramLanguageModel:
    def __init__(self):
        self.bigram_counts = {}
        self.unigram_counts = {}
        self.vocab_size = 0
        # self.train(corpus)

    def train(self, sentences):
        for tokens in sentences:
            # Update unigram counts
            for token in tokens:
                if token in self.unigram_counts:
                    self.unigram_counts[token] += 1
                else:
                    self.unigram_counts[token] = 1
                    self.vocab_size += 1

            # Update bigram counts
            for i in range(1, len(tokens)):
                bigram = (tokens[i-1], tokens[i])
                if bigram in self.bigram_counts:
                    self.bigram_counts[bigram] += 1
                else:
                    self.bigram_counts[bigram] = 1
            



    def get_bigram_prob(self, prev_word, word):
        bigram = (prev_word, word)
        # Calculate smoothed probability using add-one smoothing
        numerator = self.bigram_counts.get(bigram, 1)
        denominator = self.unigram_counts.get(prev_word, self.vocab_size)
        if denominator == 0:
            denominator = 1/self.vocab_size
        return numerator / denominator

    def get_sentence_probability(self, sentence):
        # Add start and end tokens to sentence
        # sentence = "<s> " + sentence.strip() + " </s>"
        tokens = preprocessing(sentence)[0]
        print(tokens)
        log_prob = 0.0
        for i in range(len(tokens)-1):
            token1 = tokens[i]
            token2 = tokens[i+1]
            log_prob += math.log(self.get_bigram_prob(token1, token2))
         
        return math.exp(log_prob)

