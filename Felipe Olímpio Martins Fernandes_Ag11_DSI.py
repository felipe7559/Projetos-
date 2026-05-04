from colorama import Fore, Style, init

init()

def exibir_status_reservatorio(nivel):
    situacoes = [
        "Muito baixo (crítico)",
        "Baixo",
        "Médio",
        "Alto",
        "Muito alto (alerta)"
    ]

    indice = nivel - 1
    mensagem = situacoes[indice]

    if nivel == 1:
        cor = Fore.RED
    elif nivel == 2:
        cor = Fore.YELLOW
    elif nivel == 3:
        cor = Fore.GREEN
    elif nivel == 4:
        cor = Fore.CYAN
    elif nivel == 5:
        cor = Fore.BLUE
    else:
        return

    print(f"Nível {nivel}: {cor}{mensagem}{Style.RESET_ALL}")

def simular_monitoramento():
    print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
    
    niveis_para_teste = [1, 2, 3, 4, 5]
    
    for n in niveis_para_teste:
        exibir_status_reservatorio(n)
    
    print("-------------------------------------------------")

if __name__ == "__main__":
    simular_monitoramento()
    