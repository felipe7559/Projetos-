quantidade_excelente = 0
quantidade_ruim = 0

print("--- Início da Pesquisa de Satisfação TudoWeb ---")

for i in range(1, 11):
    print(f"\nEntrevistado nº {i}")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opinião sobre o atendimento:")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = int(input("Sua opção: "))

    if opiniao == 1:
        quantidade_excelente = quantidade_excelente + 1
    elif opiniao == 3:
        quantidade_ruim = quantidade_ruim + 1
    elif opiniao == 2:
        pass
    else:
        print("Opção inválida! Esta resposta não será contabilizada.")

print("\n" + "="*30)
print("RESULTADO FINAL DA PESQUISA")
print(f"Total de respostas EXCELENTE: {quantidade_excelente}")
print(f"Total de respostas RUIM: {quantidade_ruim}")
print("="*30)
