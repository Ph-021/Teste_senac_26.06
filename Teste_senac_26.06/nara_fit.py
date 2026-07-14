'''products =




print("#" * 20, "WELCOME TO THE NARA HORTI-FRUT", "#" * 20)

while True:
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        escolha_produto = input("Digite o produto: ")
        products.append(escolha_produto)
    elif opcao == 2:
        if len(products) == 0:
            print("Nenhum profuto foi cadastrado")

    elif opcao == 3:

    else:
'''



produtos = []   
print('#' * 20, 'BEM VINDO A NARA HORTI FRUTI', '#' * 20)

while True:
    print("1 - Adicionar item")
    print("2 - Listar itens")
    print("3 - Sair")
    opcao = int(input("Escolha uma opcao: "))

    if opcao == 1:
        escolha_produto = input('Digite o produto que deseja ').title()
        produtos.append(escolha_produto)
    elif opcao == 2:
        if len(produtos) == 0:
            print('Nenhum produto cadastrado') 
        else:
            for i in produtos:
                print(f'Produto {i}')
    elif opcao == 3:
        break
    else:
        print('Escolha uma opção válida')