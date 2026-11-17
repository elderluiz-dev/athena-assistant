from core.modules.system_monitor import *
from core.modules.time import *

COMMANDS = {
    "monitor": system_monitor,
    "tempo": show_time,
}


def main():
    print('\033[H\033[2J', end='')
    print("Athena Assistant")

    while True:
        listener = input("> ").strip().lower()

        if listener != "athena":
            continue

        print('\033[H\033[2J', end='')
        print("Athena ativada!")

        while True:
            command = input("cmd> ").strip().lower()

            if command == "sair":
                break

            if command in COMMANDS:
                COMMANDS[command]()
            else:
                print("Comando não reconhecido.")
            


if __name__ == "__main__":
    main()