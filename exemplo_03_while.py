def exemplo_lanchonete():
    # Solciitar o nome 6 vezes
    indice = 0
    # while indice <= 5: # executará 6
    # while indice != 5: # executará 6
    while indice < 6: # executará 6
        nome = input("Digite o nome: ")
        # Incrementar a variável indice em 1
        indice = indice + 1

def solicitar_numeros():
    indice = 0
    soma = 0
    while indice < 4: # 0..3
        numero = int(input("Digite o número: "))
        soma = soma + numero

        # if numero < 0:
        #     quantidade_negativo = quantidade_negativo + 1
        # if numero > 0:
        #     qunatidade_positivo = qunatidade_positivo + 1
        
        indice = indice + 1
    
    media = soma / indice
    print("Soma:", soma)
    print("Média:", media)


def solicitar_ate_fim():
    nome = ""
    while nome.lower() != "fim": # repetir até que o usuário digite 'fim'
        nome = input("Digite o nome do produto (fim para encerrar):").strip()
        

def descobrir_quantidade_por_categoria():
    quantidade_sc, quantidade_pr, quantidade_rs, quantidade_outros, indice = 0, 0, 0, 0, 0
    while indice < 6:
        cidade = input("Digite o nome da cidade: ")
        estado = input("Digite a sigla do estado: ").strip()
        if estado.lower() == "sc":
            quantidade_sc = quantidade_sc + 1
        elif estado.lower() == "pr":
            quantidade_pr = quantidade_pr + 1
        elif estado.lower() == "rs":
            quantidade_rs = quantidade_rs + 1
        else:
            quantidade_outros = quantidade_outros + 1
        indice = indice + 1

    print("Quantidade SC:", quantidade_sc)
    print("Quantidade PR:", quantidade_pr)
    print("Quantidade RS:", quantidade_rs)
    print("Quantidade outros:", quantidade_outros)


def solicitar_quantidade_desejada():
    indice = 0
    quantidade_desejada = int(input("Digite a quantidade desejada: "))
    while indice < quantidade_desejada:
        print("Olá mundo")
        indice = indice + 1

def descobrir_maior_salario():
    indice = 0
    maior_salario = 0.0
    while indice < 3:
        colaborador = input("Digite o nome do colab.: ").strip()
        salario = float(input("Digite o salário: "))

        if salario > maior_salario:
            maior_salario = salario

        indice = indice + 1
    
    print("Maior salário: ", maior_salario)

def descobrir_menor_salario():
    indice = 0
    menor_salario = 100000000.0
    while indice < 3:
        colaborador = input("Digite o nome do colab.: ").strip()
        salario = float(input("Digite o salário: "))

        if salario < menor_salario:
            menor_salario = salario

        indice = indice + 1
    
    print("Menor salário: ", menor_salario)

def descobrir_menor_salario_com_nome():
    indice = 0
    menor_salario = 100000000.0
    nome_menor_salario = ""
    while indice < 3:
        colaborador = input("Digite o nome do colab.: ").strip()
        salario = float(input("Digite o salário: "))

        if salario < menor_salario:
            menor_salario = salario
            nome_menor_salario = colaborador

        indice = indice + 1
    
    print("Colaborador: ", nome_menor_salario, " tem o menor salário: ", menor_salario)


def solicitar_dados_com_validacao():
    indice = 0
    while indice < 3:
        nome = input("Digite o nome: ").strip()
        while len(nome) < 3:
            print("Nome deve conter no mínimo 3 caracteres")
            nome = input("Digite o nome: ").strip()

        idade = int(input("Digite a idade: "))
        while idade < 0 or idade > 130: # enquanto for negativo ou maior que 130
            print("Idade deve ser maior ou igual a 0 e menor que 130 anos")
            idade = int(input("Digite a idade: "))

        indice = indice + 1
    

if __name__ == "__main__":
    solicitar_dados_com_validacao()