import json
from Project_ToolKit import load_json, sum_for_all_paths, clean_file

paths_1 = ['/Users/luhao/Desktop/Project/Scraped_results/Monster.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Reed.json',
           '/Users/luhao/Desktop/Project/Scraped_results/CVLibrary.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Glassdoor1.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Indeed.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Independentjobs.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Totaljobs.json']
paths_3 = ['/Users/luhao/Desktop/Project/Scraped_results/Monster_3.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Reed_3.json',
           '/Users/luhao/Desktop/Project/Scraped_results/CVLibrary_3.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Glassdoor_3_cln.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Indeed_3.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Independentjobs_3.json',
           '/Users/luhao/Desktop/Project/Scraped_results/Totaljobs_3.json']

# get the sum of first and third rounds of data
sum_1 = sum_for_all_paths(paths_1)
sum_3 = sum_for_all_paths(paths_3)
print(len(sum_1+sum_3))

sum_13 = clean_file(sum_1 + sum_3)
print(len(sum_13))

# filtration of repeated review
seen_dic = set()
new_sum_13 = []
for dic in sum_13:
    tup = tuple(dic.items())
    if tup not in seen_dic:
        seen_dic.add(tup)
        new_sum_13.append(dic)
print(len(new_sum_13))

with open('/Users/luhao/Desktop/Project/Scraped_results/sum_13.json', 'w') as f:
    json.dump(new_sum_13, f)

