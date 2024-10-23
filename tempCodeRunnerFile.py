import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize
sentence = "Hi, My name is Vaibhav, I am a developer.I am currently pursuing my Btech degree in DYPCET"
print(sent_tokenize(sentence))

from nltk.tokenize import TreebankWordTokenizer
word_token = TreebankWordTokenizer()
print(word_token.tokenize(sentence))