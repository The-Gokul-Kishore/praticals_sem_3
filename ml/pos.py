import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.chunk import RegexpParser
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
text = "Mahendra Singh Dohni is the greatest of All time"
sentences = sent_tokenize(text)
stemmer = PorterStemmer()
chunk_grammer = r"""
    NP:{<DT>?<JJ><NN.>} #chunk sequences of dt jj nn
"""
chunk_parser = RegexpParser(chunk_grammer)
print("Original text:",text)
for sentence in sentences:
    words = word_tokenize(sentence)
    pos_tagged_words = nltk.pos_tag(words)
    stemmed_words = [(word,stemmer.stem(word))for word in words]
    chuked_sentence = chunk_parser.parse(pos_tagged_words)
    print("\n Sentence:",sentence)
    print("POS tagging result:")
    for word ,pos in pos_tagged_words:
        print(f"{word}:{pos}")
    print("stemming Resut:")
    for word, stem in stemmed_words: 
        print(f" {word},{stem}")
    print("chunking result")
    print(chuked_sentence)