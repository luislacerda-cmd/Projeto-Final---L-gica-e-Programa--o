# Projeto: Sistema de Controle de Peças Industriais

## Descrição

Este projeto foi desenvolvido em Python para simular o controle de qualidade de peças em uma linha de produção industrial.

O sistema permite cadastrar peças, verificar se elas foram aprovadas ou reprovadas de acordo com critérios definidos, armazenar as peças aprovadas em caixas com capacidade máxima de 10 unidades e gerar um relatório final com os resultados do processo.

Este projeto foi desenvolvido como atividade da disciplina de Algoritmos e Lógica de Programação.

---

## Objetivo

O objetivo do sistema é ajudar no controle de peças produzidas, permitindo:

- cadastrar novas peças;
- verificar se cada peça atende aos padrões de qualidade;
- separar peças aprovadas e reprovadas;
- armazenar as peças aprovadas em caixas;
- listar caixas fechadas;
- gerar um relatório final da produção.

---

## Funcionalidades do sistema

O programa possui as seguintes opções no menu:

1. Cadastrar nova peça  
2. Listar peças aprovadas e reprovadas  
3. Remover peça cadastrada  
4. Listar caixas fechadas  
5. Gerar relatório final  
0. Sair  

---

## Regras de aprovação da peça

Uma peça será considerada **aprovada** quando atender a todos os critérios abaixo:

- **Peso** entre **95g e 105g**
- **Cor** igual a **azul** ou **verde**
- **Comprimento** entre **10cm e 20cm**

Caso algum desses critérios não seja atendido, a peça será **reprovada** e o sistema mostrará o motivo da reprovação.

---

## Regras de armazenamento em caixas

- Somente peças **aprovadas** são armazenadas em caixas.
- Cada caixa pode guardar no máximo **10 peças**.
- Quando a caixa atinge 10 peças, ela é considerada **fechada**.
- O sistema cria automaticamente uma nova caixa para continuar o armazenamento das próximas peças aprovadas.

---

## Tecnologias utilizadas

- **Python 3**
- Execução em **terminal / IDLE**
- Estruturas básicas de programação:
  - variáveis
  - listas
  - dicionários
  - funções
  - condicionais (`if`, `elif`, `else`)
  - repetição com `while`

---

## Como executar o projeto

### 1. Instalar o Python
Baixe e instale o Python no computador.

### 2. Abrir o arquivo do projeto
Abra o arquivo:

```python
projeto_pecas.py
```

### 3. Executar o programa
No IDLE, clique em:

**Run > Run Module**

ou pressione:

**F5**

---

## Exemplo de uso

### Exemplo de peça aprovada

- ID: `P001`
- Peso: `100`
- Cor: `azul`
- Comprimento: `15`

Resultado:

```text
Peça APROVADA.
```

### Exemplo de peça reprovada

- ID: `P003`
- Peso: `110`
- Cor: `vermelha`
- Comprimento: `8`

Resultado:

```text
Peça REPROVADA.
Motivo: peso fora do padrão, cor inválida, comprimento fora do padrão
```

---

## Exemplo de relatório final

O relatório final informa:

- total de peças aprovadas;
- total de peças reprovadas;
- quantidade de caixas fechadas;
- quantidade total de caixas utilizadas;
- quantidade de peças na caixa atual;
- motivos das reprovações.

Exemplo:

```text
=== RELATÓRIO FINAL ===
Total de peças aprovadas: 2
Total de peças reprovadas: 1
Quantidade de caixas fechadas: 0
Quantidade total de caixas utilizadas: 1
Peças na caixa atual (ainda aberta): 2

Motivos das reprovações:
- P003 : peso fora do padrão, cor inválida, comprimento fora do padrão
```

---

## Estrutura geral do programa

O programa foi organizado com funções para facilitar a leitura e o entendimento.

Principais funções:

- `id_existe()`  
  Verifica se já existe uma peça cadastrada com o mesmo ID.

- `avaliar_peca()`  
  Analisa se a peça está aprovada ou reprovada.

- `reorganizar_caixas()`  
  Organiza as peças aprovadas dentro das caixas.

- `cadastrar_peca()`  
  Recebe os dados da peça e faz a validação.

- `listar_pecas()`  
  Mostra as peças aprovadas e reprovadas.

- `remover_peca()`  
  Remove uma peça cadastrada pelo ID.

- `listar_caixas_fechadas()`  
  Exibe as caixas que já foram fechadas.

- `gerar_relatorio()`  
  Mostra o resumo final da produção.

- `menu()`  
  Controla a navegação entre as opções do sistema.

---

## Observações

- O sistema não permite cadastrar duas peças com o mesmo ID.
- IDs são convertidos para letras maiúsculas para facilitar o controle.
- O projeto foi desenvolvido com foco didático, utilizando recursos básicos de Python adequados para iniciantes.

---

## Autor

**Nome do aluno:** Luis Henrique Lacerda  
**Disciplina:** Algoritmos e Lógica de Programação  
**Curso:** Graduação Tecnológica em Inteligência Artificial e Automação Digital  
**Instituição:** UniFecaf
