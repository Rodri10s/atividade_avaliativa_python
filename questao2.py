def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 3 and media < 7:
        return "Em Final"
    else:
        return "Reprovado"
        
while True:
    print("\n1 - Média e Situação do Aluno")
    print("2 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '2':
        break
    elif opcao == '1':
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        print(f"\nMedia do Aluno: {media(nota1, nota2, nota3):.2f}\nSituação do aluno: {situacao(media(nota1, nota2, nota3))}")
        continue
    
    