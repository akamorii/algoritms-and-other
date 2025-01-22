import os
import time

def draw_static_field(width, height):
    os.system('clear')  # Очистить экран
    print("\033[H", end="")  # Переместить курсор в начало
    for _ in range(height):
        print(" " * width)

def update_field(x, y, char="O"):
    print(f"\033[{y + 1};{x + 1}H{char}", end="")  # Обновить позицию курсора
    print("\033[H", end="")  # Вернуться в начало

# Пример использования
width, height = 20, 10
draw_static_field(width, height)

# Двигайте "O" по экрану
for i in range(15):
    update_field(i, i % height)
    time.sleep(0.5)
