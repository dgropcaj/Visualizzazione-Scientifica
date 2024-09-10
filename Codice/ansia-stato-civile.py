import matplotlib.pyplot as plt
import numpy as np

marital_status = [
    'Married or Civil Partners', 'Cohabiting or Same sex couple', 'Single', 
    'Widow or Surviving Civil Partner', 'Divorced or Separated'
]
very_low = np.array([41.17, 40.36, 37.88, 43.29, 35.47])
low = np.array([23.83, 23.34, 23.57, 20.21, 21.58])
medium = np.array([16.18, 16.77, 17.85, 16.70, 18.00])
high = np.array([18.82, 19.52, 20.70, 19.80, 24.95])

colors = ['#ffe598', '#ffbc7c', '#ff9f74', '#fb8274']

plt.figure(figsize=(10, 4)) 

bar_height = 0.45  

plt.barh(marital_status, very_low, color=colors[0], height=bar_height, label='Very Low (0-1)')
plt.barh(marital_status, low, left=very_low, color=colors[1], height=bar_height, label='Low (2-3)')
plt.barh(marital_status, medium, left=very_low + low, color=colors[2], height=bar_height, label='Medium (4-5)')
plt.barh(marital_status, high, left=very_low + low + medium, color=colors[3], height=bar_height, label='High (6-10)')

plt.xlim(0, 100)

plt.xlabel('Percentage')
plt.title('Anxiety Levels by Marital Status')

plt.legend(title='Anxiety Levels', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout(pad=0.1)

plt.show()
