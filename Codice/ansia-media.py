import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Religion': [
        'No Religion', 
        'Christian (all denominations)', 
        'Buddhist', 
        'Hindu', 
        'Jewish', 
        'Muslim', 
        'Sikh', 
        'Any other Religion'
    ],
    'Average Mean Rating': [
        2.90, 
        2.92, 
        3.09, 
        3.11, 
        3.15, 
        3.05, 
        2.89, 
        3.19
    ]
}


df = pd.DataFrame(data)


df = df.sort_values(by='Average Mean Rating', ascending=False)

plt.figure(figsize=(10, 6))
plt.barh(df['Religion'], df['Average Mean Rating'], color='#7fa8c6')
plt.xlabel('Average Mean Rating')
plt.ylabel('Religion')
plt.title('Average Mean Rating by Religion')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()
