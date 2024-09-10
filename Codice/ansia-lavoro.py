import matplotlib.pyplot as plt

labels = ['Very Low (0-1)', 'Low (2-3)', 'Medium (4-5)', 'High (6-10)']
full_time = [39.04, 25.75, 16.93, 18.28]
part_time = [39.56, 23.72, 17.19, 19.53]

colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7)) 

wedges1, texts1, autotexts1 = ax1.pie(
    full_time, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'}, 
    textprops={'color': 'black'}, pctdistance=0.75)


centre_circle1 = plt.Circle((0, 0), 0.50, fc='white')  
ax1.add_artist(centre_circle1)
ax1.set_title('Full Time')

for autotext in autotexts1:
    autotext.set_color('black')
    autotext.set_fontsize(10)

wedges2, texts2, autotexts2 = ax2.pie(
    part_time, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'}, 
    textprops={'color': 'black'}, pctdistance=0.75)

centre_circle2 = plt.Circle((0, 0), 0.50, fc='white')  
ax2.add_artist(centre_circle2)
ax2.set_title('Part Time')

for autotext in autotexts2:
    autotext.set_color('black')
    autotext.set_fontsize(10)

plt.tight_layout()
plt.show()
