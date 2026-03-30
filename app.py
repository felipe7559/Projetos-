
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência em watts (W): "))
horas_dia = float(input("Digite as horas de uso por dia: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75

print("\n--- Resultado do Cálculo ---")
print(f"Aparelho: {nome_aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}")
