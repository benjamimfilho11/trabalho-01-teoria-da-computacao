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

    fecho = automato.fecho_epsilon({automato.estado_inicial})

    print("Estados:", automato.estados)
    print("Alfabeto:", automato.alfabeto)
    print("Estado inicial:", automato.estado_inicial)
    print("Estados finais:", automato.estados_finais)
    print("Transições:", automato.transicoes)

    print("\nFecho-ε do estado inicial:", fecho)

if __name__ == "__main__":
    main()