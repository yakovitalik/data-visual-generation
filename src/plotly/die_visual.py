import plotly.express as px

from die import Die

# Создание кубика D6.
die = Die()

# Моделирование серии бросков, с сохранением результата в списке.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Анализ результатов
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов
fig = px.bar(x=poss_results, y=frequencies)
fig.show()
