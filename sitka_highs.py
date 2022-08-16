import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get dates and high temperatures from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# format plot
ax.set_title('Daily high temperatures - 2018', fontsize=20)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=13)
ax.tick_params(axis='both', which='major', labelsize=13)

plt.show()
