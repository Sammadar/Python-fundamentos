def tratar_erro_conversao_string_nao_inteira():
    # Tentar executar um trecho de código que sabemos que poderá acontecer algum erro
    try: # tente
        # convertendo o que o usuário digitou de str para int e sabemos que pode acontecer algum erro
        numero = int(input("Digite o número: "))
    except Exception as erro: # quando ocorrer algum erro executa o código daqui de dentro do except
        print("Deu erro na conversão do número")
        # Caso desejar apresentar a mensagem do erro
        print("Mensagem do erro: ", erro)

    # Apresentar essa mensagem dando erro ou não
    print("Programa finalizado com sucesso")


def tratar_divisao_com_multiplos_except():
    try:
        numero1 = int(input("Digite o número 1: "))
        numero2 = int(input("Digite o número 2: "))
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    except ZeroDivisionError as erro: # cai aqui quando ocorrer erro na divisão
        print("Não é possível realizar a divisão por 0")
    except ValueError as erro: # cai aqui quando ocorrer erro na conversão
        print("Não foi possível converter o número para inteiro")
    except Exception as erro: # cai aqui com qualquer tipo de erro, caso n tiver sido tratado nos excepts anteriores
        print("Ocorreu um erro inesperado")

    print("Encerrou a aplicação com sucesso")


# ✔ Solicitar até que o usuário digite sair
# ✔ Solicitar os seguintes dados:
#   ✔ - nome do curso: str
#   ✔   Validar min: 8
#   ✔   Validar max: 20
#   ✔ - quantidade_alunos: int
#   ✔   Validar erro de conversão (try except)
#   ✔   Validar min: 5
#   ✔   Validar max: 20
def exemplo_curso():
    opcao: str = ""
    while opcao.strip().upper() != "SAIR":
        # Solicitar os dados do nome do curso
        nome: str = input("Digite o nome do curso: ").strip()
        while len(nome) < 8 or len(nome) > 20:
            print("Nome deve conter no mínimo 8 e no máximo 20 caracteres")
            nome = input("Digite o nome do curso: ").strip()

        quantidade_alunos: int = 0
        quantidade_valida = False
        while quantidade_valida == False:
            try:
                quantidade_alunos: int = int(input("Digite a quantidade de alunos: "))
                # if quantidade_alunos < 5 or quantidade_alunos > 20:
                #     print("A quantidade mínima de alunos é 5 e a máxima é 20")
                #     continue

                if quantidade_alunos < 5:
                    print("A quantidade mínima de alunos para uma turma é 5")
                    continue
                
                if quantidade_alunos > 20:
                    print("A quantidade máxima de alunos para uma turma é 20")
                    continue

                quantidade_valida = True
            except Exception as erro:
                print("A quantidade de alunos deve ser um número inteiro")

        opcao = input("Pressione enter para continuar ou digite 'sair' para encerrar... ")


if __name__ == "__main__":
    import os 
    os.system("cls")
    exemplo_curso()


# Ex. 1: Solicitar um número inteiro e apresentar se ele é menor que 15 ou maior que 15
num = int(input("Digite um número inteiro: "))
if num < 15:
    print("O número é menor que 15")
else:
    print("O número é maior que 15")

# Ex. 2: Solicitar o nome de um animal e apresentar a quantidade de caracteres
animal = input("Digite o nome de um animal: ")
print("A quantidade de caracteres no nome do animal é: " + str(len(animal)))

# Ex. 3: Solicitar um texto, remover espaços do começo transformando em minúsculo
texto = input("Digite um texto: ").strip().lower()
print("Texto após remoção de espaços e transformação para minúsculo: " + texto)

# Ex. 4: Solicitar o nome de uma empresa e remover o texto 'LTDA', assim como, 'SA'.
empresa = input("Digite o nome de uma empresa: ").replace(" LTDA", "").replace(" SA", "")
print("Nome da empresa após remoção de 'LTDA' ou 'SA': " + empresa)

# Ex. 5: Solicitar o nome do curso e apresentar se o curso começa com SuperDev, caso contrário apresentar que não começa com SuperDev
curso = input("Digite o nome do curso: ")
if curso.startswith("SuperDev"):
    print("O curso começa com SuperDev")
else:
    print("O curso não começa com SuperDev")

# Ex. 6: Solicitar uma idade e apresentar se é:
#   - Adulto
#   - Criança
#   - Adolescente
#   - Idoso
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 60:
    print("Adulto")
else:
    print("Idoso")

#  UTILIZAR WHILE para estes exercícios abaixo:
# Ex. 7: Solicitar o nome da empresa e verificar se termina com LTDA, apresentar que é uma empresa 'Sociedade de responsabilidade limitada', caso terminar com SA apresentar que é uma empresa 'Sociedade Anônima
empresa = input("Digite o nome da empresa: ")
if empresa.endswith("LTDA"):
    print("Sociedade de responsabilidade limitada")
elif empresa.endswith("SA"):
    print("Sociedade Anônima")
else:
    print("Outro tipo de empresa")

# Ex. 8: Solicitar 5 vezes o nome do dia da semana
dias = []
for i in range(5):
    dia = input("Digite o nome do " + str(i+1) + "º dia da semana: ")
    dias.append(dia)
print("Dias da semana cadastrados:", dias)

# Ex. 9: Solicitar o nome da cidade e a quantidade de habitantes para quatro cidades.
for i in range(4):
    cidade = input("Digite o nome da cidade " + str(i+1) + ": ")
    habitantes = int(input("Digite a quantidade de habitantes da cidade " + cidade + ": "))
    print("A cidade " + cidade + " tem " + str(habitantes) + " habitantes.")

# Ex. 10: Solicitar o nome e altura de 6 alunos, descobrir  qual a maior altura e apresentar
maior_altura = 0
nome_maior = ""
for i in range(6):
    nome = input("Digite o nome do " + str(i+1) + "º aluno: ")
    altura = float(input("Digite a altura de " + nome + ": "))
    if altura > maior_altura:
        maior_altura = altura
        nome_maior = nome
print("O aluno com a maior altura é " + nome_maior + " com " + str(maior_altura) + "m.")

# Ex. 11: Solicitar nome e preço de 5 notebooks, descobrir qual o nome e o valor do notebook que tem o menor preço
menor_preco = float('inf')
nome_menor_preco = ""
for i in range(5):
    nome = input("Digite o nome do " + str(i+1) + "º notebook: ")
    preco = float(input("Digite o preço do " + nome + ": "))
    if preco < menor_preco:
        menor_preco = preco
        nome_menor_preco = nome
print("O notebook com o menor preço é " + nome_menor_preco + " com o preço de R$" + str(menor_preco) + ".")

# Ex. 12: Solicitar o preço do petróleo e tratar o erro (neste não precisa de while, somente try/except)
try:
    preco_petroleo = float(input("Digite o preço do petróleo: "))
    print("O preço do petróleo é R$" + str(preco_petroleo) + ".")
except ValueError:
    print("Erro: Por favor, digite um valor numérico válido para o preço.")

# Ex. 12: Solicitar o peso da carne e tratar o erro (neste precisa de while e try/except)
while True:
    try:
        peso_carne = float(input("Digite o peso da carne: "))
        print("O peso da carne é " + str(peso_carne) + "kg.")
        break
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para o peso.")

# Ex. 13: Solicitar o salário do pedreiro (neste precisa de while e try/catch), passos para resolver:
#         Solicitar o salário
#         Adicionar o try/except
#         Fazer com que repita com while
#         Validar que o salário mínimo é de R$ 4000,00
#         Validar que o salário máximo é R$ 15000,00
while True:
    try:
        salario = float(input("Digite o salário do pedreiro: "))
        if salario < 4000 or salario > 15000:
            print("Erro: O salário deve ser entre R$4000,00 e R$15000,00.")
        else:
            print("O salário do pedreiro é R$" + str(salario) + ".")
            break
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para o salário.")

# Ex. 13: Solicitar nome do projeto, categoria e seu custo, apresentar conforme abaixo:
#           - Quantidade de projetos da categoria 'Cross Fit'
#           - Quantidade de projetos da categoria 'Pilates'
#           - Quantidade de projetos da categoria 'Fisioculturismo'
projetos = {'Cross Fit': 0, 'Pilates': 0, 'Fisioculturismo': 0}
while True:
    nome_projeto = input("Digite o nome do projeto (ou 'fim' para sair): ")
    if nome_projeto.lower() == 'fim':
        break
    categoria = input("Digite a categoria do projeto (Cross Fit, Pilates, Fisioculturismo): ")
    custo = float(input("Digite o custo do projeto: "))
    
    if categoria in projetos:
        projetos[categoria] += 1

print("Quantidade de projetos 'Cross Fit': " + str(projetos['Cross Fit']))
print("Quantidade de projetos 'Pilates': " + str(projetos['Pilates']))
print("Quantidade de projetos 'Fisioculturismo': " + str(projetos['Fisioculturismo']))

# Ex. 14: Solicitar nome, nota 1, nota 2 e nota 3 até que o usuário digite 'fim'.
# Ex. 14: (continuação) Calcular a média das notas e apresentar.
# Ex. 14: (continuação) Descobrir qual o status da média e apresentar
#        Critérios de média:
#        Até 4.99 reprovado
#        Até 6.99 em exame
#        Até 10 aprovado
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor nota 1
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior nota 2
# Ex. 14: (continuação) Descobrir e apresentar qual é a maior média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar qual é a menor média e o nome do aluno
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que tem "Enzo" em seu nome
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o nome começa com "Valentina"
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é reprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é aprovado
# Ex. 14: (continuação) Descobrir e apresentar quantidade de alunos que o status é em exame
alunos = []
while True:
    nome = input("Digite o nome do aluno (ou 'fim' para sair): ")
    if nome.lower() == 'fim':
        break
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    media = (nota1 + nota2 + nota3) / 3
    if media < 5:
        status = "Reprovado"
    elif media <= 6.99:
        status = "Em Exame"
    else:
        status = "Aprovado"
    
    alunos.append({'nome': nome, 'media': media, 'status': status, 'nota1': nota1, 'nota2': nota2, 'nota3': nota3})

# Cálculos e apresentações adicionais podem ser feitos com base na lista de alunos.
