import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '../Datasets/ansia-dati.csv'
df = pd.read_csv(file_path)

sns.set(style="white", rc={'axes.grid': False})

palette_custom = {'male': '#ebd96a', 'female': '#eb91d7'}

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='gender', y='gad_score', palette=palette_custom )
plt.title('Correlation between Anxiety and Gender')
plt.xlabel('Gender')
plt.ylabel('GAD-7 Score')

plt.show()

