import pandas as pd
import matplotlib.pyplot as plt


file_path = '../Datasets/ansia-dal-2012-al-2022.csv'
data = pd.read_csv(file_path)

overall_trend_data = data.groupby('government Year')['Mean adults\' self-reporting anxiety score'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))


ax.plot(overall_trend_data['government Year'], overall_trend_data['Mean adults\' self-reporting anxiety score'], 
        marker='o', color='#845aaf', linewidth=3) 

ax.set_title('Aggregated Mean Anxiety Scores Across All Regions', fontsize=14)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Mean Anxiety Score', fontsize=12)

ax.set_facecolor('#ffffff')
ax.grid(False)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
