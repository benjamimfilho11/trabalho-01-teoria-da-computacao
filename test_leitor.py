import pytest

from leitor import validar_automato


def automato_valido():
    return {
        "estados": ["q0", "q1", "q2"],
        "alfabeto": ["a", "b"],
        "estado_inicial": "q0",
        "estados_finais": ["q2"],
        "transicoes": {
            "q0": {
                "epsilon": ["q1"]
            },
            "q1": {
                "a": ["q1"],
                "b": ["q2"]
            },
            "q2": {}
        },
        "palavras": [
            "aab",
            "ab",
            "b"
        ]
    }


def test_automato_valido():
    dados = automato_valido()

    validar_automato(dados)


def test_campo_obrigatorio_ausente():
    dados = automato_valido()

    del dados["alfabeto"]

    with pytest.raises(ValueError):
        validar_automato(dados)


def test_estado_inicial_invalido():
    dados = automato_valido()

    dados["estado_inicial"] = "q99"

    with pytest.raises(ValueError):
        validar_automato(dados)


def test_estado_final_invalido():
    dados = automato_valido()

    dados["estados_finais"] = ["q99"]

    with pytest.raises(ValueError):
        validar_automato(dados)


def test_estado_origem_invalido():
    dados = automato_valido()

    dados["transicoes"]["q99"] = {
        "a": ["q1"]
    }

    with pytest.raises(ValueError):
        validar_automato(dados)


def test_simbolo_transicao_invalido():
    dados = automato_valido()

    dados["transicoes"]["q1"]["c"] = ["q2"]

    with pytest.raises(ValueError):
        validar_automato(dados)


def test_estado_destino_invalido():
    dados = automato_valido()

    dados["transicoes"]["q1"]["a"] = ["q99"]

    with pytest.raises(ValueError):
        validar_automato(dados)


def test_palavra_com_simbolo_invalido():
    dados = automato_valido()

    dados["palavras"] = ["abc"]

    with pytest.raises(ValueError):
        validar_automato(dados)