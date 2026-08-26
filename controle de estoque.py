produtos=[]

def cadastrar_produto():
    print("=== Cadastro de Produto ===")

    try:
        nome=input("Digite o nome do produto: ")
        if nome=="":
            print("o nome nao pode ser vazio")
            return
        codigo=int(input('digite o codigo do produto: '))
        if codigo<=0:
            print("o codigo nao pode ser menor ou igual a zero")
            return
        preço=float(input("digite o valor do produto:"))
        if preço<=0:
            print("o preço nao pode ser menor ou igual a zero")
            return
        quantidade=int(input("digite a quantidade do produto: "))
        if  quantidade<0:
            print("a quantidade nao pode ser menor que zero")
            return
        produto={"nome":nome,
                 "codigo":codigo,
                 "preço":preço,
                 "quantidade":quantidade,
                    }
        produtos.append(produto) 
        print("produto cadastrado com sucesso")           
    except ValueError:
        print("entrada invalida,por favor digite um valor valido")


def calcular_total_produtos():
    total=0
    for produto in produtos:
        total+=produto["quantidade"]
    print(f"total de produtos cadastrados: {total}")


while True:
    print("=== Controle de Estoque ===")
    print("1-cadastrar_produto")
    print("2-calcular_total_produtos")
    print("3-sair")

    opcao=input("digite a opcao desejada: ")
    if opcao=="1":
        cadastrar_produto()
    elif opcao=="2":
        calcular_total_produtos()
    elif opcao=="3":
        print("saindo do programa...")
        break
    else:
        print("opcao invalida,por favor digite uma opcao valida")

        
