import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '../Datasets/ansia-etnicita.csv'
df = pd.read_csv(file_path)

df_filtered = df[['Ethnicity', 'Mean']]

df_filtered = df_filtered.dropna()

df_filtered['Mean'] = pd.to_numeric(df_filtered['Mean'], errors='coerce')

mean_scores = df_filtered.groupby('Ethnicity').mean().reset_index()

mean_scores = mean_scores.sort_values(by='Mean', ascending=False)

mean_scores = mean_scores[mean_scores['Ethnicity'] != 'White Gypsy / Traveller ']

custom_palette = ['#394c59',
'#3d596c',
 '#40657f',
 '#437192',
'#477ea6',
'#508ab3',
 '#6195ba',
 '#71a1c1',
 '#81acc9',
 '#92b7d0',
'#a3c3d7',
'#a3c3d7'
]

plt.figure(figsize=(10, 6))
sns.barplot(x='Mean', y='Ethnicity', data=mean_scores, palette=custom_palette)
plt.title('Average Anxiety Score by Ethnicity')
plt.xlabel('Average Anxiety Score')
plt.ylabel('Ethnicity')
plt.show()
