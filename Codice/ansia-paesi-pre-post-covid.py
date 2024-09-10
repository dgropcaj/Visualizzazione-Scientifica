import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = '../Datasets/ansia-pre-post-covid.xlsx'  
df = pd.read_excel(file_path, sheet_name='Foglio 1')

df_cleaned = df.rename(columns={'Tabella 1': 'Country', 'Unnamed: 1': 'Pre-COVID', 'Unnamed: 2': 'Post-COVID'})
df_cleaned = df_cleaned.drop([0]) 
df_cleaned = df_cleaned[['Country', 'Pre-COVID', 'Post-COVID']].dropna() 

df_cleaned['Pre-COVID'] = pd.to_numeric(df_cleaned['Pre-COVID'], errors='coerce')
df_cleaned['Post-COVID'] = pd.to_numeric(df_cleaned['Post-COVID'], errors='coerce')

max_anxiety_country = df_cleaned.loc[df_cleaned['Post-COVID'].idxmax(), 'Country']

bar_width = 0.35
index = np.arange(len(df_cleaned['Country']))

fig, ax = plt.subplots(figsize=(10, 6))

colors_post_covid = ['#3b2453' if country == max_anxiety_country else '#845aaf' for country in df_cleaned['Country']]

bars1 = ax.bar(index, df_cleaned['Pre-COVID'], bar_width, label='Pre-COVID', alpha=0.6, color='#bba4d3')
bars2 = ax.bar(index + bar_width, df_cleaned['Post-COVID'], bar_width, label='2020', alpha=0.8, color=colors_post_covid)

ax.set_xlabel('Country')
ax.set_ylabel('Prevalence of Anxiety (%)')
ax.set_title('Prevalence of Anxiety in Selected OECD Countries (Pre-COVID vs 2020)')

ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(df_cleaned['Country'], rotation=45, ha='right')

ax.legend()

plt.tight_layout()
plt.show()
