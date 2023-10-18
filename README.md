# CRUD - Jogos Estudantis

## Intuito
Prover um sistema que seja capaz de gerenciar registros de jogadores, escolas, turmas, times e jogos para jogos estudantis (também conhecidos por jogos interclasses).

Vídeo de demonstração do CRUD: https://youtu.be/b7slwGl3_WU

## Execução do Sistema

Requisitos:
- Ambiente Linux;
- Banco de Dados Oracle.

### Passos para realização do CRUD

#### 1. Instalando Dependências

Certifique-se de instalar as dependências antes de executar o projeto, o arquivo requirements.txt contém todas elas. Para instalá-las, utilizando-se da ferramenta PIP, execute:

```
pip3 install -r requirements.txt
```

#### 2. Criando as tabelas e inserindo registros

Em um ambiente Linux, execute o seguinte script dentro da pasta crud-jogos-estudantis/src:

```
python3 script_criacao_tabelas_registros.py
```

O script deve informar que a criação das tabelas e inserções de dados ocorreram bem, caso isso não aconteça, verifique se o ambiente atende a todos os requisitos e que executou o comando para instalar as dependências.

#### 3. Execução do CRUD
```
python3 principal.py
```

Um menu aparecerá para que possa escolher as opções de CRUD bem como visualização dos relatórios de cada entidade do sistema.

## Estrutura de Pastas

[diagram](https://github.com/tbdje/crud-jogos-estudantis/tree/main/diagram): contém o diagrama relacional (modelo lógico de dados) e arquivos do mesmo para o SQL Power Architect.

[sql](https://github.com/tbdje/crud-jogos-estudantis/tree/main/sql): aqui estão todos os scripts de criação de tabelas e inserção de dados nas mesmas.

[src](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src): todos os elementos da lógica do sistema, dividos nas pastas:

+ [conexion](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/conexion): responsável pela conexão ao banco de dados Oracle (criado pelo nosso [professor](https://github.com/howardroatti/)).

+ [controller](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/controller): classes controladoras (inserção, atualização...).

+ [model](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/model): classes das entidades do banco de dados.

+ [reports](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/reports): contém a classe que auxilia na consulta pra visualização dos relatórios.

+ [sql](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/sql): toda a consulta para os relatórios que são usados pelo [reports](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/reports).

+ [utils](https://github.com/tbdje/crud-jogos-estudantis/tree/main/src/utils): contém as constantes dos menus, função de limpeza de terminal e a splash screen.