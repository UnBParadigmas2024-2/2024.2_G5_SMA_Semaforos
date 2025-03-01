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

<p align=justify>
Este trabalho tem como objetivo explorar o uso do paradigma de sistemas multiagentes (MAS - Multi-Agent Systems) por meio da simulação de tráfego urbano. Para isso, foi utilizado o framework MESA, uma poderosa biblioteca Python voltada para a modelagem e simulação de agentes em ambientes discretos.
</p>

<p align=justify>
Na simulação, agentes representam veículos que interagem em um ambiente composto por ruas, semáforos e cruzamentos. Cada agente possui comportamentos autônomos, como deslocar-se em uma direção específica, respeitar sinais de trânsito e evitar colisões com outros veículos. O ambiente é gerenciado de forma descentralizada, destacando a aplicação prática do paradigma multiagente para resolver problemas complexos, como o gerenciamento do fluxo de tráfego.
</p>

<p align=justify>
Este projeto demonstra como conceitos fundamentais de sistemas multiagentes, como autonomia, interação e adaptação, podem ser aplicados em contextos reais, promovendo uma compreensão mais aprofundada do paradigma estudado.
</p>

## Uso e Screenshots

### Excutando o servidor:

![GIF Local](./assets/start.gif)

### Em funcionamento:
![GIF Local](./assets/exec.gif)

## Instalação 
**Linguagens**: Python 3.11 ou superior<br>
**Tecnologias**: MESA<br>

Para instalar o MESA e suas dependências, utilize o seguinte comando:
```
pip3 install -r requirements.txt
```
Para executar o projeto, na pasta raiz, basta executar o servidor:
```
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

Clique [aqui](https://youtu.be/mfGSf5s1wrk) para assistir o vídeo.


## Participações
Apresente, brevemente, como cada membro do grupo contribuiu para o projeto.

|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) | Comprobatórios (ex. links para commits) |
| -- | -- | -- | -- |
| Danilo Domingo Vitoriano Silva  | Criação da primeira versão de inputs para os usuários | Boa  | [Inputs](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/52b73985d9828450e2a2137aa9e90d6686de9c86)
| Gabrielly Assunção | Agentes de semáforos, alternância entre os estados e estruturação do documento | Execelente | https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/bd225ddeeaa09a0ea0b20788fb65cd7aae3181ca, https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/4e6dfb674faf0a88fc716e86fd72e31e4cde4128, https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/d83a5369dd24bb5df3f8cc28b5272e0d237b2632
| Jackes Fonseca | Atuei na criação do documento de estudo e análise do paradigma e projeto | Regular | [https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/e0a871bbdfe273fed054729fad55f4d8a8685051](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/9be54153aa2ea26f8fd6df49b3253d0b35dccb70)
| Karla Feliciano   | Interação do carro com outros agentes | Boa | [Commit](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/0fc1f29e38bfed4d8906a175e949549bef200b9c)
| Lucas Medeiros Rosa | Implementei o agente pedestre e adicionei o sistema de colisões com carros | Excelente | [Commit](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/9b55a4b2c7fd07cea6ffde18dc5364a39518ada8) 
| Luís Furtado de Araújo  | Criação e possibilidade de escalar os posicionamentos no mapa: buildings, traffic lights e intersections nas traffics cells. Documentação fix do problema comum das dependências do meta que está descrita neste Readme. | Boa | [Error installing Mesa](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/b3ee6118350b717d2857cdb6c513e2b19b1ab2da), [Regra dinâmica para as ruas](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/9cc01811dd26d05954ec747f32b887d01cfaec00), [Regras de interseção dinâmicas](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/6bbb6c92fa8f9990517e01a186cce9d3a6a01731)
| Vinícius Roriz | Criação das classes TrafficLightAgent, CarAgent, TrafficModel, TrafficCell. Implementação dos parâmetros de modelo.  | Excelente | [Semáforos](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/52b73985d9828450e2a2137aa9e90d6686de9c86), [Carro](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/76f5d374567221b6649e8ba7957c738bba4b82ae), [Parâmetros](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/commit/f5a05af0178064b05223b7710e1cee0a4d65ef91)

## Outros 
### I. Licões Aprendidas

#### Danilo Domingo

<p align=justify>
Foi um experiência bem diferente do convencional, a onde tive que aprender como cada agente se comporta a entrar em contato com outro e como eles podem trabalhar de forma autônoma.
</p>

#### Gabrielly Assunção

<p align=justify>
Minha principal tarefa foi desenvolver a lógica que gerencia a alternância entre os estados (verde, amarelo e vermelho) de forma sincronizada e eficiente. Durante esse processo, enfrentei dificuldades em compreender o paradigma de sistemas multiagentes, pois trata-se de uma abordagem descentralizada que exige uma mudança de mentalidade em relação aos paradigmas mais tradicionais de programação. Essa experiência me ajudou a desenvolver uma nova perspectiva sobre como os agentes podem interagir de maneira autônoma
</p>

#### Jackes Fonseca

<p align=justify>
Durante o desenvolvimento deste trabalho, diversas lições foram adquiridas, como por exemplo Compreensão do paradigma multiagente e modelagem de cenários realistas, uso de ferramentas e Frameworks e impacto dos parâmetros no desempenho
</p>

#### Karla Feliciano
Apesar de ser um paradigma bastante diferente, utilizar o framework mesa facilitou bastante o entendimento de como os agentes funcionam e interagem entre si.

#### Lucas Medeiros

<p align=justify>
Acredito que a maior lição que tive com essa atividade foi o cuidado necessário para modelar os diferentes comportamentos e interações entre os agentes.
Dificilmente em outros paradigmas é tão necessário avaliar os corner cases e prever comportamentos emergentes.
</p>

#### Luís Furtado

<p align=justify>
O uso da ferramenta Mesa no desenvolvimento dos agentes nos reforçou a relevância da descentralização em determinados contextos de sistemas. Observamos que, embora cada agente opere de forma independente, as dinâmicas coletivas entre eles podem gerar fenômenos inesperados, como padrões no fluxo de tráfego e formação de congestionamentos.
</p>

#### Vinícius Roriz

<p align=justify>
Trabalhar com agentes autônomos destacou a importância da descentralização em sistemas complexos. Cada agente toma decisões localmente, mas as interações entre eles geram comportamentos emergentes, como congestionamentos e padrões de fluxo no tráfego.
</p>

### II. Percepções

<p align=justify>
Este trabalho demonstrou a aplicabilidade do paradigma multiagente (MAS) na simulação de
tráfego urbano, evidenciando como a interação entre agentes pode fornecer uma visão
detalhada e realista de fenômenos complexos, como congestionamentos e padrões de fluxo. O
modelo implementado destacou-se pela capacidade de representar comportamentos individuais
e suas interações no ambiente simulado, permitindo a análise de métricas relevantes, como
tempo médio de viagem, tempos de espera em cruzamentos e padrões de congestionamento.
Os resultados mostraram que o uso de sistemas multiagentes oferece uma ferramenta flexível
e adaptável para explorar soluções de mobilidade urbana, além de abrir caminhos para
aplicações em planejamento de infraestrutura e gestão de tráfego em tempo real. A
implementação utilizando o framework MESA reforçou a simplicidade e eficiência na criação de
cenários customizados, contribuindo para o aprendizado e experimentação no campo da
simulação.
Além disso, o trabalho evidenciou os desafios inerentes a simulações realistas, como a
necessidade de calibrar parâmetros adequados e as limitações computacionais quando se lida
com cenários de grande escala.
</p>

### Análise do Paradigma

Confira o [documento de estudo e análise do paradigma sistemas multiagentes](https://github.com/UnBParadigmas2024-2/2024.2_G5_SMA_Semaforos/blob/9be54153aa2ea26f8fd6df49b3253d0b35dccb70/docs/Sistemas%20multiagentes.docx.pdf), que explora os fundamentos teóricos e práticos desse modelo computacional, destacando sua aplicação na simulação de tráfego urbano com o framework MESA.

### III. Contribuições e Fragilidades

#### Danilo Domingo

<p align=justify>
Fiz a primeira versão de inputs, a onde os usuários informavam a quantidade de carros, tamanho do mapa, etc, porém com o desenvolvimento do código ele precisou ser refatorado para que se adequasse melhor aos novos parâmetros.
</p>

#### Gabrielly Assunção

<p align=justify>
Minha contribuição principal foi a implementação do agente semáforo e o desenvolvimento da lógica de interação entre os estados de verde, amarelo e vermelho, que são cruciais para a simulação do fluxo de tráfego.Entretanto, uma das fragilidades que enfrentei foi a minha dificuldade inicial em compreender e aplicar o paradigma multiagente de maneira eficiente. A descentralização e a autonomia dos agentes foram conceitos desafiadores de assimilar no início do projeto, especialmente em relação ao entendimento de como as interações locais resultam em comportamentos no sistema global.
</p>

#### Jackes Fonseca

<p align=justify>
Atuei na criação do documento de estudo e análise do paradigma e projeto.
</p>

#### Karla Feliciano
Atuei na implementação de funcionalidades da integração do carro com outros agentes, adicionando algumas regras e validações para adequar ao cenário do mundo real.

#### Lucas Medeiros

<p align=justify>
Idealizei e implementei a adição do agente pedestre no sistema, modelando seu comportamento de andar e definindo as eurísticas de movimentação.
Além disso também implementei a colisão entre carros e pedestres, e por fim refatorei o código completo do projeto que antes estava em apenas um arquivo.
</p>

#### Luís Furtado

<p align=justify>
Trabalhei na criação e escalabilidade dinâmica dos posicionamentos no mapa: buildings, traffic lights e intersections nas traffics cells. Além disso, contribui na documentação do readme também do fix das dependências do meta que está descrita neste Readme.
</p>

#### Vinícius Roriz

<p align=justify>
Trabalhei na conceitualização do projeto e na implementação básica dos agentes e do modelo. A maior parte do tempo foi gasto pesquisando a documentação pois os exemplos disponíveis no repositório do MESA utilizam uma versão mais antiga, e muito foi alterado desde então.  
Também fiquei responsável pela correção de erros no código e a refatoração de algumas implementações.
</p>

### IV. Trabalhos Futuros

Embora o modelo atual tenha alcançado seus objetivos iniciais, há diversas possibilidades de
extensão e aprimoramento que podem ampliar o impacto e a aplicabilidade prática do trabalho.
Entre elas:
Expansão do modelo para incluir pedestres e ciclistas:
A inclusão de agentes representando pedestres e ciclistas permitiria analisar a interação entre
diferentes modos de transporte, contribuindo para o planejamento de soluções mais inclusivas
e seguras para todos os usuários das vias urbanas. Essa expansão poderia incluir a simulação
de faixas exclusivas, cruzamentos compartilhados e o impacto de medidas como passarelas e
ciclovias.
- **Avaliação de políticas de tráfego diversificadas:**
Simulação de rodízio de veículos para reduzir congestionamentos em horários de pico.
Avaliação de estratégias para mudanças dinâmicas no tempo dos semáforos, considerando
diferentes horários do dia ou condições de tráfego em tempo real.
Testes de impacto de novas políticas públicas, como tarifas de congestionamento urbano (e.g.,
pedágio em áreas centrais) ou incentivos ao transporte coletivo.
- **Integração com aprendizado de máquina:**
O uso de aprendizado de máquina pode ajudar a melhorar a adaptação dos agentes,
permitindo que aprendam a reagir de forma mais eficiente às mudanças no ambiente de
tráfego. Isso incluiria a capacidade de prever congestionamentos e ajustar
comportamentos em tempo real.
- **Simulação de redes urbanas reais:**
A aplicação do modelo em redes viárias reais, utilizando dados provenientes de fontes
como OpenStreetMap ou sistemas de monitoramento de tráfego, poderia validar ainda
mais sua aplicabilidade e relevância prática.
- **Otimização computacional e escalabilidade:**
Investir em técnicas de paralelismo e distribuição de carga, utilizando tecnologias como
MPI ou integração com a nuvem, permitiria simular cenários maiores e mais complexos
sem comprometer o desempenho.
- **Aplicação em contextos emergentes de mobilidade:**
Investigar o impacto de novas tecnologias, como veículos autônomos e sistemas de
carona compartilhada, no tráfego urbano. Esses cenários poderiam fornecer insights
sobre como preparar as cidades para o futuro da mobilidade

## Fontes

> [MESA API Documentation](https://mesa.readthedocs.io/stable/apis/api_main.html).  Acesso em: 22 jan. 2024.

> [MESA Introductory Tutorial](https://mesa.readthedocs.io/stable/tutorials/intro_tutorial.html#).  Acesso em: 22 jan. 2024.

> [MESA Visualization Tutorial](https://mesa.readthedocs.io/stable/tutorials/visualization_tutorial.html).  Acesso em: 23 jan. 2024.

> [MESA Examples: Conway's Game of Life (Fast)](https://github.com/projectmesa/mesa-examples/tree/main/examples/conways_game_of_life_fast).  Acesso em: 25 jan. 2024.

> [MESA Migration Guide](https://mesa.readthedocs.io/latest/migration_guide.html).  Acesso em: 25 jan. 2024.

- A maior parte dos exemplos disponíveis na internet foram criados usando o MESA 2.0. No *Migration Guide* estão listadas as mudanças que ocorreram no update 3.0, que é o que estamos utilizando.
