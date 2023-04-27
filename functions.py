import psutil


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
