
from datetime import datetime

def show_time():
    type = "show_time"
    now = datetime.now()

    weekdays = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }

    weekday = weekdays[now.weekday()]

    return{
        "type": "show_time",
        "weekday": weekday,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute    
    }
