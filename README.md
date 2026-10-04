# Simulador de Linguagens Regulares — AFN-ε

Trabalho desenvolvido para a disciplina de **Teoria da Computação** da Universidade Federal do Piauí (UFPI).

O projeto implementa um simulador de **Autômato Finito Não Determinístico com movimentos vazios (AFN-ε)**.

O programa recebe a definição de um autômato por meio de um arquivo JSON e realiza o reconhecimento de uma lista de palavras, exibindo passo a passo os estados ativos durante a computação.

## Funcionalidades

O programa permite:

- carregar a definição de um autômato a partir de um arquivo JSON;
- validar os dados fornecidos no arquivo de entrada;
- calcular o fecho-ε de um conjunto de estados;
- realizar transições a partir de um símbolo;
- processar palavras em um AFN-ε;
- mostrar os estados ativos após cada símbolo lido;
- indicar se uma palavra foi aceita ou rejeitada;
- mostrar a interseção entre os estados ativos finais e os estados finais do autômato.

## Estrutura do Projeto

```text
trabalho-01-teoria-da-computacao/
│
├── main.py
├── automata.py
├── leitor.py
├── automato_exemplo.json
├── test_automata.py
├── test_leitor.py
├── test_integracao.py
└── README.md
```

### `main.py`

Arquivo principal do programa.

É responsável por:

- carregar os dados do arquivo JSON;
- criar o objeto que representa o autômato;
- exibir os dados do autômato;
- processar todas as palavras definidas no arquivo de entrada.

### `automata.py`

Contém a classe `Automato`, responsável pela lógica de funcionamento do AFN-ε.

Possui os principais métodos:

- `fecho_epsilon()` — calcula todos os estados alcançáveis utilizando apenas transições epsilon;
- `mover()` — calcula os estados alcançáveis a partir de um conjunto de estados e de um símbolo;
- `reconhecer()` — realiza o processamento completo de uma palavra e informa se ela é aceita ou rejeitada.

### `leitor.py`

Responsável pela leitura e validação do arquivo JSON.

São verificados, entre outros pontos:

- presença dos campos obrigatórios;
- existência do estado inicial;
- validade dos estados finais;
- validade dos estados utilizados nas transições;
- símbolos pertencentes ao alfabeto;
- validade dos símbolos presentes nas palavras.

### `automato_exemplo.json`

Arquivo de entrada contendo a definição formal do autômato.

O arquivo contém:

- conjunto de estados;
- alfabeto;
- estado inicial;
- estados finais;
- transições;
- palavras que serão processadas.

As transições vazias são representadas no JSON utilizando:

```json
"epsilon"
```

Exemplo:

```json
"q0": {
    "epsilon": ["q1", "q2"]
}
```

## Formato do Arquivo de Entrada

Exemplo de estrutura:

```json
{
    "estados": ["q0", "q1", "q2", "q3"],
    "alfabeto": ["a", "b"],
    "estado_inicial": "q0",
    "estados_finais": ["q3"],

    "transicoes": {
        "q0": {
            "epsilon": ["q1", "q2"]
        },
        "q1": {
            "a": ["q1"],
            "b": ["q3"]
        },
        "q2": {
            "a": ["q3"],
            "b": ["q2"]
        },
        "q3": {}
    },

    "palavras": [
        "aab",
        "bba",
        "aaa",
        "bbb",
        "ab",
        "ba"
    ]
}
```

O arquivo pode ser alterado para representar outros AFN-ε, desde que a mesma estrutura seja mantida.

## Requisitos

- Python 3
- pytest, apenas para execução dos testes automatizados

Para instalar o pytest:

```bash
pip install pytest
```

## Como Executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

O programa carregará automaticamente o arquivo:

```text
automato_exemplo.json
```

e processará todas as palavras presentes nele.

## Saída do Programa

O simulador não apresenta apenas o resultado final.

Durante o processamento, são mostrados os estados ativos a cada etapa da computação.

Exemplo:

```text
Palavra: aab

Estados ativos iniciais (fecho-ε): {'q0', 'q1', 'q2'}

Símbolo lido: a
Estados ativos: {'q1', 'q3'}

Símbolo lido: a
Estados ativos: {'q1'}

Símbolo lido: b
Estados ativos: {'q3'}

Interseção com estados finais: {'q3'}
Resultado: ACEITA
```

Uma palavra é aceita quando, após o processamento de todos os seus símbolos, existe pelo menos um estado ativo pertencente ao conjunto de estados finais.

Formalmente, a palavra é aceita quando:

```text
Estados ativos finais ∩ Estados finais ≠ ∅
```

Caso a interseção seja vazia, a palavra é rejeitada.

## Testes Automatizados

O projeto possui testes automatizados utilizando o framework `pytest`.

### `test_automata.py`

Testa a lógica principal do autômato, incluindo:

- cálculo do fecho-ε;
- função `mover`;
- aceitação de palavras;
- rejeição de palavras.

### `test_leitor.py`

Testa a validação dos dados de entrada, incluindo:

- autômato válido;
- ausência de campos obrigatórios;
- estado inicial inválido;
- estado final inválido;
- estado de origem inválido;
- símbolo de transição inválido;
- estado de destino inválido;
- palavra contendo símbolo fora do alfabeto.

### `test_integracao.py`

Testa o funcionamento conjunto dos componentes:

```text
JSON
 ↓
leitor.py
 ↓
Automato
 ↓
reconhecimento da palavra
 ↓
resultado
```

## Executando os Testes

Na pasta do projeto, execute:

```bash
pytest -v
```

Atualmente, a suíte possui **13 testes automatizados**.

O resultado esperado é:

```text
13 passed
```

## Implementação

Os algoritmos utilizados para rastreamento de estados, transições e cálculo do fecho-ε foram implementados manualmente.

Não são utilizadas bibliotecas especializadas em autômatos, Teoria da Computação ou Teoria dos Grafos.