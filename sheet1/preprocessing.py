import string
import re
def preprocessing(text):
    # remove non-ASCII characters
    text = text.encode("ascii", "ignore").decode()
    # remove newlines and extra whitespace
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    # Remove Roman numerals
    text = re.sub(r'\b[MDCLXVI]+\b', '', text)

    # remove URLs
    text = re.sub(r"http\S+", "", text)

    # remove email addresses
    text = re.sub(r"\S+@\S+", "", text)
    
    # remove special characters and digits
    text = re.sub(r"[^A-Za-z\.]+", " ", text)
    text = text.lower()
    text = text.split(". ")
    
   
    # Add <s> and </s> to the beginning and end of each sentence
    text = ["<s> " + sentence.strip() + " </s>" for sentence in text]
    text = [sentence.split() for sentence in text]
    return text



# # Convert tokens to integer IDs
# def tokens_to_ids(tokens, vocab):
#     ids = []
#     for token in tokens:
#         if token in vocab:
#             ids.append(vocab[token])
#         else:
#             ids.append(vocab["<unk>"])
#     return ids


# # Create a vocabulary and map tokens to IDs
# def create_vocab(data):
#     print(type(data))
#     vocab = {"<pad>": 0, "<unk>": 1, "<s>": 2, "</s>": 3}
#     for sentence in data:
#         tokens = tokenize(sentence)
#         for token in tokens:
#             if token not in vocab:
#                 vocab[token] = len(vocab)
#     return vocab


# # Preprocess the data
# def preprocess(data):
#     vocab = create_vocab(data)
#     preprocessed = []
#     for sentence in data:
#         tokens = tokenize(sentence)
#         ids = tokens_to_ids(tokens, vocab)
#         preprocessed.append(ids)
#     return preprocessed, vocab




