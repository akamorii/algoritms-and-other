
# # X + (x+shift+iteration-tomod)%mod
# for i in range(5):
#     iter = i+1
#     mod = 3
#     print(1+(1+0+iter)%mod)
    
    
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
from time import sleep

# x = [1,2,4,5,6,7]
# y = [3,4,5,6,7,9]

# Создание фигуры и осей
fig, ax = plt.subplots()

# Начальные данные
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
line, = ax.plot(x, y)

# Функция инициализации
def init():
    line.set_ydata([np.nan] * len(x))
    return line,

# Функция обновления
def update(frame):
    y = np.sin(x + frame * 0.1)
    line.set_ydata(y)
    return line,

# Создание анимации
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(0, 100, 1), init_func=init, blit=True)

# Отображение графика
plt.show()