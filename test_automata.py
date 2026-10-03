from automata import Automato


def criar_automato_teste():
    estados = ["q0", "q1", "q2", "q3"]
    alfabeto = ["a", "b"]
    estado_inicial = "q0"
    estados_finais = ["q3"]

    transicoes = {
        "q0": {
            "epsilon": ["q1", "q2"]
        },
        "q1": {
            "a": ["q1"],
            "b": ["q3"]
        },
        "q2": {
            "a": ["q3"]
        },
        "q3": {}
    }

    return Automato(
        estados,
        alfabeto,
        estado_inicial,
        estados_finais,
        transicoes
    )


def test_fecho_epsilon():
    automato = criar_automato_teste()

    resultado = automato.fecho_epsilon({"q0"})

    assert resultado == {"q0", "q1", "q2"}


def test_mover():
    automato = criar_automato_teste()

    resultado = automato.mover({"q1", "q2"}, "a")

    assert resultado == {"q1", "q3"}


def test_palavra_aceita():
    automato = criar_automato_teste()

    resultado = automato.reconhecer("aab")

    assert resultado is True


def test_palavra_rejeitada():
    automato = criar_automato_teste()

    resultado = automato.reconhecer("aaa")

    assert resultado is False