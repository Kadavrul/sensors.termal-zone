import pygame
import curses
import psutil
import subprocess
import re
import random
import os
import shutil
import time


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


if __name__ == "__main__":
    say_hello()
    try:
        # say_hello() ACTIVATE
        # keyboard.add_hotkey('ctrl+c', on_ctrl_c_pressed)
        while True:
            # time.sleep(3)
            try:
                # Запускаем основную функцию

                def main(stdscr):
                    # Устанавливаем флаги для работы с цветом
                    curses.start_color()
                    curses.use_default_colors()

                    # Устанавливаем цвет фона и текста для всех ячеек
                    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                    stdscr.bkgd(curses.color_pair(1))

                    # Разделяем экран на 4 части
                    h, w = stdscr.getmaxyx()
                    left_top = curses.newwin(h//2, w//2, 0, 0)
                    left_bottom = curses.newwin(h-h//2, w//2, h//2, 0)
                    right_top = curses.newwin(h//2, w-w//2, 0, w//2)
                    right_bottom = curses.newwin(h-h//2, w-w//2, h//2, w//2)

                    # Выводим текст в каждую часть экрана

                    cpu_percent = psutil.cpu_percent()
                    cpu_freq = round(psutil.cpu_freq().current / 1000, 2)
                    cpu_cores = psutil.cpu_count(logical=False)
                    cpu_threads = psutil.cpu_count(logical=True)
                    cpu_temp = psutil.sensors_temperatures().get('coretemp')[
                        0].current
                    cpu_load_avg = psutil.getloadavg()

                    left_top.addstr(f"{'-'*30}\n{' '*10}CPU INFO\n{'-'*30}\n")
                    left_top.addstr(f"CPU usage: {cpu_percent}%\n")
                    left_top.addstr(f"CPU frequency: {cpu_freq} GHz\n")
                    left_top.addstr(f"CPU cores: {cpu_cores}\n")
                    left_top.addstr(f"CPU threads: {cpu_threads}\n")
                    left_top.addstr(f"CPU temperature: {cpu_temp}°C\n")
                    left_top.addstr(f"CPU load average: {cpu_load_avg}\n")

                    total, used, free = shutil.disk_usage("/")
                    total = total / (1024**3)
                    used = used / (1024**3)
                    free = free / (1024**3)

                    left_bottom.addstr(
                        f"{'-'*30}\n{' '*12}DISK INFO\n{'-'*30}\n")
                    left_bottom.addstr(
                        f"Total: {total:.2f} GB |\n Used: {used:.2f} GB |\n Free: {free:.2f} GB\n")

                    mem = psutil.virtual_memory()
                    total_mem = round(mem.total / (1024 ** 3), 2)
                    used_mem = round(mem.used / (1024 ** 3), 2)
                    free_mem = round(mem.available / (1024 ** 3), 2)

                    right_top.addstr(
                        f"{'-'*30}\n{' '*10}MEMORY USAGE\n{'-'*30}\n")
                    right_top.addstr(f"Total Memory:\t\t{total_mem} GB\n")
                    right_top.addstr(f"Used Memory:\t\t{used_mem} GB\n")
                    right_top.addstr(f"Free Memory:\t\t{free_mem} GB\n")
                    right_top.addstr(f"Memory Utilization:\t{mem.percent}%\n")

                    right_bottom.addstr(
                        f"{'-'*30}\n{' '*10}TEMP INFO\n{'-'*30}\n")
                    # Получаем вывод команды sensors для термальных зон
                    sensors_output = subprocess.check_output(
                        ['sensors']).decode('utf-8')
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
                    # print("Текущие температуры термальных зон:")
                    right_bottom.addstr(
                        "Текущие температуры термальных зон:\n")
                    for zone, temperature in temperatures.items():
                        # print(f"{zone}: {temperature}°C")
                        right_bottom.addstr(f"{zone}: {temperature}°C\n")

                    # Возвращаем среднюю температуру всех термальных зон
                    # return sum(temperatures.values()) / len(temperatures)
                    temperature = sum(temperatures.values()
                                      ) / len(temperatures)
                    right_bottom.addstr(
                        f"Текущая температура: {temperature}°C\n")
                # Если температура больше 85 градусов Цельсия, выводим уведомление
                    if temperature > 85:
                        os.system(
                            'notify-send "Внимание! Температура превысила 85 градусов!"')
                        sound_file_path_halo = './bell.mp3'
                        play_sound(sound_file_path_halo)
                        # Отображаем изменения на экране

                    # stdscr.refresh()
                    left_top.refresh()
                    left_bottom.refresh()
                    right_top.refresh()
                    right_bottom.refresh()

                    # Ожидаем нажатия клавиши
                    time.sleep(3)

                def on_ctrl_c_pressed(e):
                    sound_file_path = './jarvis_kak-pojelaete.wav'
                    play_sound(sound_file_path)
                    # Здесь можете добавить логику завершения программы
                    time.sleep(2)

                curses.wrapper(main)
            except ValueError as e:
                print(f"Ошибка: {e}")
                break  # выходим из бесконечного цикла при возникновении ошибки

    except KeyboardInterrupt:
        on_ctrl_c_pressed('ctrl+c')
