import sys
from preprocessing import preprocessing
from bigram import BigramLanguageModel
# def main(argv):

#     if len(argv) == 0:
#         print("sad")
#         return
#     print(argv)

# if __name__ == "__main__":
#    main(sys.argv[1:])
with open('./data/wiki/wiki.train.raw', 'r') as f:
    contents = f.read()

sentences = preprocessing(contents)
model = BigramLanguageModel()
model.train(sentences)
print(model.get_sentence_probability("It has also been the headquarters of the Little Rock Æsthetic Club since 1894 ."))