import psutil

def system_monitor():
    gib = 1024 ** 3
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    used_memory = memory.used / gib
    available_memory = memory.available / gib
    total_memory = memory.total / gib

    print(f"Uso da CPU em {cpu_usage}%.") 
    print(f"Memória utilizada {used_memory:.2f} gigas, {available_memory:.2f} gigas disponiveis de {total_memory:.2f} gigas totais.")