import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv

timestamps = list()
node_1_cpu_percentage = list()
node_1_memory_percentage = list()
node_2_cpu_percentage = list()
node_2_memory_percentage = list()

with open('usage.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
       match row[1].strip():
           case "node-1":
              node_1_cpu_percentage.append(int(row[3].rstrip("%")))
              node_1_memory_percentage.append(int(row[5].rstrip("%")))
           case "node-2":
              node_2_cpu_percentage.append(int(row[3].rstrip("%")))
              node_2_memory_percentage.append(int(row[5].rstrip("%")))
              timestamps.append(row[0])


fig, ax = plt.subplots(2, sharex=True)
fig.suptitle('CPU and Memory Usage During Run')

ax[0].set_title('node-1')
ax[0].plot(timestamps, node_1_memory_percentage, color='r', label='memory') 
ax[0].plot(timestamps, node_1_cpu_percentage, color='b', label='cpu') 
ax[0].set(ylabel='Usage (%)')
ax[0].legend()
ax[0].grid()

ax[1].set_title('node-2')
ax[1].plot(timestamps, node_2_memory_percentage, color='r', label='memory') 
ax[1].plot(timestamps, node_2_cpu_percentage, color='b', label='cpu') 
ax[1].set(xlabel='Timestamp (UTC)', ylabel='Usage (%)')
ax[1].xaxis.set_major_locator(ticker.MultipleLocator(25)) 
ax[1].legend()
ax[1].grid()
plt.xticks(rotation=30)


fig.tight_layout()
fig.set_size_inches(8,8)
fig.savefig("test.png")
plt.show()
