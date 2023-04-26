#https://chat-gpt.com/chat
import os
import re
import subprocess
import time
import random
import pygame
import keyboard
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
#	'./jarvis-halo_2.wav',
        './jarvis-halo.wav',
        'jarvis-halo_1.wav',
        
    ]
    greeting1 = random.choice(greetings1)
    sound_file_path_halo = greeting1
    play_sound(sound_file_path_halo)

def on_ctrl_c_pressed(e):
    sound_file_path = './jarvis_kak-pojelaete.wav'
    play_sound(sound_file_path)
    # Здесь можете добавить логику завершения программы
    time.sleep(2)
    exit()    
    
def get_temp():
    # Получаем вывод команды sensors для термальных зон
    sensors_output = subprocess.check_output(['sensors']).decode('utf-8')
    thermal_zones = re.findall(r'([A-Za-z0-9\-_\.\(\)]+):\s+\+([\d\.]+).+C', sensors_output)

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


if __name__ == "__main__":
    try:
        say_hello()
        #keyboard.add_hotkey('ctrl+c', on_ctrl_c_pressed)
        while True:
            try:
                temperature = get_temp()
                # Выводим текущую температуру
                print(f"Текущая температура: {temperature}°C")
                # Если температура больше 85 градусов Цельсия, выводим уведомление
                if temperature > 85:
                    os.system('notify-send "Внимание! Температура превысила 85 градусов!"')
                    sound_file_path_halo = './bell.mp3'
                    play_sound(sound_file_path_halo)    
                # Пауза между проверками температуры в 5 секунд
                time.sleep(5)
            except ValueError as e:
                print(f"Ошибка: {e}")
                break  # выходим из бесконечного цикла при возникновении ошибки
    except KeyboardInterrupt:
        on_ctrl_c_pressed('ctrl+c')
