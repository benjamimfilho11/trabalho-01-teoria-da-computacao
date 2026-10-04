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

    print("=" * 50)
    print("SIMULADOR DE AUTÔMATO FINITO COM MOVIMENTOS VAZIOS")
    print("=" * 50)

    print(f"\nEstados: {dados['estados']}")
    print(f"Alfabeto: {dados['alfabeto']}")
    print(f"Estado inicial: {dados['estado_inicial']}")
    print(f"Estados finais: {dados['estados_finais']}")

    print("\nPalavras a serem testadas:")
    for palavra in dados["palavras"]:
        print(f"- {palavra}")

    print("\n" + "=" * 50)
    print("INÍCIO DAS COMPUTAÇÕES")
    print("=" * 50)

    for palavra in dados["palavras"]:
        print("\n" + "-" * 50)

        automato.reconhecer(palavra)

    print("\n" + "=" * 50)
    print("FIM DAS COMPUTAÇÕES")
    print("=" * 50)


if __name__ == "__main__":
    main()