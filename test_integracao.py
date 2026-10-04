from leitor import carregar_automato
from automata import Automato


def test_fluxo_completo():
    dados = carregar_automato("automato_exemplo.json")

    automato = Automato(
        dados["estados"],
        dados["alfabeto"],
        dados["estado_inicial"],
        dados["estados_finais"],
        dados["transicoes"]
    )

    resultados = {}

    for palavra in dados["palavras"]:
        resultados[palavra] = automato.reconhecer(palavra)

    assert resultados["aab"] is True
    assert resultados["aaa"] is False