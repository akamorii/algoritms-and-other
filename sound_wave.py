# import matplotlib.pyplot as plt
# import numpy as np

# def generate_wave(amplitude, frequency, duration, sample_rate):
#     t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
#     wave = amplitude * np.sin(2 * np.pi * frequency * t)
#     return t, wave

# # Пример: Генерация звуковой волны частотой 440 Гц (нота Ля)
# amplitude = 1
# frequency = 440
# duration = 1  # 1 секунда
# sample_rate = 44100

# t, wave = generate_wave(amplitude, frequency, duration, sample_rate)
# plt.plot(t[:1000], wave[:1000])  # Показываем первые 1000 точек
# plt.xlabel("Время (с)")
# plt.ylabel("Амплитуда")
# plt.title("Синусоидальная волна")
# plt.show()


# SOUND

import numpy as np
import sounddevice as sd

def play_sine_wave(frequency, duration, amplitude=0.5, sample_rate=44100):
    """
    Генерация и воспроизведение синусоидального звука.
    
    :param frequency: Частота звука в Герцах
    :param duration: Длительность звука в секундах
    :param amplitude: Амплитуда звука (от 0 до 1)
    :param sample_rate: Частота дискретизации (по умолчанию 44100 Гц)
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()  # Дождаться окончания воспроизведения

# Пример: воспроизвести ноту Ля (440 Гц) на 2 секунды
play_sine_wave(440, 2)
