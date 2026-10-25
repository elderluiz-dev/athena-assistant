def main():
    temperatures = []
    temp = float(input("Temperatura: "))
    temperatures.append(temp)
    temp = float(input("Temperatura: "))
    temperatures.append(temp)
    temp = float(input("Temperatura: "))
    temperatures.append(temp)

    count = 0
    for temp in temperatures:
        print(f"{temp:.1f} ºC")
        count = count + 1

    print("Temperaturas lidas:", count)
    print(f"Ultima temperatura lida: {temperatures[-1]} ºC")

if __name__ == "__main__":
    main()