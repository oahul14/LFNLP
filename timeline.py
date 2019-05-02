import matplotlib.pyplot as plt
from Project_ToolKit import load_json
import numpy as np
import pandas as pd


base_path = '/Users/luhao/Desktop/Project/Scraped_results/'

cv1_size = len(load_json(base_path + 'CVLibrary.json'))
cv13_size = len(load_json(base_path + 'cv13.json'))
cv134_size = len(load_json(base_path + 'cv134.json'))
cv1345_size = len(load_json(base_path + 'cv1345.json'))
cv13456_size = len(load_json(base_path + 'cv13456.json'))
cv_size = np.ndarray([cv1_size, cv13_size, cv134_size, cv1345_size, cv13456_size])

glass1_size = len(load_json(base_path + 'Glassdoor1.json'))
glass13_size = len(load_json(base_path + 'glass13.json'))
glass134_size = len(load_json(base_path + 'glass134.json'))
glass1345_size = len(load_json(base_path + 'glass1345.json'))
glass13456_size = len(load_json(base_path + 'glass13456.json'))

indeed1_size = len(load_json(base_path + 'Indeed.json'))
indeed13_size = len(load_json(base_path + 'indeed13.json'))
indeed134_size = len(load_json(base_path + 'indeed134.json'))
indeed1345_size = len(load_json(base_path + 'indeed1345.json'))
indeed13456_size = len(load_json(base_path + 'indeed13456.json'))

independent1_size = len(load_json(base_path + 'Independentjobs.json'))
independent13_size = len(load_json(base_path + 'independent13.json'))
independent134_size = len(load_json(base_path + 'independent134.json'))
independent1345_size = len(load_json(base_path + 'independent1345.json'))
independent13456_size = len(load_json(base_path + 'independent13456.json'))

monster1_size = len(load_json(base_path + 'Monster.json'))
monster13_size = len(load_json(base_path + 'monster13.json'))
monster134_size = len(load_json(base_path + 'monster134.json'))
monster1345_size = len(load_json(base_path + 'monster1345.json'))
monster13456_size = len(load_json(base_path + 'monster13456.json'))

reed1_size = len(load_json(base_path + 'Reed.json'))
reed13_size = len(load_json(base_path + 'reed13.json'))
reed134_size = len(load_json(base_path + 'reed134.json'))
reed1345_size = len(load_json(base_path + 'reed1345.json'))
reed13456_size = len(load_json(base_path + 'reed13456.json'))

total1_size = len(load_json(base_path + 'Totaljobs.json'))
total13_size = len(load_json(base_path + 'total13.json'))
total134_size = len(load_json(base_path + 'total134.json'))
total1345_size = len(load_json(base_path + 'total1345.json'))
total13456_size = len(load_json(base_path + 'total13456.json'))

cv_size = np.asarray(['CV Library', cv1_size, cv13_size, cv134_size, cv1345_size, cv13456_size])
glass_size = np.asarray(['Glassdoor', glass1_size, glass13_size, glass134_size, glass1345_size, glass13456_size])
indeed_size = np.asarray(['Indeed', indeed1_size, indeed13_size, indeed134_size, indeed1345_size, indeed13456_size])
independent_size = np.asarray(['Independent Jobs', independent1_size, independent13_size, independent134_size, independent1345_size, independent13456_size])
monster_size = np.asarray(['Monster', monster1_size, monster13_size, monster134_size, monster1345_size, monster13456_size])
reed_size = np.asarray(['Reed', reed1_size, reed13_size, reed134_size, reed1345_size, reed13456_size])
total_size = np.asarray(['Total Jobs', total1_size, total13_size, total134_size, total1345_size, total13456_size])

data = np.array([['Scraping Period', '2.21 - 2.27', '3.14 - 3.20', '3.21 - 3.27', '4.28 - 4.3', '4.4 - 4.10'], cv_size, glass_size, indeed_size, independent_size, monster_size, reed_size, total_size])
print(data)
np.savetxt('/Users/luhao/Desktop/Project/Rough_results/st1.csv', data, delimiter=',')

# print(cv_size)
# print(glass_size)
# print(indeed_size)
# print(independent_size)
# print(monster_size)
# print(reed_size)
# print(total_size)

# x = ['2.21 - 2.27', '3.14 - 3.20', '3.21 - 3.27', '3.28 - 4.3', '4.4 - 4.10']
# plt.grid(True, linestyle='-.')
# plt.bar(x, indeed_size, width=0.5, label='Indeed', fc='peachpuff')
# plt.bar(x, glass_size, bottom=indeed_size, width=0.5, label='Glassdoor', fc='tomato')
# plt.bar(x, total_size, bottom=indeed_size+glass_size, width=0.5, label='Total jobs', fc='skyblue')
# plt.bar(x, independent_size, bottom=indeed_size+glass_size+total_size, width=0.5, label='Independent jobs', fc='olivedrab')
# plt.bar(x, monster_size, bottom=indeed_size+glass_size+total_size+independent_size, width=0.5, label='Monster', fc='tan')
# plt.bar(x, reed_size, bottom=indeed_size+glass_size+total_size+independent_size+monster_size, width=0.5, label='Reed', fc='slateblue')
# plt.bar(x, cv_size, bottom=indeed_size+glass_size+total_size+independent_size+monster_size+reed_size, width=0.5, label='CV Library', fc='palevioletred')
#
# plt.legend()
#
# plt.title('The Change of Data Size over Time')
# plt.xlabel('Date of Scraping')
# plt.ylabel('Number of Scraped Results')
#
# plt.savefig('/Users/luhao/Desktop/Project/Rough_results/TV.png', dpi=300)

