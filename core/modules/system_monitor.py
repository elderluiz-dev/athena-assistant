import psutil

def system_monitor():
    gib = 1024 ** 3
    memory = psutil.virtual_memory()

    cpu = psutil.cpu_percent(interval=1)
    used_memory = memory.used / gib
    available_memory = memory.available / gib
    total_memory = memory.total / gib

    return {
        "type": "system_monitor",
        "cpu": cpu,
        "used_memory": used_memory,
        "available_memory": available_memory,
        "total_memory": total_memory
    }