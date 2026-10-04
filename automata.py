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

    def fecho_epsilon(self, estados):
        fecho = set(estados)
        pilha = list(estados)

        while pilha:
            estado = pilha.pop()

            # Busca as transições epsilon do estado atual.
            destinos = self.transicoes.get(
                estado,
                {}
            ).get("epsilon", [])

            for destino in destinos:
                if destino not in fecho:
                    fecho.add(destino)
                    pilha.append(destino)

        return fecho

    def mover(self, estados, simbolo):
        destinos = set()

        for estado in estados:
            # Busca os estados alcançáveis pelo símbolo atual
            # a partir de cada estado ativo.
            transicoes_simbolo = self.transicoes.get(
                estado,
                {}
            ).get(simbolo, [])

            for destino in transicoes_simbolo:
                destinos.add(destino)

        return destinos

    def reconhecer(self, palavra):
        estados_ativos = self.fecho_epsilon(
            {self.estado_inicial}
        )

        print(f"\nPalavra: {palavra}")
        print(
            "Estados ativos iniciais (fecho-ε): "
            f"{estados_ativos}"
        )

        for simbolo in palavra:
            estados_ativos = self.mover(
                estados_ativos,
                simbolo
            )

            estados_ativos = self.fecho_epsilon(
                estados_ativos
            )

            print(f"Símbolo lido: {simbolo}")
            print(f"Estados ativos: {estados_ativos}")

        intersecao = estados_ativos & self.estados_finais

        if intersecao:
            print(
                "Interseção com estados finais: "
                f"{intersecao}"
            )
            print("Resultado: ACEITA")
            return True

        print("Interseção com estados finais: ∅")
        print("Resultado: REJEITADA")
        return False