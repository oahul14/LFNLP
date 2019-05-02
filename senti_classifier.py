from nltk.classify import NaiveBayesClassifier
from nltk import word_tokenize
import json
import numpy as np
import re
from nltk.probability import FreqDist
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB, GaussianNB, ComplementNB

MNB_classifier = SklearnClassifier(MultinomialNB())
BNB_classifier = SklearnClassifier(BernoulliNB())
GNB_classifier = SklearnClassifier(GaussianNB())
CNB_classifier = SklearnClassifier(ComplementNB())

# find all sentences with 'landfill'
paths = ['/Users/luhao/Desktop/Project/Scraped_results/monster13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/reed13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/cv13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/glass13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/indeed13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/independent13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/total13456.json']

def get_all_descriptions(path):
    singledes_collection = []
    with open(path, encoding='utf-8') as f:
        file = json.loads(f.read())
    for dict in file:
        singledes_collection.append(dict['description'])
    singledes_collection.append('\n')
    return singledes_collection

des_collection = []
for path in paths:
    singledes_collection = get_all_descriptions(path)
    des_collection = des_collection + singledes_collection
    nd_collection = np.array(des_collection)
    nd_collection[nd_collection == ''] = 'Description NA'
    cleaned_collection = nd_collection.tolist()

sent_collection=[]
for cont in cleaned_collection:
    for i in re.split(r'\.|\. |\?|\? |-|- |!|! |\n|\t|  |   |; |;|• ', cont):
            sent_collection.append(i)

landfill_sents = [i for i in  sent_collection if 'landfill' in word_tokenize(i) or 'Landfill' in word_tokenize(i)]

with open('/Users/luhao/Desktop/Project/Lingual_study/testset.txt', 'w') as f:
    for sent in landfill_sents:
        f.write('%s\n' % sent)
# build classifier
def format_sentence(x):
    return({word: True for word in word_tokenize(x)})

pos = []
with open("/Users/luhao/Desktop/Project/Lingual_study/Training_sets/positive-words.txt") as f:
    for i in f:
        pos.append([format_sentence(i), 'pos'])
neg = []
with open("/Users/luhao/Desktop/Project/Lingual_study/Training_sets/negative-words.txt", encoding='ISO-8859-1') as f:
    for i in f:
        neg.append([format_sentence(i), 'neg'])

training = pos + neg

NB_classifier = NaiveBayesClassifier.train(training)
MNB = MNB_classifier.train(training)
BNB = BNB_classifier.train(training)
CNB = CNB_classifier.train(training)
# GNB = GNB_classifier.train(training)

result = []
for sent in landfill_sents:
    result.append(NB_classifier.classify(format_sentence(sent)))
result_freq = FreqDist(result)
print('NB: ', result_freq.most_common(2))

result = []
for sent in landfill_sents:
    result.append(MNB.classify(format_sentence(sent)))
result_freq = FreqDist(result)
print('MNB: ', result_freq.most_common(2))

result = []
for sent in landfill_sents:
    result.append(BNB.classify(format_sentence(sent)))
result_freq = FreqDist(result)
print('BNB: ', result_freq.most_common(2))

result = []
for sent in landfill_sents:
    result.append(CNB.classify(format_sentence(sent)))
result_freq = FreqDist(result)
print('CNB: ', result_freq.most_common(2))

# result = []
# for sent in landfill_sents:
#     result.append(GNB.classify(format_sentence(sent)))
# result_freq = FreqDist(result)
# print('GNB: ', result_freq.most_common(2))

