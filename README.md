# Semáforos

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T01 <br>
**Número do Grupo**: 05<br>
**Paradigma**: Sistemas Multiagentes<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0015311 |  Danilo Domingo |
| 20/0018442 |  Gabrielly Assunção |
| 19/0030291 |  Jackes Fonseca |
| 20/0021541 |  Karla Chaiane  |
| 17/0039803 | Lucas Medeiros Rosa |
| 18/0042661 | Luís Furtado de Araújo |
| 19/0020814 |  Vinícius Roriz |

## Sobre 
Este trabalho tem como objetivo explorar o uso do paradigma de sistemas multiagentes (MAS - Multi-Agent Systems) por meio da simulação de tráfego urbano. Para isso, foi utilizado o framework MESA, uma poderosa biblioteca Python voltada para a modelagem e simulação de agentes em ambientes discretos.

Na simulação, agentes representam veículos que interagem em um ambiente composto por ruas, semáforos e cruzamentos. Cada agente possui comportamentos autônomos, como deslocar-se em uma direção específica, respeitar sinais de trânsito e evitar colisões com outros veículos. O ambiente é gerenciado de forma descentralizada, destacando a aplicação prática do paradigma multiagente para resolver problemas complexos, como o gerenciamento do fluxo de tráfego.

Este projeto demonstra como conceitos fundamentais de sistemas multiagentes, como autonomia, interação e adaptação, podem ser aplicados em contextos reais, promovendo uma compreensão mais aprofundada do paradigma estudado.

## Uso e Screenshots

## Instalação 
**Linguagens**: Python 3.11 ou superior<br>
**Tecnologias**: MESA<br>

Para instalar o MESA e suas dependências, utilize o seguinte comando:
```
pip3 install -r requirements.txt
```
Para executar o projeto, entre na pasta `src` e execute o servidor:
```
cd src
solara run server.py
```

### Erros

Se durante a instalação de dependências ocorrer o erro `error: externally-managed-environment`,    
significa que o mesa é uma dependência gerenciada externamente. Para isso, instale as dependências utilizando uma virtualenv no projeto:

```
python3 -m venv semaforos
source semaforos/bin/activate
python3 -m pip install -r requirements.txt
```

É imperativo o uso de uma versão do Python equivalente ou superior à 3.11, caso contrário ocorrem diversos erros que impedem a execução do projeto.

## Vídeo

Clique [aqui]() para assistir o vídeo.


## Participações
Apresente, brevemente, como cada membro do grupo contribuiu para o projeto.
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) | Comprobatórios (ex. links para commits)
| -- | -- | -- | -- |
| Danilo Domingo Vitoriano Silva  |  |  |
| Gabrielly Assunção |  |  |
| Jackes Fonseca | Atuei na criação do documento de estudo e análise do paradigma e projeto | Regular | 
| Karla Feliciano   |  |  |
| Lucas Medeiros Rosa | |  | 
| Luís Furtado de Araújo  |  |  |
| Vinícius Roriz | |  | 

## Outros 
### I. Licões Aprendidas

#### Danilo Domingo

#### Gabrielly Assunção

#### Jackes Fonseca
Durante o desenvolvimento deste trabalho, diversas lições foram adquiridas, como por exemplo Compreensão do paradigma multiagente e modelagem de cenários realistas, uso de ferramentas e Frameworks e impacto dos parâmetros no desempenho

#### Karla Feliciano

#### Lucas Medeiros

#### Luís Furtado

#### Vinícius Roriz

### II. Percepções

### III. Contribuições e Fragilidades

#### Danilo Domingo

#### Gabrielly Assunção

#### Jackes Fonseca
Atuei na criação do documento de estudo e análise do paradigma e projeto.

#### Karla Feliciano

#### Lucas Medeiros

#### Luís Furtado

#### Vinícius Roriz

### IV. Trabalhos Futuros


## Fontes

> [MESA API Documentation ](https://mesa.readthedocs.io/stable/apis/api_main.html).  Acesso em: 22 jan. 2024.

> [MESA Introductory Tutorial](https://mesa.readthedocs.io/stable/tutorials/intro_tutorial.html#).  Acesso em: 22 jan. 2024.

> [MESA Visualization Tutorial](https://mesa.readthedocs.io/stable/tutorials/visualization_tutorial.html).  Acesso em: 23 jan. 2024.

> [MESA Examples: Conway's Game of Life (Fast)](https://github.com/projectmesa/mesa-examples/tree/main/examples/conways_game_of_life_fast).  Acesso em: 25 jan. 2024.

> [MESA Migration Guide](https://mesa.readthedocs.io/latest/migration_guide.html).  Acesso em: 25 jan. 2024.

- A maior parte dos exemplos disponíveis na internet foram criados usando o MESA 2.0. No *Migration Guide* estão listadas as mudanças que ocorreram no update 3.0, que é o que estamos utilizando.
