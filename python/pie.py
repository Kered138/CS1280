import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = [0.1,0.1,0.1,0.1]
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%',shadow ={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9}, startangle = 90)
plt.show()