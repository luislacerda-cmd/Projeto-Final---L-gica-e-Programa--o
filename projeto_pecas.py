pecas_aprovadas = []
pecas_reprovadas = []
caixas_fechadas = []
caixa_atual = []


def id_existe(id_peca):
    for peca in pecas_aprovadas:
        if peca["id"] == id_peca:
            return True

    for peca in pecas_reprovadas:
        if peca["id"] == id_peca:
            return True

    return False
# TRABALHO DE LÓGICA

def avaliar_peca(peso, cor, comprimento):
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("peso fora do padrão")

    if cor != "azul" and cor != "verde":
        motivos.append("cor inválida")

    if comprimento < 10 or comprimento > 20:
        motivos.append("comprimento fora do padrão")

    if len(motivos) == 0:
        return True, "peça aprovada"
    else:
        return False, ", ".join(motivos)


def reorganizar_caixas():
    global caixas_fechadas, caixa_atual

    caixas_fechadas = []
    caixa_atual = []
    numero_caixa = 1

    for peca in pecas_aprovadas:
        caixa_atual.append(peca)

        if len(caixa_atual) == 10:
            caixas_fechadas.append({
                "numero": numero_caixa,
                "pecas": caixa_atual.copy()
            })
            caixa_atual = []
            numero_caixa += 1


def cadastrar_peca():
    print("\n=== CADASTRO DE PEÇA ===")

    id_peca = input("Digite o ID da peça: ").upper()

    if id_existe(id_peca):
        print("Já existe uma peça cadastrada com esse ID.")
        return

    peso = float(input("Digite o peso da peça (em gramas): "))
    cor = input("Digite a cor da peça: ").lower()
    comprimento = float(input("Digite o comprimento da peça (em cm): "))

    aprovada, motivo = avaliar_peca(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento
    }

    if aprovada:
        pecas_aprovadas.append(peca)
        reorganizar_caixas()
        print("\nPeça APROVADA.")
    else:
        peca["motivo"] = motivo
        pecas_reprovadas.append(peca)
        print("\nPeça REPROVADA.")
        print("Motivo:", motivo)


def listar_pecas():
    print("\n=== PEÇAS APROVADAS ===")

    if len(pecas_aprovadas) == 0:
        print("Nenhuma peça aprovada cadastrada.")
    else:
        for peca in pecas_aprovadas:
            print(
                "ID:", peca["id"],
                "| Peso:", peca["peso"],
                "| Cor:", peca["cor"],
                "| Comprimento:", peca["comprimento"]
            )

    print("\n=== PEÇAS REPROVADAS ===")

    if len(pecas_reprovadas) == 0:
        print("Nenhuma peça reprovada cadastrada.")
    else:
        for peca in pecas_reprovadas:
            print(
                "ID:", peca["id"],
                "| Peso:", peca["peso"],
                "| Cor:", peca["cor"],
                "| Comprimento:", peca["comprimento"],
                "| Motivo:", peca["motivo"]
            )


def remover_peca():
    print("\n=== REMOVER PEÇA ===")
    id_remover = input("Digite o ID da peça que deseja remover: ").upper()

    for i in range(len(pecas_aprovadas)):
        if pecas_aprovadas[i]["id"] == id_remover:
            del pecas_aprovadas[i]
            reorganizar_caixas()
            print("Peça removida da lista de aprovadas.")
            return

    for i in range(len(pecas_reprovadas)):
        if pecas_reprovadas[i]["id"] == id_remover:
            del pecas_reprovadas[i]
            print("Peça removida da lista de reprovadas.")
            return

    print("Peça não encontrada.")


def listar_caixas_fechadas():
    print("\n=== CAIXAS FECHADAS ===")

    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa fechada até o momento.")
    else:
        for caixa in caixas_fechadas:
            print(f"\nCaixa {caixa['numero']}:")
            for peca in caixa["pecas"]:
                print(f"- ID da peça: {peca['id']}")


def gerar_relatorio():
    print("\n=== RELATÓRIO FINAL ===")

    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_caixas_fechadas = len(caixas_fechadas)

    if len(caixa_atual) > 0:
        total_caixas_utilizadas = total_caixas_fechadas + 1
    else:
        total_caixas_utilizadas = total_caixas_fechadas

    print("Total de peças aprovadas:", total_aprovadas)
    print("Total de peças reprovadas:", total_reprovadas)
    print("Quantidade de caixas fechadas:", total_caixas_fechadas)
    print("Quantidade total de caixas utilizadas:", total_caixas_utilizadas)

    if len(caixa_atual) > 0:
        print("Peças na caixa atual (ainda aberta):", len(caixa_atual))
    else:
        print("Não há caixa aberta no momento.")

    if len(pecas_reprovadas) > 0:
        print("\nMotivos das reprovações:")
        for peca in pecas_reprovadas:
            print("-", peca["id"], ":", peca["motivo"])
    else:
        print("\nNão houve peças reprovadas.")


def menu():
    while True:
        print("\n==============================")
        print(" SISTEMA DE CONTROLE DE PEÇAS ")
        print("==============================")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
