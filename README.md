# Simulador de Linguagens Regulares — AFN-ε

Trabalho desenvolvido para a disciplina de **Teoria da Computação** da Universidade Federal do Piauí (UFPI).

O projeto implementa um simulador de **Autômato Finito Não Determinístico com movimentos vazios (AFN-ε)**, utilizando Python.

O programa recebe a definição formal de um autômato por meio de um arquivo JSON e realiza o reconhecimento de uma lista de palavras, exibindo passo a passo os estados ativos durante a computação e indicando se cada palavra é aceita ou rejeitada.

## Funcionalidades

O programa permite:

- Carregar a definição de um autômato a partir de um arquivo JSON;
- Validar os dados fornecidos no arquivo de entrada;
- Calcular o fecho-ε de um conjunto de estados;
- Realizar transições a partir de um símbolo;
- Processar palavras em um AFN-ε;
- Mostrar os estados ativos iniciais, incluindo o fecho-ε;
- Mostrar os estados ativos após cada símbolo lido;
- Indicar se uma palavra foi aceita ou rejeitada;
- Mostrar a interseção entre os estados ativos finais e o conjunto de estados finais do autômato.

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
├── README.md
└── .gitignore
```

### `main.py`

Arquivo principal do programa, responsável por:

- Carregar os dados do arquivo JSON;
- Criar o objeto que representa o autômato;
- Exibir os dados do autômato;
- Processar todas as palavras definidas no arquivo de entrada.

### `automata.py`

Contém a classe `Automato`, responsável pela lógica de funcionamento do AFN-ε.

Principais métodos:

- `fecho_epsilon()` — calcula os estados alcançáveis utilizando apenas transições vazias;
- `mover()` — calcula os estados alcançáveis a partir de um conjunto de estados e de um símbolo;
- `reconhecer()` — realiza o processamento completo de uma palavra e informa se ela é aceita ou rejeitada.

### `leitor.py`

Responsável pela leitura e validação do arquivo JSON.

São verificados, entre outros pontos:

- Presença dos campos obrigatórios;
- Existência do estado inicial;
- Validade dos estados finais;
- Validade dos estados utilizados nas transições;
- Símbolos pertencentes ao alfabeto;
- Validade dos símbolos presentes nas palavras.

### `automato_exemplo.json`

Arquivo de entrada contendo a definição formal do autômato.

O arquivo contém:

- Conjunto de estados;
- Alfabeto;
- Estado inicial;
- Estados finais;
- Transições;
- Lista de palavras que serão processadas.

As transições vazias são representadas utilizando a chave `"epsilon"`.

Exemplo:

```json
"q0": {
    "epsilon": ["q1", "q2"]
}
```

### Arquivos de teste

- `test_automata.py` — testes dos algoritmos do autômato;
- `test_leitor.py` — testes da leitura e validação dos dados;
- `test_integracao.py` — testes da integração entre os componentes.

O arquivo `.gitignore` define arquivos e pastas que não devem ser rastreados pelo Git.

## Formato do Arquivo de Entrada

O programa utiliza um arquivo JSON estruturado com os elementos formais do AFN-ε.

Exemplo:

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

O arquivo pode ser modificado para representar outros AFN-ε, desde que sua estrutura seja mantida e os dados sejam válidos.

## Requisitos

Para executar o programa:

- Python 3 instalado;
- Terminal ou prompt de comando.

Para executar os testes automatizados, também é necessário instalar o `pytest`:

```bash
pip install pytest
```

O simulador utiliza recursos nativos do Python, não sendo necessária a instalação de bibliotecas externas para seu funcionamento principal.

## Como Executar

1. Extraia o arquivo ZIP do trabalho.
2. Abra o terminal na pasta que contém o arquivo `main.py`.
3. Execute:

```bash
python main.py
```

O programa carregará automaticamente o arquivo:

```text
automato_exemplo.json
```

Em seguida, processará todas as palavras presentes na lista `palavras` do JSON, apresentando o reconhecimento passo a passo.

## Como Testar Outros Autômatos

Para executar o simulador com outros autômatos:

1. Abra o arquivo `automato_exemplo.json` em um editor de texto ou código.
2. Modifique os estados, o alfabeto, o estado inicial, os estados finais e as transições de acordo com o novo autômato.
3. Atualize a lista `palavras` com as cadeias que deseja testar.
4. Salve o arquivo, mantendo a estrutura JSON.
5. Execute novamente:

```bash
python main.py
```

O simulador utilizará automaticamente as novas definições.

Também é possível criar outro arquivo JSON com a mesma estrutura. Nesse caso, basta alterar, em `main.py`, o caminho do arquivo de entrada para o novo arquivo.

**Importante:** os símbolos das palavras devem pertencer ao alfabeto definido, os estados utilizados nas transições devem existir no conjunto de estados e as transições vazias devem ser identificadas pela chave `"epsilon"`.

## Saída do Programa

O simulador não apresenta apenas o resultado final. Durante a computação, são exibidos:

- O conjunto inicial de estados ativos, incluindo o fecho-ε;
- O símbolo consumido em cada etapa;
- O novo conjunto de estados ativos;
- A interseção entre os estados ativos finais e os estados finais;
- O resultado do reconhecimento.

Exemplo de saída para a palavra `aab`:

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

A ordem de apresentação dos elementos de um conjunto pode variar.

Uma palavra é aceita quando, após o processamento de todos os símbolos, existe pelo menos um estado ativo pertencente ao conjunto de estados finais.

Formalmente:

```text
Estados ativos finais ∩ Estados finais ≠ ∅
```

Caso a interseção seja vazia, a palavra é rejeitada.

## Testes Automatizados

O projeto possui testes automatizados utilizando o framework `pytest`.

### `test_automata.py`

Verifica a lógica principal do autômato, incluindo:

- Cálculo do fecho-ε;
- Funcionamento do método `mover()`;
- Aceitação de palavras;
- Rejeição de palavras.

### `test_leitor.py`

Verifica a leitura e validação dos dados de entrada, incluindo:

- Autômato válido;
- Ausência de campos obrigatórios;
- Estado inicial inválido;
- Estado final inválido;
- Estado de origem inválido;
- Símbolo de transição inválido;
- Estado de destino inválido;
- Palavra contendo símbolo fora do alfabeto.

### `test_integracao.py`

Verifica o funcionamento conjunto dos componentes do programa:

```text
Arquivo JSON
     |
     v
  leitor.py
     |
     v
   Automato
     |
     v
Reconhecimento
     |
     v
   Resultado
```

## Executando os Testes

Abra o terminal na pasta do projeto e execute:

```bash
pytest -v
```

A suíte possui **13 testes automatizados**.

Quando todos os testes são executados corretamente, o resultado esperado inclui:

```text
13 passed
```

Os testes permitem verificar os principais comportamentos do simulador e identificar possíveis problemas na implementação.

## Implementação dos Algoritmos

Os algoritmos de rastreamento dos estados, processamento das transições e cálculo do fecho-ε foram implementados manualmente em Python.

O reconhecimento de cada palavra segue, de forma geral, estas etapas:

1. Calcula o fecho-ε do estado inicial;
2. Para cada símbolo da palavra, identifica os estados alcançáveis por esse símbolo;
3. Calcula o fecho-ε dos estados alcançados;
4. Atualiza e exibe o conjunto de estados ativos;
5. Ao terminar a palavra, verifica a interseção entre os estados ativos e os estados finais;
6. Apresenta o resultado de aceitação ou rejeição.

Não são utilizadas bibliotecas especializadas em autômatos, Teoria da Computação ou Teoria dos Grafos.

Toda a lógica de reconhecimento é implementada diretamente no código-fonte do projeto.