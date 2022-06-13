#Trial run to see if i remember how to make NLTK tools as scripts

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage (count, total):
    return 100 * count / total

#runs with NLTK tools, ensure importNLTK has been run prior
