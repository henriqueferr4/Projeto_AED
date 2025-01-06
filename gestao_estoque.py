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
    
    arq = open("estoque.csv", "r")

    produtos = arq.readlines()

    estoque = []

    for linha in produtos:
        estoque.append(linha.split(";"))

    return estoque

# Cadastrar novos produtos - OK 
def cadastrar_produto(estoque):
    arq = open("estoque.csv", "a")

    cadastrar = True
    while cadastrar == True:
        acao = input("Cadastrar novo produto (1 - Sim / 2 - Nao): ")
        if acao == "1":
            novo_produto = []

            codigo = input("Código: ")
            nome = input("Nome: ")
            quantidade = input("Quantidade: ")

            novo_produto.append(codigo)
            novo_produto.append(nome)
            novo_produto.append(quantidade)

            arq.write(f"{novo_produto[0]};{novo_produto[1]};{novo_produto[2]}\n")

            return "Produdo cadastrado com sucesso."
        
        elif acao == "2":
            cadastrar == False
            return "Cadastro de produto finalizado."

        else:
            cadastrar = False
            return "Opção inválida."

#Gerar uma lista com as informações atuais do estoque - ESTA MOSTRANDO SO A PRIMEIRA LINHA
def lista_estoque(estoque):
    
    for produto in estoque: 
        return f"Código: {produto[0]} Nome: {produto[1]} Quantidaede: {produto[2]} \n"
               
# Verificar quantidade de produtos em estoque - OK

def verificar_quant(estoque):

    produto = input("Nome do produto: ")
    
    encontrado = False

    for i in estoque:
        if i[1] == produto:
            encontrado = True
            return f"Quantidade atual: {i[2]}"
        
        else: 
           continue

    if encontrado == False:
        return "Produto nao encontrado" #Caso o produto digitado não seja encontrado
        
# Lançamento de vendas - COMO COLOCAR NOVA LINHA "\n" apenas no produto que foi lancada a venda?
def venda(estoque):

    produto = input("Produto vendido: ")
    quantidade = int(input("Quantidade vendida: "))

    encontrado = False

    for i in estoque: 
        if i[1] == produto:
            encontrado = True
            i[2] = int(i[2]) - quantidade
            break
        
        else:
            continue
    if encontrado == False:
        return "Produto nao encontrado"
    
    arq = open("estoque.csv", "w")

    for produto in estoque:
         arq.write(f"{produto[0]};{produto[1]};{produto[2]}") #Atualiza a quantidade no arquivo
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

while True:
    acao = input("Opção: ")
    
    if acao == '0':

        estoque = ler_estoque()

        saida = lista_estoque(estoque)
        
        print(saida)

    elif acao == '1':

        estoque = ler_estoque()

        cadastro = cadastrar_produto(estoque)

        print(cadastro)
        
    elif acao == '2':

        estoque = ler_estoque()

        saida_quant = verificar_quant(estoque)

        print(saida_quant)

    elif acao == '3':

        estoque = ler_estoque()
        
        lancamento = venda(estoque)

        print(lancamento)

    elif acao == '4':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
        break