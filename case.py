class AlgumaCoisa:

    # Isso é chamado dentro de um contexto
    def __enter__(self):
        print("ENTRO NO CONTEXTO")

    def __exit__(self):
        print("SAIO DO CONTEXTO")


def main():
    with AlgumaCoisa as alguma_coisa:
        print("DENTRO DO CONTEXTO")


main()
