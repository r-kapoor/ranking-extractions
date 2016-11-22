from nltk.tokenize import sent_tokenize, word_tokenize

def tokenize(text):
    
    word_tokens = list()
    for s in sent_tokenize(text):
        word_tokens += word_tokenize(s)

    return word_tokens

def text_to_lower(text):
    return text.lower()

def list_to_lower(list):
    return map(lambda x:x.lower(),list)

def tokens_remove_non_alpha(tokens):
    tokens_less_non_alpha = list()
    for token in tokens:
        if token.isalpha():
            tokens_less_non_alpha.append(token)
    return tokens_less_non_alpha