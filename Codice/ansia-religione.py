import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    "Religion": [
        "No Religion", "Christian (all denominations)", "Buddhist", "Hindu", "Jewish",
        "Muslim", "Sikh", "Any other Religion"
    ],
    "Very Low (0-1)": [39.60, 40.42, 35.59, 35.01, 33.99, 38.66, 39.36, 36.36],
    "Low (2-3)": [24.11, 22.58, 24.86, 24.44, 28.22, 21.89, 23.74, 22.99],
    "Medium (4-5)": [16.76, 16.81, 17.09, 20.31, 15.99, 19.01, 17.38, 17.42],
    "High (6-10)": [19.53, 20.19, 22.46, 20.24, 21.80, 20.45, 19.51, 23.23],
}

df = pd.DataFrame(data)

religions = df['Religion']
categories = ['Very Low (0-1)', 'Low (2-3)', 'Medium (4-5)', 'High (6-10)']
values = df[categories].values

row_sums = values.sum(axis=1)
values = values / row_sums[:, np.newaxis] * 100 

colors = ['#ffe598', '#ffbc7c', '#ff9f74', '#fb8274']  

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.5
indices = np.arange(len(religions))

bottoms = np.zeros(len(religions))

for i, category in enumerate(categories):
    ax.barh(indices, values[:, i], left=bottoms, color=colors[i], label=category, height=bar_width)
    bottoms += values[:, i]

ax.set_yticks(indices)
ax.set_yticklabels(religions)
ax.set_xlabel('Percentage')
ax.set_xlim(0, 100)  
ax.set_title('Anxiety Levels by Religion')


ax.legend(title='Anxiety Levels', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
