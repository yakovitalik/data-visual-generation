from random_walk import RandomWalk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# Создание нескольких случайных блужданий
# Новые блуждания создаются до тех пор, пока программа остается активной.
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_runing = input("Make another walk? (y/n): ")
    if keep_runing == 'n':
        break
