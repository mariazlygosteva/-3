import matplotlib.pyplot as plt

labels = ['B', 'A', 'E', 'D', 'C']
sizes = [10, 14, 3, 6, 8]
colors = ['red', 'blue', 'darkblue', 'green', 'orange' ]
plt.pie(sizes, labels=labels, colors=colors, startangle=240)
plt.axis('equal')
plt.show()
