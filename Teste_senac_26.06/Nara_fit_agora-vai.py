Alunos = []   
print('#' * 20, 'BEM VINDO A NARA FIT', '#' * 20)

while True:
    print("1 - Cadastrar novo aluno")
    print("2 - Listar todos os alunos")
    print("3 - Ver estatisticas da academia")
    print("3 - Sair")
    opcao = int(input("Escolha uma opcao: "))

    

    if opcao == 1:
        nome_aluno = input('Digite o nome do aluno: ').title()
        idade_aluno = int(input("Digite a idade do aluno: "))
        peso_aluno = float(input("Digite o peso do aluno: "))
        altura_aluno = float(input("Digite a altura do aluno: "))
        Alunos.append(nome_aluno, idade_aluno, peso_aluno, altura_aluno)
        
    elif opcao == 2:
        for i in Alunos:
            print(i)







        