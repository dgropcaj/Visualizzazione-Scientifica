import matplotlib.pyplot as plt
import numpy as np

health_status = [
    'Very Good', 'Good', 'Fair', 'Bad', 'Very Bad'
]
very_low = np.array([46.98, 38.97, 32.73, 24.27, 21.22])
low = np.array([24.46, 24.52, 20.67, 17.10, 12.45])
medium = np.array([14.08, 17.54, 20.27, 20.05, 17.70])
high = np.array([14.48, 18.97, 26.34, 38.58, 48.62])

colors = ['#c4e8b5', '#77c1b2', '#4fa3b1', '#2378aa']

plt.figure(figsize=(10, 5))

bar_height = 0.7  

plt.barh(health_status, very_low, color=colors[0], height=bar_height, label='Very Low (0-1)')
plt.barh(health_status, low, left=very_low, color=colors[1], height=bar_height, label='Low (2-3)')
plt.barh(health_status, medium, left=very_low + low, color=colors[2], height=bar_height, label='Medium (4-5)')
plt.barh(health_status, high, left=very_low + low + medium, color=colors[3], height=bar_height, label='High (6-10)')

plt.xlim(0, 100)

plt.xlabel('Percentage')
plt.title('Anxiety Levels by Self-Reported Health')

plt.legend(title='Anxiety Levels', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.grid(False)

plt.tight_layout()

plt.show()
