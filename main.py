from leitor import carregar_automato

def main():
    dados = carregar_automato("automato_exemplo.json")

    print(dados)


if __name__ == "__main__":
    main()