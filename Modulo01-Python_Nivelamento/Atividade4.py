'''
ATIVIDADE 4 - EM GRUPO
Objetivo: Desenvolver competências técnicas na manipulação de
vetores e listas.
Você deve escrever um programa que permita ao usuário gerenciar um
vetor de números inteiros. O programa deve oferecer um menu com as
seguintes opções:
Adicionar um número ao vetor.
Remover um número do vetor.
Exibir o vetor completo.
Encontrar e exibir o maior e o menor número no vetor.
Calcular e exibir a soma de todos os números no vetor.
Sair.

Obs: O programa deve continuar exibindo o menu até que o usuário
escolha a opção de sair.

Requisitos:
Utilizar vetores (listas) para armazenar os números inteiros.
Utilizar laços for para iterar sobre os vetores quando necessário.

Exemplo de Interação:
Menu:
1. Adicionar um número
2. Remover um número
3. Exibir o vetor completo
4. Encontrar e exibir o maior e o menor número
5. Calcular e exibir a soma de todos os números
6. Sair

Escolha uma opção: 1
Digite o número para adicionar: 5

Menu:
1. Adicionar um número
2. Remover um número
3. Exibir o vetor completo
4. Encontrar e exibir o maior e o menor número
5. Calcular e exibir a soma de todos os números
6. Sair

Escolha uma opção: 3
O vetor completo é: [5]

Menu:
1. Adicionar um número
2. Remover um número
3. Exibir o vetor completo
4. Encontrar e exibir o maior e o menor número
5. Calcular e exibir a soma de todos os números
6. Sair

'''

vetor = []

while True:
    print("Menu:")
    print("1. Adicionar um número")
    print("2. Remover um número")
    print("3. Exibir o vetor completo")
    print("4. Encontrar e exibir o maior e o menor número")
    print("5. Calcular e exibir a soma de todos os números")
    print("6. Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    match opcao:
        case 1:
            numero = int(input("Digite o número para adicionar: "))
            vetor.append(numero)
            print(f"O número {numero} foi adicionado ao vetor.\n")
        
        case 2:
            numero = int(input("Digite o número para remover: "))
            if numero in vetor:
                vetor.remove(numero)
                print(f"O número {numero} foi removido do vetor.\n")
            else:
                print(f"O número {numero} não está no vetor.\n")
        
        case 3:
            print(f"O vetor completo é: {vetor}\n")
        
        case 4:
            if vetor:
                maior = vetor[0]
                menor = vetor[0]
                for num in vetor:
                    if num > maior:
                        maior = num
                    if num < menor:
                        menor = num
                print(f"O maior número no vetor é: {maior}")
                print(f"O menor número no vetor é: {menor}\n")
            else:
                print("O vetor está vazio.\n")
        
        case 5:
            soma = 0
            for num in vetor:
                soma += num
            print(f"A soma de todos os números no vetor é: {soma}\n")
        
        case 6:
            print("Saindo do programa...")
            break
        
        case _:
            print("Opção inválida. Tente novamente.\n")
