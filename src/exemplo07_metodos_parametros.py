# Encapsulamento: é a forma que temos para proteger métodos, variávies......
# Método privados: Método que será utilizado somente no arquivo atual, 
#                  tem como prefixo '__calcular()', '_calcular()'
# Métodos públicos: Método que será utilizado em qualquer outro arquivo
def __solicitar_numero1() -> int:
    numero01 = int(input("Digite o número 1: "))
    return numero01


def __solicitar_numero2() -> int:
    numero02 = int(input("Digite o número 2: "))
    return numero02


# Método com retorno do tipo inteiro que recebe dois parâmetros:
# O primeiro chama-se numero1 que é do tipo inteiro
# O segundo chama-se numero2 que é do tipo inteiro
# Como chamar(executar) métodos que tem parâmetros? somar(20, 2)
def __somar(numero1: int, numero2: int) -> int:
    soma = numero1 + numero2
    return soma

def __solicitar_nome_colaborador() -> str:
    nome_colaborador = input("Digite o nome do colaborador: ")
    return nome_colaborador

def __solicitar_horas_trabalhadas() -> int:
    horas_trabalhadas = 0
    while horas_trabalhadas <= 0:
        try:
            horas_trabalhadas = int(
                input("Digite a quantidade de horas trabalhadas: ").strip()
            )
        except ValueError as error:
            print("A quantidade de horas deve ser um número inteiro")
    
    return horas_trabalhadas

def __solicitar_cargo() -> str:
    cargos_disponiveis = ["Junior", "Pleno", "Senior"]

    cargo = ""
    while cargo not in cargos_disponiveis:
        cargo = input("Digite o cargo: ")
        if cargo not in cargos_disponiveis:
            print("Cargo inválido, cargos disponíveis:", cargos_disponiveis)
    return cargo

def __obter_valor_hora_por_cargo(cargo: str) -> float:
    valor_hora = 0
    if cargo == "Junior":
        valor_hora = 9.09
    elif cargo == "Pleno":
        valor_hora = 18.18
    else:
        valor_hora = 36.36
    return valor_hora


def __obter_aliquota_imposto_renda(salario_bruto: float) -> float:
    if salario_bruto <= 2259.20:
        aliquota = 0
    elif salario_bruto <= 2826.65:
        aliquota = 0.075 # 7.5%
    elif salario_bruto <= 3751.05:
        aliquota = 0.15 # 15%
    elif salario_bruto <= 4664.68:
        aliquota = 0.225 # 22.5
    else:
        aliquota = 0.275 # 27.5
    return aliquota

def __calcular_imposto_de_renda(salario_bruto: float):
    aliquota = __obter_aliquota_imposto_renda(salario_bruto)
    imposto_renda = salario_bruto * aliquota
    return imposto_renda

# def __calcular_salario_bruto(valor_hora: float, horas_trabalhadas: int):
def __calcular_salario_bruto(
    horas_trabalhadas: int, valor_hora: float,
) -> float:
    valor_salario_bruto = valor_hora * horas_trabalhadas
    return valor_salario_bruto

def __apresentar_dados(
    colaborador: str, 
    horas_trabalhadas: int, 
    cargo: str, 
    valor_hora: float, 
    salario_bruto: float, 
    imposto_renda: float,
    salario_liquido: float,
):
    print("Colaborador:", colaborador)
    print("Quantidade de horas trabalhadas:", horas_trabalhadas)
    print("Cargo:", cargo)
    print("Valor hora:", valor_hora)
    print("Salário Bruto:", salario_bruto)
    print("Imposto renda:", imposto_renda)
    print("Salário Líquido:", salario_liquido)

def __calcular_salario_liquido(salario_bruto: float, descontos: float) -> float:
    salario_liquido = salario_bruto - descontos
    return salario_liquido


# Método de entrada para calcular a folha de pagamento do usuário
def calcular_folha_pagamento():
    colaborador = __solicitar_nome_colaborador()
    horas_trabalhadas = __solicitar_horas_trabalhadas()
    cargo = __solicitar_cargo()

    valor_hora = __obter_valor_hora_por_cargo(cargo)
    salario_bruto = __calcular_salario_bruto(horas_trabalhadas, valor_hora)
    
    imposto_renda = __calcular_imposto_de_renda(salario_bruto)
    descontos = imposto_renda # + inss + vale_passe
    salario_liquido = __calcular_salario_liquido(salario_bruto, descontos)
    # salarioBruto => camelCase => não usa em python
    # SalarioBruto => PascalCase => nome de Classes
    # salario_bruto => snake_case => nome de variáveis, funções
    # SALARIO_BRUTO => SCREAMING_SNAKE_CASE => nome de constantes
    

    # calcular salário bruto: horas trabalhadas, cargo => valor hora
    # calcular salário líquido: salario bruto - descontos
    __apresentar_dados(
        colaborador, 
        horas_trabalhadas, 
        cargo, 
        valor_hora, 
        salario_bruto, 
        imposto_renda,
        salario_liquido,
    )


def calculadora():
    numero1 = __solicitar_numero1()
    numero2 = __solicitar_numero2()

    soma = __somar(numero1, numero2)

    print("Número 1:", numero1)
    print("Número 2:", numero2)
    print("Soma:", soma)
