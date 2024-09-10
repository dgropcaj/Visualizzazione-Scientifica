import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Reason for Part-time Work": ["Student or at school", "Ill or disabled", "Could not find full-time job", "Did not want full-time job"],
    "Very Low (0-1)": [39.12, 27.69, 37.26, 40.57],
    "Low (2-3)": [24.70, 17.42, 22.35, 24.08],
    "Medium (4-5)": [15.60, 21.65, 19.46, 16.80],
    "High (6-10)": [20.58, 33.25, 20.93, 18.55]
}

df = pd.DataFrame(data)

df_normalized = df.set_index('Reason for Part-time Work')
df_normalized = df_normalized.div(df_normalized.sum(axis=1), axis=0) * 100

work_reasons = df_normalized.index
categories = ['Very Low (0-1)', 'Low (2-3)', 'Medium (4-5)', 'High (6-10)']
values = df_normalized.values

colors = ['#ffe598', '#ffbc7c', '#ff9f74', '#fb8274']

fig, ax = plt.subplots(figsize=(10, 5))  
bar_width = 0.5
indices = range(len(work_reasons))

bottoms = [0] * len(work_reasons)
for i, category in enumerate(categories):
    ax.barh(indices, values[:, i], left=bottoms, color=colors[i], label=category, height=bar_width)
    bottoms = [x + y for x, y in zip(bottoms, values[:, i])]

ax.set_yticks(indices)
ax.set_yticklabels(work_reasons)
ax.set_xlabel('Percentage')
ax.set_xlim(0, 100) 
ax.set_title('Anxiety Levels by Reason for Part-time Work')

ax.legend(title='Anxiety Levels', bbox_to_anchor=(1.05, 1), loc='upper left')


plt.tight_layout(pad=0.1)
plt.show()
