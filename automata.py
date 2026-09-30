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

    def fecho_epsilon(self,estados):
        fecho = set(estados)
        pilha = list(estados)

        while pilha:
            estado = pilha.pop()

            # Busca as transições epsilon do estado atual; se não existirem, retorna uma lista vazia
            destinos = self.transicoes.get(estado, {}).get("epsilon", [])

            for destino in destinos:
                if destino not in fecho:
                    fecho.add(destino)
                    pilha.append(destino)
        return fecho

    def mover(self, estados, simbolo):
        destinos = set()

        for estado in estados:
            # Busca os estados alcançáveis pelo símbolo atual a partir de cada estado ativo
            transicoes_simbolo = self.transicoes.get(estado, {}).get(simbolo, [])

            for destino in transicoes_simbolo:
                destinos.add(destino)

        return destinos

        

    