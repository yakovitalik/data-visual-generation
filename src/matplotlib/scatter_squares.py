import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Задание заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Задание размера шрифта делений на осях.
ax.tick_params(labelsize=14)

plt.show()
