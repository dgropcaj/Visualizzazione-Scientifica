import pandas as pd
import matplotlib.pyplot as plt


file_path = '../Datasets/anxiety_by_age_group.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

df.set_index('Age Group', inplace=True)

df_normalized = df.div(df.sum(axis=1), axis=0) * 100

colors = ['#c4e8b5', '#77c1b2', '#4fa3b1', '#2378aa']

fig, ax = plt.subplots(figsize=(10, 6))

df_normalized.plot(kind='barh', stacked=True, color=colors, ax=ax)

plt.title('Anxiety Levels by Age Group', pad=10)
plt.xlabel('Percentage')
plt.ylabel('Age Group')

plt.xlim(0, 100)

plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)

plt.legend(title='Anxiety Levels', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout(pad=0)
plt.show()
