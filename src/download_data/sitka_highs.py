from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат и максимальных температур
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Нанесение данных на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Форматирование диаграммы
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
