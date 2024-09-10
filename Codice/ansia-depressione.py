import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '../Datasets/ansia-dati.csv'
df_ansia = pd.read_csv(file_path)


sns.set(style="white") 

palette_custom = {'male': '#ebd96a', 'female': '#eb91d7'}

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_ansia, x='phq_score', y='gad_score', hue='gender', palette=palette_custom, style='gender', markers=["o", "o"])

plt.title('Correlation between Anxiety and Depression in University Students')
plt.xlabel('PHQ-9 Score (Depression)')
plt.ylabel('GAD-7 Score (Anxiety)')

plt.grid(False)


plt.show()
