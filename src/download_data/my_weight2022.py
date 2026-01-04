from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

path = Path('my_weights/my_weights2022.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Извлечение дат и максимальных температур
dates, weights = [], []
for row in reader:
    current_date = datetime.strptime(row[0], '%Y-%m-%d')
    weight = float(row[1])
    dates.append(current_date)
    weights.append(weight)

# Нанесение данных на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, weights, color='green')

# Форматирование диаграммы
ax.set_title("My weights", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Weight (kg)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
