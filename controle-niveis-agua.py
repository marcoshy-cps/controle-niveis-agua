from colorama import Fore, Style, init

init()

# Níveis do reservatório com a situação
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"}
]

def obter_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    return Fore.WHITE

def exibir_painel():
    print("=" * 45)
    print("   SISTEMA DE MONITORAMENTO DE RESERVATÓRIO   ")
    print("=" * 45)

    for item in niveis_reservatorio:
        nivel = item["nivel"]
        situacao = item["situacao"]
        cor = obter_cor(nivel)
        print(f"{cor}[Nível {nivel}] - Situação: {situacao}")

    print(Style.RESET_ALL + "=" * 45)

if __name__ == "__main__":
    exibir_painel()