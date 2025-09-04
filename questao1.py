eleitores = []

def cadastrar():
    print("\nCadastro de Eleitores")
    nome = input("Digite o nome do eleitor: ")
    titulo = input("Digite o Número do Título do eleitor: ")
    cidade = input("Digite a Cidade do eleitor: ")
    eleitor = [nome, titulo, cidade] 
    eleitores.append(eleitor)

def listar_todos():
    print("\nListar Todos os Eleitores")
    if len(eleitores) == 0:
        print("Nenhum eleitor cadastrado.")
    else:
        print("Lista de Eleitores:")
        for i in eleitores:
            print(f"Nome: {i[0]}, Título: {i[1]}, Cidade: {i[2]}")

def buscar_cidade():
    print("\nBuscar Eleitor por Cidade")
    cidade = input("Digite o nome da Cidade: ")
    encontrado = False
    for eleitor in eleitores:
        if cidade == eleitor[2]:
            print(f"Nome: {eleitor[0]}, Título: {eleitor[1]}, Cidade: {eleitor[2]}")
            encontrado = True
    
    if encontrado == False:
        print("Cidade não encontrada")

def buscar_titulo():
    print("\nBuscar Eleitor por Título")
    titulo = input("Digite o Número do Título do Eleitor: ")
    encontrado = False
    for eleitor in eleitores:
        if titulo == eleitor[1]:
            print(f"Nome: {eleitor[0]}, Título: {eleitor[1]}, Cidade: {eleitor[2]}")
            encontrado = True
    
    if encontrado == False:
        print("Título de Eleitor não encontrado")

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Eleitor")
        print("2. Buscar Eleitor por Cidade")
        print("3. Listar Todos os Eleitores")
        print("4. Buscar Eleitor por Título")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            buscar_cidade()
        elif opcao == '3':
            listar_todos()
        elif opcao == '4':
            buscar_titulo()
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, tente novamente.")

main()