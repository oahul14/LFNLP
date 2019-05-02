import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cv_size = np.asarray([94, 145, 164, 196, 233])
glass_size = np.asarray([311, 598, 787, 975, 1170])
indeed_size = np.asarray([199, 347, 503, 643, 697])
independent_size = np.asarray([58, 82, 86, 101, 121])
monster_size = np.asarray([75, 107, 118, 132, 156])
reed_size = np.asarray([68, 106, 124, 142, 154])
total_size = np.asarray([115, 211, 237, 262, 309])

x = ['2.21 - 2.27', '3.14 - 3.20', '3.21 - 3.27', '3.28 - 4.3', '4.4 - 4.10']

plt.bar(x, indeed_size, width=0.5, label='Indeed', fc='peachpuff')
plt.bar(x, glass_size, bottom=indeed_size, width=0.5, label='Glassdoor', fc='tomato')
plt.bar(x, total_size, bottom=indeed_size+glass_size, width=0.5, label='Total jobs', fc='skyblue')
plt.bar(x, independent_size, bottom=indeed_size+glass_size+total_size, width=0.5, label='Independent jobs', fc='olivedrab')
plt.bar(x, monster_size, bottom=indeed_size+glass_size+total_size+independent_size, width=0.5, label='Monster', fc='tan')
plt.bar(x, reed_size, bottom=indeed_size+glass_size+total_size+independent_size+monster_size, width=0.5, label='Reed', fc='slateblue')
plt.bar(x, cv_size, bottom=indeed_size+glass_size+total_size+independent_size+monster_size+reed_size, width=0.5, label='CV Library', fc='palevioletred')

plt.legend()
plt.grid(True)
plt.show()