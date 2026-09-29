class Automato:
    def __init__(
        self,
        estados,
        alfabeto,
        estado_inicial,
        estados_finais,
        transicoes
    ):
        self.estados = set(estados)
        self.alfabeto = set(alfabeto)
        self.estado_inicial = estado_inicial
        self.estados_finais = set(estados_finais)
        self.transicoes = transicoes

    