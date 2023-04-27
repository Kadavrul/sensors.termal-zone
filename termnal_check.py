# https://chat-gpt.com/chat
import os
import re
import subprocess
import time
import random
import pygame
import psutil
import shutil
from tqdm import tqdm
pygame.init()


def play_sound(sound_file_path):
    # Инициализируем pygame.mixer
    pygame.mixer.init()
    # Загружаем звук в pygame.mixer.Sound
    sound = pygame.mixer.Sound(sound_file_path)
    # Проигрываем звук
    sound.play()


def say_hello():
    greetings = [
        'Привет! Я уведомлю тебя, если температура превысит 85 градусов.',
        'Хай! Я твой личный термостат, куда без меня.',
        'Приветствую! Я здесь, чтобы предотвратить перегрев твоего устройства.'
    ]
    # Выбираем случайное приветствие
    greeting = random.choice(greetings)
    print(greeting)
    greetings1 = [
        # './jarvis-halo_2.wav',
        './jarvis-halo.wav',
        'jarvis-halo_1.wav',

    ]
    greeting1 = random.choice(greetings1)
    sound_file_path_halo = greeting1
    play_sound(sound_file_path_halo)
    time.sleep(5)


def on_ctrl_c_pressed(e):
    sound_file_path = './jarvis_kak-pojelaete.wav'
    play_sound(sound_file_path)
    # Здесь можете добавить логику завершения программы
    time.sleep(2)
    exit()


def get_temp():
    print(f"{'-'*30}\nTEMP INFO\n{'-'*30}")
    # Получаем вывод команды sensors для термальных зон
    sensors_output = subprocess.check_output(['sensors']).decode('utf-8')
    thermal_zones = re.findall(
        r'([A-Za-z0-9\-_\.\(\)]+):\s+\+([\d\.]+).+C', sensors_output)

    # Проходимся по каждой термальной зоне и получаем температуру в градусах Цельсия
    temperatures = dict()
    for zone in thermal_zones:
        temperatures[zone[0]] = float(zone[1])

    # Проверяем, не является ли словарь пустым
    if not temperatures:
        raise ValueError("Не удалось найти термальные зоны")

    # Выводим температуры термальных зон для отладки
    print("Текущие температуры термальных зон:")
    for zone, temperature in temperatures.items():
        print(f"{zone}: {temperature}°C")

    # Возвращаем среднюю температуру всех термальных зон
    return sum(temperatures.values()) / len(temperatures)


def show_memory_usage():
    mem = psutil.virtual_memory()
    total_mem = round(mem.total / (1024 ** 3), 2)
    used_mem = round(mem.used / (1024 ** 3), 2)
    free_mem = round(mem.available / (1024 ** 3), 2)

    print(f"{'-'*30}\nMEMORY USAGE\n{'-'*30}")
    print(f"Total Memory:\t\t{total_mem} GB")
    print(f"Used Memory:\t\t{used_mem} GB")
    print(f"Free Memory:\t\t{free_mem} GB")
    print(f"Memory Utilization:\t{mem.percent}%")


def get_cpu_info():
    cpu_percent = psutil.cpu_percent()
    cpu_freq = round(psutil.cpu_freq().current / 1000, 2)
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    cpu_temp = psutil.sensors_temperatures().get('coretemp')[0].current
    cpu_load_avg = psutil.getloadavg()

    print(f"{'-'*30}\nCPU INFO\n{'-'*30}")
    print(f"CPU usage: {cpu_percent}%")
    print(f"CPU frequency: {cpu_freq} GHz")
    print(f"CPU cores: {cpu_cores}")
    print(f"CPU threads: {cpu_threads}")
    print(f"CPU temperature: {cpu_temp}°C")
    print(f"CPU load average: {cpu_load_avg}")


def get_disk_space():
    print(f"{'-'*30}\nDISK INFO\n{'-'*30}")
    total, used, free = shutil.disk_usage("/")
    total = total / (1024**3)
    used = used / (1024**3)
    free = free / (1024**3)

    # print(f"{'Дисковое пространство:':<25} {used} ГБ / {total} ГБ")
    # print(f"{'Свободно:':<25} {free} ГБ")
    print(f"Total: {total:.2f} GB | Used: {used:.2f} GB | Free: {free:.2f} GB")


if __name__ == "__main__":
    try:
        # say_hello() ACTIVATE
        # keyboard.add_hotkey('ctrl+c', on_ctrl_c_pressed)
        while True:
            try:
                get_disk_space()
                get_cpu_info()
                show_memory_usage()
                temperature = get_temp()
                print(f"Текущая температура: {temperature}°C")
                # Выводим текущую температуру
                # очистка консоли в зависимости от операционной системы

                # Если температура больше 85 градусов Цельсия, выводим уведомление
                if temperature > 85:
                    os.system(
                        'notify-send "Внимание! Температура превысила 85 градусов!"')
                    sound_file_path_halo = './bell.mp3'
                    play_sound(sound_file_path_halo)
                # Пауза между проверками температуры в 5 секунд
                time.sleep(5)
                os.system('cls' if os.name == 'nt' else 'clear')
                # print(f"Текущая температура: {temperature}°C")
            except ValueError as e:
                print(f"Ошибка: {e}")
                break  # выходим из бесконечного цикла при возникновении ошибки

    except KeyboardInterrupt:
        on_ctrl_c_pressed('ctrl+c')
