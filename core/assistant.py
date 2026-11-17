from core.modules.system_monitor import system_monitor
from core.modules.time import show_time
from core.interface import print_parser

COMMANDS = {
    "monitor": system_monitor,
    "tempo": show_time,
}

def athena():
    print('\033[H\033[2J', end='')
    print("Athena ativada!")

    while True:
        command = input("cmd> ").strip().lower()

        if command == "sair":
            break

        if command in COMMANDS:
            response = COMMANDS[command]()
            print_parser(response)
            
        else:
            print("Comando não reconhecido.")
