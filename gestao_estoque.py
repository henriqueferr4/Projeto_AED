'''
Sistema de Gestão de estoque de loja e-commerce
-> O sistema deve ler um CSV de estoque
-> Atualizar o estoque cadastrando novas peças
-> Gerar uma lista de estoque ao usuário
-> Verificar quantos itens de determinado produto tem no estoque
-> Reduzir item do estoque quando lançada compra
'''

# Ler o CSV de estoque - OK
def ler_estoque():
    estoque = []
    with open("estoque.csv", "r") as arq:
        for linha in arq:
            estoque.append(linha.strip().split(";"))
    return estoque

# Cadastrar novos produtos - OK 
def cadastrar_produto(estoque):
    with open("estoque.csv", "a") as arq:
        while True:
            acao = input("Cadastrar novo produto (1 - Sim / 2 - Não): ")
            if acao == "1":
                codigo = input("Código: ").strip()
                nome = input("Nome: ").strip()
                quantidade = input("Quantidade: ").strip()

                # Adiciona o novo produto ao arquivo
                arq.write(f"{codigo};{nome};{quantidade}\n")

                print("Produto cadastrado com sucesso.")
            elif acao == "2":
                print("Cadastro de produto finalizado.")
                break
            else:
                print("Opção inválida.")

# Gerar uma lista com as informações atuais do estoque
def lista_estoque(estoque):
    saida = ""
    for produto in estoque:
        saida += f"Código: {produto[0]} Nome: {produto[1]} Quantidade: {produto[2]}\n"
    return saida

# Verificar quantidade de produtos em estoque - OK
def verificar_quant(estoque):
    produto = input("Nome do produto: ")
    for i in estoque:
        if i[1] == produto:
            return f"Quantidade atual: {i[2]}"
    return "Produto não encontrado"

# Lançamento de vendas
def venda(estoque):
    produto = input("Produto vendido: ")
    quantidade = int(input("Quantidade vendida: "))
    
    encontrado = False

    for i in estoque:
        if i[1] == produto:
            encontrado = True
            i[2] = str(int(i[2]) - quantidade)
            break

    if not encontrado:
        return "Produto não encontrado"

    with open("estoque.csv", "w") as arq:
        for produto in estoque:
            arq.write(f"{produto[0]};{produto[1]};{produto[2]}\n")
    return "Venda realizada com sucesso."


# Utilização do sistema
print("Bem-vindo ao Sistema de Gestão de Estoque")
print("Selecione uma das opções abaixo:")
print("0 - Verificar estoque")
print("1 - Cadastrar um novo produto")
print("2 - Verificar a quantidade disponível de um produto")
print("3 - Lançar uma venda")
print("4 - Sair")
print("\n")

estoque = ler_estoque()

while True:
    acao = input("Opção: ")
    if acao == '0':
        print(lista_estoque(estoque))
    elif acao == '1':
        cadastrar_produto(estoque)
        estoque = ler_estoque()  # Atualiza o estoque após o cadastro
    elif acao == '2':
        print(verificar_quant(estoque))
    elif acao == '3':
        print(venda(estoque))
        estoque = ler_estoque()  # Atualiza o estoque após a venda
    elif acao == '4':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
