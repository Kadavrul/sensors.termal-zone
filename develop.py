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
        # './audio/jarvis-halo.wav',
        # './audio/jarvis-halo_1.wav',
        './audio/hello_user.mp3',

    ]
    greeting1 = random.choice(greetings1)
    sound_file_path_halo = greeting1
    play_sound(sound_file_path_halo)
    time.sleep(5)


def hello_art(stdscr):
    # Устанавливаем настройки экрана
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Получаем размер экрана
    height, width = stdscr.getmaxyx()

    # Создаем новое окно на всю ширину и высоту экрана
    win = curses.newwin(height, width, 0, 0)

    # Отображаем текстовый арт в окне
    art = "   ▄▄▄▄▄ ▀▄    ▄  ▄▄▄▄▄      ▄▄▄▄▀ ▄███▄   █▀▄▀█\n  █     ▀▄ █  █  █     ▀▄ ▀▀▀ █    █▀   ▀  █ █ █\n▄  ▀▀▀▀▄    ▀█ ▄  ▀▀▀▀▄       █    ██▄▄    █ ▄ █\n ▀▄▄▄▄▀     █   ▀▄▄▄▄▀       █     █▄   ▄▀ █   █\n          ▄▀                ▀      ▀███▀      █ \n                                             ▀  \n\n\n █▀▄▀█ ████▄    ▄   ▄█    ▄▄▄▄▀ ████▄ █▄▄▄▄ ▄█    ▄     ▄▀ \n █ █ █ █   █     █  ██ ▀▀▀ █    █   █ █  ▄▀ ██     █  ▄▀   \n █ ▄ █ █   █ ██   █ ██     █    █   █ █▀▀▌  ██ ██   █ █ ▀▄ \n █   █ ▀████ █ █  █ ▐█    █     ▀████ █  █  ▐█ █ █  █ █   █\n    █        █  █ █  ▐   ▀              █    ▐ █  █ █  ███ \n   ▀         █   ██                    ▀       █   ██      \n\n  ▄ ▄   ▄█    ▄▄▄▄▀ ▄  █     ██          ▄▄▄▄▄   █▀▄▀█ ▄█ █     ▄███▄   \n █   █  ██ ▀▀▀ █   █   █     █ █        █     ▀▄ █ █ █ ██ █     █▀   ▀  \n█ ▄   █ ██     █   ██▀▀█     █▄▄█     ▄  ▀▀▀▀▄   █ ▄ █ ██ █     ██▄▄   \n█  █  █ ▐█    █    █   █     █  █      ▀▄▄▄▄▀    █   █ ▐█ ███▄  █▄   ▄▀\n █ █ █   ▐   ▀        █         █                   █   ▐     ▀ ▀███▀  \n  ▀ ▀                ▀         █                   ▀                   \n\n________________________________________________________________________\n\n _________        .------------------.              \n:______.-':      :  .--------------.  :             \n| ______  |      | :                : |             \n|:______B:|      | |  Little Error: | |             \n|:______B:|      | |                | |             \n|:______B:|      | |  critical      | |             \n|         |      | |  temperature.  | |             \n|:_____:  |      | |                | |             \n|    ==   |      | :                : |             \n|       O |      :  '--------------'  :             \n|       o |      :'---...______...---'              \n|       o |-._.-i___/'             \._              \n|'-.____o_|   '-.   '-...______...-'  `-._          \n:_________:      `.____________________   `-.___.-. \n                 .'.eeeeeeeeeeeeeeeeee.'.      :___:\n    Daemon     .'.eeeeeeeeeeeeeeeeeeeeee.'.         \n              :____________________________:        \n"
    win.addstr(0, 0, art)

    # Обновляем экран и ждем 5 секунд
    win.refresh()
    time.sleep(5)
    curses.doupdate()


if __name__ == "__main__":
    say_hello()
    curses.wrapper(hello_art)
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
                    # curses.use_default_colors()
                    stdscr.keypad(True)

                    # Устанавливаем цвет фона и текста для всех ячеек
                    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
                    curses.init_pair(2, curses.COLOR_MAGENTA,
                                     curses.COLOR_BLACK)

                    stdscr.bkgd(curses.color_pair(1))

                    # Разделяем экран на 4 части
                    # Получаем размер экрана
                    h, w = stdscr.getmaxyx()

                    # Разделяем экран на 4 части
                    left_top = stdscr.subwin(h//2 - 1, w//2 - 1, 1, 1)
                    left_bottom = stdscr.subwin(
                        h - h//2 - 1, w//2 - 1, h//2 + 1, 1)
                    right_top = stdscr.subwin(
                        h//2 - 1, w - w//2 - 1, 1, w//2 + 1)
                    right_bottom = stdscr.subwin(
                        h - h//2 - 1, w - w//2 - 1, h//2 + 1, w//2 + 1)

                    # Красим окна
                    left_top.bkgd(curses.color_pair(2))
                    left_bottom.bkgd(curses.color_pair(2))
                    right_top.bkgd(curses.color_pair(2))
                    right_bottom.bkgd(curses.color_pair(2))
                    # Box win
                    left_top.attron(curses.color_pair(2))
                    left_bottom.attron(curses.color_pair(2))
                    right_top.attron(curses.color_pair(2))
                    right_bottom.attron(curses.color_pair(2))
                    # Border win

                    # Обновляем экран, чтобы изменения стали видимыми
                    # curses.doupdate()
                    # curses.doupdate()
                    # Выводим текст в каждую часть экрана

                    cpu_percent = psutil.cpu_percent()
                    cpu_freq = round(psutil.cpu_freq().current / 1000, 2)
                    cpu_cores = psutil.cpu_count(logical=False)
                    cpu_threads = psutil.cpu_count(logical=True)
                    cpu_temp = psutil.sensors_temperatures().get('coretemp')[
                        0].current
                    cpu_load_avg = psutil.getloadavg()

                    left_top.addstr(
                        f"\n{' '*10}CPU INFO\n{'-'*int(w/2-1)}\n")
                    left_top.addstr(f" CPU usage: {cpu_percent}%\n")
                    left_top.addstr(f" CPU frequency: {cpu_freq} GHz\n")
                    left_top.addstr(f" CPU cores: {cpu_cores}\n")
                    left_top.addstr(f" CPU threads: {cpu_threads}\n")
                    left_top.addstr(f" CPU temperature: {cpu_temp}°C\n")
                    # left_top.addstr(f" CPU load average: {cpu_load_avg}\n")

                    total, used, free = shutil.disk_usage("/")
                    total = total / (1024**3)
                    used = used / (1024**3)
                    free = free / (1024**3)

                    left_bottom.addstr(
                        f"\n{' '*10}DISK INFO\n{'-'*int(w/2-1)}\n")
                    left_bottom.addstr(
                        f" Total: {total:.2f} GB |\n Used: {used:.2f} GB |\n Free: {free:.2f} GB\n")

                    mem = psutil.virtual_memory()
                    total_mem = round(mem.total / (1024 ** 3), 2)
                    used_mem = round(mem.used / (1024 ** 3), 2)
                    free_mem = round(mem.available / (1024 ** 3), 2)

                    # win_name = "MEMORY USAGE"
                    right_top.addstr(
                        f"\n{' '*10}MEMORY USAGE\n{'-'*int(w/2-1)}\n")
                    # right_top.addstr(f"\n {'-'*30}\n{' '*10}MEMORY USAGE\n{'-'*30}\n")
                    right_top.addstr(f" Total Memory:\t\t{total_mem} GB\n")
                    right_top.addstr(f" Used Memory:\t\t{used_mem} GB\n")
                    right_top.addstr(f" Free Memory:\t\t{free_mem} GB\n")
                    right_top.addstr(f" Memory Utilization:\t{mem.percent}%\n")

                    right_bottom.addstr(
                        f"\n{' '*10}TEMP INFO\n{'-'*int(w/2-1)}\n")
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
                        " Текущие температуры термальных зон:\n")
                    for zone, temperature in temperatures.items():
                        # print(f"{zone}: {temperature}°C")
                        right_bottom.addstr(f" {zone}: {temperature}°C\n")

                    # Возвращаем среднюю температуру всех термальных зон
                    # return sum(temperatures.values()) / len(temperatures)
                    temperature = sum(temperatures.values()
                                      ) / len(temperatures)
                    right_bottom.addstr(
                        f" Текущая температура: {temperature}°C\n")
                # Если температура больше 85 градусов Цельсия, выводим уведомление
                    if temperature > 85:
                        os.system(
                            'notify-send "Внимание! Температура превысила 85 градусов!"')
                        sound_file_path_halo = './audio/bell.mp3'
                        play_sound(sound_file_path_halo)
                        sound_file_path_halo = './audio/critical_temp.mp3'
                        play_sound(sound_file_path_halo)

                        # Отображаем изменения на экране

                    # stdscr.refresh()
                    left_top.box()
                    left_bottom.box()
                    right_top.box()
                    right_bottom.box()
                    left_top.refresh()
                    left_bottom.refresh()
                    right_top.refresh()
                    right_bottom.refresh()

                    # Ожидаем нажатия клавиши
                    time.sleep(3)

                def on_ctrl_c_pressed(e):
                    sound_file_path = './audio/exit.mp3'
                    play_sound(sound_file_path)
                    # Здесь можете добавить логику завершения программы
                    time.sleep(2)

                curses.wrapper(main)
            except ValueError as e:
                print(f"Ошибка: {e}")
                break  # выходим из бесконечного цикла при возникновении ошибки

    except KeyboardInterrupt:
        on_ctrl_c_pressed('ctrl+c')
