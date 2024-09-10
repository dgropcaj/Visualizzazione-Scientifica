import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '../Datasets/ansia-dati.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='epworth_score', y='gad_score', hue='gender', palette='Set2', alpha=0.6, style='gender', markers=["o", "o"])
plt.title('Correlation between Anxiety and Sleepiness')
plt.xlabel('Epworth Sleepiness Scale Score')
plt.ylabel('GAD-7 Score (Anxiety)')
plt.legend(title='Gender', markerscale=1.5)
plt.grid(False) 
plt.show()

