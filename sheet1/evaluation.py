def calculate_perplexity(model, test_set):
    n = len(test_set)
    log_sum = 0
    for i in range(n):
        if i == 0:
            context = "<s>"
        else:
            context = test_set[i - 1]
        word = test_set[i]
        if (context, word) in model:
            log_sum += math.log(model[(context, word)])
        else:
            log_sum += math.log(1e-10)  # to avoid log(0)
    entropy = -1 / n * log_sum
    perplexity = math.exp(entropy)
    return perplexity

# import math

# # Split corpus into training and test sets
# train_corpus = corpus[:int(0.8 * len(corpus))]
# test_corpus = corpus[int(0.8 * len(corpus)):]

# # Train the bigram language model
# model = BigramLanguageModel()
# model.fit(train_corpus)

# # Compute perplexity on test set
# total_words = 0
# log_probability_sum = 0.0

# for sentence in test_corpus:
#     probability = model.score_sentence(sentence)
#     log_probability_sum += math.log(probability)
#     total_words += len(sentence)

# perplexity = math.exp(-log_probability_sum / total_words)

# print("Perplexity: ", perplexity)


# # create a small corpus of text
# corpus = ["the quick brown fox jumps over the lazy dog", "the lazy dog sleeps all day"]

# # initialize the model with the corpus
# model = BigramLanguageModel(corpus)

# # test the model by generating probabilities for some bigrams
# print(model.get_probability("the quick"))
# print(model.get_probability("jumps over"))
# print(model.get_probability("dog sleeps"))

# # compare the probabilities to the actual probabilities
# # (you will need to manually calculate these probabilities)
