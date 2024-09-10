import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path_excel = '../Datasets/tipi-di-ansia-tra-giovani.xlsx'
df = pd.read_excel(file_path_excel)

male_color = sns.color_palette("Blues", 2)[0]
female_color = sns.color_palette("Blues", 2)[1]

plt.figure(figsize=(10, 6))
bar_width = 0.35
index = range(len(df))

plt.barh(index, df['Male'], bar_width, label='Male', color=male_color)
plt.barh([i + bar_width for i in index], df['Female'], bar_width, label='Female', color=female_color)

plt.ylabel('Disorder')
plt.xlabel('Prevalence (%)')
plt.title('Prevalence of anxiety disorders among young people in 2017, by gender')
plt.yticks([i + bar_width / 2 for i in index], df['Disorder'])
plt.legend()
plt.grid(False) 

plt.tight_layout()

plt.show()
