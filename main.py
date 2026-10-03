from leitor import carregar_automato
from automata import Automato


def main():
    dados = carregar_automato("automato_exemplo.json")

    automato = Automato(
        dados["estados"],
        dados["alfabeto"],
        dados["estado_inicial"],
        dados["estados_finais"],
        dados["transicoes"]
    )

    for palavra in dados["palavras"]:
        print(f"\nPalavra: {palavra}")

        if automato.reconhecer(palavra):
            print("Resultado: ACEITA")
        else:
            print("Resultado: REJEITADA")


if __name__ == "__main__":
    main()