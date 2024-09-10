import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '../Datasets/ansia-etnicita.csv'
df = pd.read_csv(file_path)

df_filtered = df[['Year', 'Ethnicity', 'Mean']]

df_filtered = df_filtered.dropna()

df_filtered['Mean'] = pd.to_numeric(df_filtered['Mean'], errors='coerce')

df_filtered = df_filtered[df_filtered['Ethnicity'] != 'White Gypsy / Traveller ']

mean_scores = df_filtered.groupby(['Year', 'Ethnicity']).mean().reset_index()

plt.figure(figsize=(12, 8))
sns.lineplot(data=mean_scores, x='Year', y='Mean', hue='Ethnicity', marker='o')

plt.title('Average Anxiety Score by Ethnicity Over Time')
plt.xlabel('Year')
plt.ylabel('Average Anxiety Score')
plt.legend(title='Ethnicity', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
