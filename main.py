from core.assistant import athena

def main():
    print('\033[H\033[2J', end='')
    print("Athena Assistant")
    
    while True:
        listener = input("> ").strip().lower()
    
        if listener != "athena":
            continue

        athena()

if __name__ == "__main__":
    main()