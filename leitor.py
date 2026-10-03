import json


def carregar_automato(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    validar_automato(dados)

    return dados


def validar_automato(dados):
    campos_obrigatorios = [
        "estados",
        "alfabeto",
        "estado_inicial",
        "estados_finais",
        "transicoes",
        "palavras"
    ]

    # Verifica se todos os campos obrigatórios existem
    for campo in campos_obrigatorios:
        if campo not in dados:
            raise ValueError(
                f"Campo obrigatório ausente: {campo}"
            )

    estados = set(dados["estados"])
    alfabeto = set(dados["alfabeto"])

    # Verifica se o estado inicial existe
    if dados["estado_inicial"] not in estados:
        raise ValueError(
            f"Estado inicial inválido: {dados['estado_inicial']}"
        )

    # Verifica se todos os estados finais existem
    for estado_final in dados["estados_finais"]:
        if estado_final not in estados:
            raise ValueError(
                f"Estado final inválido: {estado_final}"
            )

    # Verifica as transições
    for estado_origem, transicoes in dados["transicoes"].items():

        # Estado de origem precisa existir
        if estado_origem not in estados:
            raise ValueError(
                f"Estado de origem inválido: {estado_origem}"
            )

        for simbolo, destinos in transicoes.items():

            # Símbolo precisa pertencer ao alfabeto
            # ou representar uma transição epsilon
            if simbolo not in alfabeto and simbolo != "epsilon":
                raise ValueError(
                    f"Símbolo inválido na transição: {simbolo}"
                )

            # Estados de destino precisam existir
            for destino in destinos:
                if destino not in estados:
                    raise ValueError(
                        f"Estado de destino inválido: {destino}"
                    )

    # Verifica se as palavras usam apenas símbolos do alfabeto
    for palavra in dados["palavras"]:
        for simbolo in palavra:
            if simbolo not in alfabeto:
                raise ValueError(
                    f"Símbolo '{simbolo}' da palavra "
                    f"'{palavra}' não pertence ao alfabeto"
                )