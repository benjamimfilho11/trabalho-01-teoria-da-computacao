import json


def carregar_automato(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    validar_automato(dados)
    return dados


def validar_automato(dados):
    campos_obrigatorios = [
        "estados", "alfabeto", "estado_inicial",
        "estados_finais", "transicoes", "palavras"
    ]

    if not isinstance(dados, dict):
        raise ValueError("A definição do autômato deve ser um objeto JSON.")

    for campo in campos_obrigatorios:
        if campo not in dados:
            raise ValueError(f"Campo obrigatório ausente: {campo}")

    for campo in ("estados", "alfabeto", "estados_finais", "palavras"):
        if not isinstance(dados[campo], list):
            raise ValueError(f"O campo '{campo}' deve ser uma lista.")

    if not isinstance(dados["transicoes"], dict):
        raise ValueError("O campo 'transicoes' deve ser um objeto JSON.")

    if not dados["estados"]:
        raise ValueError("O conjunto de estados não pode ser vazio.")

    for estado in dados["estados"]:
        if not isinstance(estado, str) or not estado.strip():
            raise ValueError("Todos os estados devem ter nomes de texto não vazios.")

    if len(set(dados["estados"])) != len(dados["estados"]):
        raise ValueError("O conjunto de estados contém nomes repetidos.")

    for simbolo in dados["alfabeto"]:
        if not isinstance(simbolo, str) or len(simbolo) != 1:
            raise ValueError("Cada símbolo do alfabeto deve ser um caractere.")
        if simbolo == "ε":
            raise ValueError("O símbolo 'ε' é reservado para transições vazias.")

    if "epsilon" in dados["alfabeto"]:
        raise ValueError("'epsilon' é reservado para transições vazias.")

    if len(set(dados["alfabeto"])) != len(dados["alfabeto"]):
        raise ValueError("O alfabeto contém símbolos repetidos.")

    estados = set(dados["estados"])
    alfabeto = set(dados["alfabeto"])

    if not isinstance(dados["estado_inicial"], str) or dados["estado_inicial"] not in estados:
        raise ValueError(f"Estado inicial inválido: {dados['estado_inicial']}")

    for estado_final in dados["estados_finais"]:
        if not isinstance(estado_final, str) or estado_final not in estados:
            raise ValueError(f"Estado final inválido: {estado_final}")

    if len(set(dados["estados_finais"])) != len(dados["estados_finais"]):
        raise ValueError("O conjunto de estados finais contém nomes repetidos.")

    for estado_origem, transicoes in dados["transicoes"].items():
        if estado_origem not in estados:
            raise ValueError(f"Estado de origem inválido: {estado_origem}")

        if not isinstance(transicoes, dict):
            raise ValueError(f"As transições de '{estado_origem}' devem ser um objeto JSON.")

        for simbolo, destinos in transicoes.items():
            if simbolo not in alfabeto and simbolo != "epsilon":
                raise ValueError(f"Símbolo inválido na transição: {simbolo}")

            if not isinstance(destinos, list):
                raise ValueError(
                    f"Os destinos da transição ({estado_origem}, {simbolo}) devem ser uma lista."
                )

            for destino in destinos:
                if not isinstance(destino, str) or destino not in estados:
                    raise ValueError(f"Estado de destino inválido: {destino}")

            if len(set(destinos)) != len(destinos):
                raise ValueError(
                    f"Destinos repetidos na transição ({estado_origem}, {simbolo})."
                )

    for palavra in dados["palavras"]:
        if not isinstance(palavra, str):
            raise ValueError("Cada palavra deve ser um texto (a palavra vazia é '').")

        for simbolo in palavra:
            if simbolo not in alfabeto:
                raise ValueError(
                    f"Símbolo '{simbolo}' da palavra '{palavra}' não pertence ao alfabeto"
                )
