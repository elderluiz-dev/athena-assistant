
from datetime import datetime

def show_time():
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

    print(
        f"Hoje é {weekday}, dia {now.day}. "
        f"Agora são {now.hour:02d}:{now.minute:02d}.\n"
    )
