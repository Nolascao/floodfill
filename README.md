# Flood Fill em Grid 2D

## Integrantes:

- Ana Carolina de Carvalho Corrêa - ana.correa.1313117@sga.pucminas.br

- Júlia Evelyn de Oliveira Silva - jeosilva@sga.pucminas.br

- Matheus Nolasco Miranda Soares - matheus.nolasco@sga.pucminas.br

- Pedro Talma Toledo - pedrotoledo1717@gmail.com

## Descrição do Projeto

Este projeto implementa o algoritmo **Flood Fill** para identificar e preencher regiões conectadas em um grid bidimensional (2D). O programa utiliza uma abordagem baseada em **busca em largura (BFS)** para explorar células navegáveis a partir de uma célula inicial, preenchendo-as com uma cor específica. Ele também mapeia automaticamente todas as regiões conectadas no grid, atribuindo cores distintas a cada região.

O objetivo é resolver problemas relacionados à identificação de áreas conectadas em grids, como mapas de terrenos, imagens binárias ou representações de grafos, respeitando obstáculos e limites do grid.

## Introdução ao Problema

Em muitos cenários computacionais, é necessário identificar e preencher regiões conectadas em uma matriz ou grid 2D. Por exemplo:

- Em jogos, para detectar áreas acessíveis ao jogador.
- Em processamento de imagens, para segmentar objetos em uma imagem binária.
- Em sistemas de simulação, para modelar terrenos navegáveis.

O problema consiste em encontrar todas as células conectadas a uma célula inicial e preenchê-las com uma cor específica, respeitando os limites do grid e quaisquer obstáculos. Este projeto resolve esse problema utilizando o Algoritmo **Flood Fill**, amplamente utilizado em ferramentas de edição gráfica e análise de dados espaciais.

## Configuração e Execução

### Pré-requisitos

- Python 3.7 ou superior.
- Biblioteca padrão do Python (`collections` é usada).

### Como Configurar

1. Clone este repositório ou copie os arquivos do projeto para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina. Você pode verificar a versão instalada com:

```sh
python --version
```

### Como Executar

1. Navegue até o diretório do projeto.
2. Execute o script principal com o comando:

```sh
python main.py
```

3. Siga as instruções interativas para fornecer:
    - As dimensões do grid (número de linhas e colunas).
    - O grid inicial, linha por linha (valores separados por espaço).
    - As coordenadas iniciais da célula onde o preenchimento começará.

4. O programa exibirá o grid atualizado, com as regiões preenchidas.

## Funcionamento do Algoritmo Flood Fill

### Entrada Inicial

Um grid 2D composto por valores inteiros:

- `0`: Representa células navegáveis (áreas vazias).
- `1`: Representa obstáculos (células não navegáveis).
- Coordenadas iniciais `(x, y)` indicando onde o preenchimento começa.
- Uma cor inicial para preencher a região conectada.

### Exploração do Grid

A partir da célula inicial `(x, y)`, o algoritmo verifica todas as células vizinhas (cima, baixo, esquerda, direita).

Se uma célula vizinha for navegável (`0`) e estiver dentro dos limites do grid, ela é preenchida com a cor fornecida e adicionada à fila de exploração.

### Respeito aos Limites e Obstáculos

- O algoritmo garante que nenhuma célula fora dos limites do grid seja acessada.
- Células com valor diferente de `0` (obstáculos ou já preenchidas) são ignoradas.

### Preenchimento Automático de Regiões

O programa identifica automaticamente todas as regiões conectadas no grid e as preenche com **cores distintas**, incrementando a cor para cada nova região encontrada.

### Saída Final

O grid atualizado é exibido, mostrando todas as regiões preenchidas com cores diferentes.

## Exemplo de Funcionamento

### Exemplo 1: Grid Pequeno

**Entrada**:  
Dimensões do grid: `5 5`  
Grid inicial:

```
0 0 1 0 0  
0 1 1 0 0  
0 0 1 1 1  
1 1 0 0 0  
0 0 0 1 1  
```

Coordenadas iniciais: `0 0`

**Saída**:  
Grid atualizado:

```
2 2 1 3 3  
2 1 1 3 3  
2 2 1 1 1  
1 1 4 4 4  
4 4 4 1 1  
```

---

### Exemplo 2: Grid Médio

**Entrada**:  
Dimensões do grid: `6 6`  
Grid inicial:

```
0 0 1 1 0 0  
0 1 1 1 0 0  
1 1 0 0 1 1  
1 0 0 1 1 1  
0 0 1 1 0 0  
0 0 0 0 0 1  
```

Coordenadas iniciais: `0 0`

**Saída**:  
Grid atualizado:
```
(Exemplo da saída formatada do grid atualizado)
```
