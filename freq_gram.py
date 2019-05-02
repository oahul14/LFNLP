from Project_ToolKit import get_all_descriptions, fdist_plot, fdist_csv
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import ngrams
import matplotlib.pyplot as plt
# change paths' names to get the result
paths = ['/Users/luhao/Desktop/Project/Scraped_results/monster13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/reed13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/cv13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/glass13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/indeed13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/independent13456.json',
         '/Users/luhao/Desktop/Project/Scraped_results/total13456.json']


collection = []
for path in paths:
    singledes_collection = get_all_descriptions(path)
    collection = collection + singledes_collection
cleaned_collection = [x for x in collection if x]

tokenizer = RegexpTokenizer(r'\w+')
token_collect = []
for des in cleaned_collection:
    tokens = tokenizer.tokenize(des)
    for w in tokens:
        token_collect.append(w)

# filter with stopwords
# using .add() when creating a set object returns only NoneType
stop_words = set(stopwords.words('english'))
filtered_tokens = [x for x in token_collect if x not in stop_words]

# stemming and its filtration
ps = PorterStemmer()
stemmed_tokens = [ps.stem(x) for x in filtered_tokens]
my_stop_words = ['We', 'UK', 'within', 'you', 'our', 'thi', 'the', 'includ', 'client', 'us', 'role', 'team', 'busi', 'ensur',
                 'A', 'work', 'peopl', 'landfil', 'servic', 'opportun', 'plant', 'time', 'provid', 'respons', 'job']
filtered_stems = [x for x in stemmed_tokens if x not in my_stop_words]


# single stem frequency counting, using filtered_stems
sing_freq = FreqDist(filtered_stems).most_common(15)
# print(sing_freq)
# fdist_csv(sing_freq, 'Single word13456-15')
single_colors = ['maroon', 'maroon', 'maroon',
          'plum', 'plum', 'plum', 'plum',
          'orangered', 'orangered','orangered', 'orangered',
          'orange', 'orange', 'orange', 'orange']

# bigram frequency counting, using original words, no second filtration
my_stop_bi = ['competit', 'salari', 'indirect', 'tax', 'time', 'join', 'us', 'We', 'look', 'UK', 'work', 'within', 'day', 'the' ]
bigram_stems = [x for x in stemmed_tokens if x not in my_stop_bi]
bigram_freq = FreqDist(ngrams(bigram_stems, 2)).most_common(15)
# print(bigram_freq)
# fdist_csv(bigram_freq, 'Bigram 13456-15')
bigram_colors = ['maroon', 'maroon', 'maroon',
          'plum', 'plum', 'plum', 'plum',
          'orangered', 'orangered','orangered', 'orangered',
          'orange', 'orange', 'orange', 'orange']

# trigram frequency counting, using original words, no second filtration
trigram_freq = FreqDist(ngrams (stemmed_tokens, 3)).most_common(15)
# print(trigram_freq)
# fdist_csv(trigram_freq, 'Trigram 13456-20')
trigram_colors = ['maroon', 'maroon', 'maroon',
          'plum', 'plum', 'plum', 'plum',
          'orangered', 'orangered','orangered', 'orangered',
          'orange', 'orange', 'orange', 'orange']

plt.figure(figsize=(60, 70))
plt.style.use('ggplot')
plt.subplot(311)
fdist_plot('Single-word13456', sing_freq, single_colors, 'Word Frequency Distribution', 'Word Stems')
plt.subplot(312)
fdist_plot('Bigram13456', bigram_freq, bigram_colors, 'Bigrams Frequency Distribution', 'Bigram Stems')
plt.subplot(313)
fdist_plot('Trigram13456', trigram_freq, trigram_colors, 'Trigrams Frequency Distribution', 'Trigram Stems')

plt.savefig('/Users/luhao/Desktop/Project/Rough_results/freq_dist.png', dpi=350)

