import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_json(path):
    with open(path, encoding='utf-8') as f:
        file = json.loads(f.read())
    return file

def sum_for_all_paths(paths):
    overall_list = []
    for path in paths:
        overall_list = overall_list + load_json(path)
    return overall_list

def get_all_descriptions(path):
    singledes_collection = []
    file = load_json(path)
    for dic in file:
        singledes_collection.append(dic['description'])
    singledes_collection.append('\n')
    return singledes_collection

###################################################
#
# to clean up the possible existence of list format
# and possible blank information
#
###################################################
def clean_file(file):
    cln_file = []
    for dic in file:
        if type(dic['jobinfo']) == list:
            dic['jobinfo'] = ' '.join(dic['jobinfo'])
        if type(dic['company']) == list:
            dic['company'] = ' '.join(dic['company'])
        if type(dic['postcode']) == list:
            dic['postcode'] = ' '.join(dic['postcode'])
        if type(dic['description']) == list:
            dic['description'] = ' '.join(dic['description'])
        if dic['description'] != '' and dic['location'] != '':
            cln_file.append(dic)
    return cln_file

###########################
#
# extract newly added information from a new-round scraped result
# for a single file
#
###########################
def file_filter(new_path, old_path):
    new_file = clean_file(load_json(new_path))
    old_file = clean_file(load_json(old_path))
    old_set = set()
    for dic in old_file:
        tup = tuple(dic.items())
        old_set.add(tup)
    added_revs = []
    for dic in new_file:
        tup = tuple(dic.items())
        if tup not in old_set:
            added_revs.append(dic)
    return added_revs

def dump_json(name, file):
    with open('/Users/luhao/Desktop/Project/Scraped_results/' + str(name) + '.json', 'w') as f:
        json.dump(file, f)

# plot the frequency distribution for single word, bigram and trigram.
# need to include:
# frequency: list with tuples included
# color selection for bars in a list
# title name and which words/phrases

def fdist_plot(fname, freq, color_type, title_name, ylabel_name):
    # freq is a tuple: (str('word'), int(frequency))
    # plt.style.use('ggplot')
    xvalue = np.array([x[1] for x in freq])
    yvalue = []
    for x in range(1, len(freq) + 1):
        yvalue.append(x)
    yvalue.reverse()
    yticks = []
    for x in freq:
        if 'Word' in ylabel_name:
            yticks.insert(0, x[0])
        else:
            yticks.insert(0, ' '.join(x[0]))
    yticks.reverse()

    # plt.figure(figsize=(30,15))
    plt.title(title_name, fontsize='40', y=1.05, fontweight="bold")
    plt.ylabel(ylabel_name, rotation='horizontal', fontsize='40', fontweight='bold')
    plt.gca().yaxis.set_label_coords(-0.05, 1.02)
    plt.xlabel('Frequency', fontsize='40', fontweight='bold')
    plt.gca().xaxis.set_label_coords(0.5, -0.05)
    plt.yticks(yvalue, yticks, fontsize='40', fontweight='bold')
    plt.xticks(fontsize='40', fontweight='bold')
    plt.barh(yvalue, xvalue, 0.5, color=color_type)
    plt.gca().yaxis.grid(True)
    # plt.savefig('/Users/luhao/Desktop/Project/Rough_results/' + fname + '.png')

def fdist_csv(fdist, name):
    nd_tuplist = np.array(fdist)
    for x in nd_tuplist:
        if type(x[0]) == tuple:
            x[0] == ' '.join(x[0])
    df = pd.DataFrame(nd_tuplist)
    df.to_csv('/Users/luhao/Desktop/Project/Rough_results/' + name, index=False)

def save_txt(name, list):
    with open(name, 'w') as f:
        for item in list:
            f.write("%s, " % item)

