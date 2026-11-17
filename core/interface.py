def print_parser(response):

    if response["type"] == "system_monitor":
        print(f"Uso da CPU em {response['cpu']}%.")
        print(
            f"Memória utilizada {response['used_memory']:.2f} GiB, "
            f"{response['available_memory']:.2f} GiB disponíveis "
            f"de {response['total_memory']:.2f} GiB totais."
        )

    elif response["type"] == "show_time":
        print(f"Hoje é {response['weekday']}, dia {response['day']}.")
        print(f"Agora são {response['hour']:02d}:{response['minute']:02d}.\n")