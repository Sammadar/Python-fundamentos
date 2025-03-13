def remover_espacos_comeco_string():
    texto = "    Minha casa é amarela   "
    # Remover os espaços da esquerda(começo) da string
    texto_removido_espacos_comeco = texto.lstrip()
    print("Texto: '" + texto_removido_espacos_comeco + "'")


def remover_espacos_final_string():
    texto = "   Minha casa é amarela   "
    # Remover os espaços da direita(final) da string
    texto_removido_espacos_final = texto.rstrip()
    print("Texto: '" + texto_removido_espacos_final + "'")


def remover_espacos_comeco_final_string():
    texto = "   Minha casa é amarela   "
    # Remover os espaços da esquerda(comeco) e direita(final) da string
    texto_removido_espacos_comeco_final = texto.strip()
    print("Texto: '" + texto_removido_espacos_comeco_final + "'")


def substituir_parte_string():
    texto = "EU tenho um gato."
    # Substituir o EU para Eu
    texto = texto.replace("EU", "Eu")
    # Substituir o ponto final por nada
    texto = texto.replace(".", "")
    print("Texto: " + texto)


def substituir_valor():
    valor_entrada: str = "R$ 2.395,33" # Alterar a string para '2395.33'
    valor_entrada_sanitizada: str = valor_entrada.replace(".", "") # "R$ 2.395,33" => "R$ 2395,33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.replace(",", ".") # "R$ 2395,33" => "R$ 2395.33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.replace("R$", "") # "R$ 2395.33" => " 2395.33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.strip() # " 2395.33" => "2395.33"

    valor: float = float(valor_entrada_sanitizada)
    print("Valor: ", valor)
# como formatar float no formato real pt-br em python


def verificar_comeca_com_enzo():
    texto = "Enzo da Silva"
    if texto.startswith("Enzo"): # começa com 'Enzo'
        print("Geração Alpha")
    else:
        print("Outra geração")


def verificar_termina_com_silva_ou_souza():
    texto = "Enzo da Souza"
    if texto.endswith("Silva") or texto.endswith("Souza") : # termina 'Silva' ou "Souza"
        print("Brasileiro")
    else:
        print("Estrangeiro")


def verificar_se_contem():
    # produto = "Toddy com pão e linguiça blumenau"
    # produto = "Pão de queijo e Toddy"
    # produto = "Pizza, Toddy e Açaí"
    # produto = "Nescau é top!"
    produto = "Água é top!"
    if "Toddy" in produto:
        print("Viva o toddy")
    elif "Nescau" in produto:
        print("Trocar por Toddy o verdadeiro achocolatado")
    else:
        print("Sei lá")


def verificar_se_nao_contem():
    produto = "Aipim com frango"
    # produto = "Toddy"
    if "Toddy" not in produto: # se 'Toddy' não está no texto
        print("Ta safe pode comer:", produto)
    else:
        print("Ta errado, deixa o toddy de lado")


def transformar_letras_minusculas():
    carro = "Gol Quadrado cINzA "
    # lower é utilizado para converter em letra minúscula
    carro = carro.lower() # "Gol Quadrado cINzA " => "gol quadrado cinza "
    carro = carro.strip()
    if carro == "gol quadrado cinza":
        print("É VW")
    else:
        print("Não é VW")


def transformar_letras_maisculas():
    carro = "Gol Quadrado cINzA "
    # lower é utilizado para converter em letra minúscula
    carro = carro.upper() # "Gol Quadrado cINzA " => "GOL QUADRADO CINZA "
    carro = carro.strip() # "GOL QUADRADO CINZA " => "GOL QUADRADO CINZA"
    if carro == "GOL QUADRADO CINZA":
        print("É VW")
    else:
        print("Não é VW")
    

def converter_data():
    data = "10/07/2025"
    partes = data.split("/") # 0 - "10", 1 - "03", 2 = "2025"
    dia = int(partes[0]) # 10
    mes = int(partes[1]) # 03
    ano = int(partes[2]) # 2025

    if ano == 2025:
        print("Ano do SuperDev")
    else:
        print("Não é o ano")
    
    if mes == 1:
        mes_extenso = "Janeiro"
    elif mes == 2:
        mes_extenso = "Fevereiro"
    elif mes == 3:
        mes_extenso = "Março"
    elif mes == 4:
        mes_extenso = "Abril"
    elif mes == 5:
        mes_extenso = "Maio"
    elif mes == 6:
        mes_extenso = "Junho"
    elif mes == 7:
        mes_extenso = "Julho"
    elif mes == 8:
        mes_extenso = "Agosto"
    elif mes == 9:
        mes_extenso = "Setembro"
    elif mes == 10:
        mes_extenso = "Outubro"
    elif mes == 11:
        mes_extenso = "Novembro"
    elif mes == 12:
        mes_extenso = "Dezembro"
    else:
        mes_extenso = "Mês inválido"


    print("Blumenau, " + str(dia) + " de " + mes_extenso.lower() + " de " + str(ano))
    

def extrair_data_hora():
    texto = "20/02/1996 23:49:13"
    partes_data_hora = texto.split(" ") # duas posições: 0 "20/02/1996" 1 "23:49:13"
    partes_data = partes_data_hora[0].split("/") # 20/02/1996 => 0 20, 1 02, 2 1996
    partes_hora = partes_data_hora[1].split(":") # 23:49:13
    dia = partes_data[0] # 20
    mes = partes_data[1] # 02
    ano = partes_data[2] # 1996

    hora = partes_hora[0]
    minuto = partes_hora[1]
    segundo = partes_hora[2]
    print(dia)
    print(mes)
    print(ano)
    print(hora)
    print(minuto)
    print(segundo)


def extrair_da_string(): # subtring
    #       0123456789
    data = "19/04/2020"
    dia = data[0:2] # pegou posição 0 e 1
    mes = data[3:5] # pegou posição 3 e 4
    ano = data[6:10] # pegou a posição 6, 7, 8 e 9
    print(dia, mes, ano)


def verificar_tamanho_string():
    texto = "    Eu estou com fome   "
    texto = texto.strip()
    quantidade_caracteres = len(texto) # length: comprimento
    print("Texto: '" + texto + "'")
    print("Quantidade de caracteres: ", quantidade_caracteres)


def solicitar_nome():
    nome = input("Digite o nome: ").strip()
    while len(nome) < 3 or len(nome) > 50:
        print("Nome deve conter no mínimo 3 caracteres e no máximo 50")
        nome = input("Digite o nome: ").strip()

# texto.lstrip() remover os espaços do início
# texto.rstrip() remover os espaços do final
# texto.strip() remover os espaços do início e do final
# texto.replace("antigo", "novo") substruir o que está no antigo por o novo
# texto.startswith("texto começo") verificar que começa com  
# texto.endswith("texto final") verificar que termina com
# texto.lower() transformar letra minúscula
# texto.upper() transformar letra maiúscula
# len(texto) obter a quantidade de caracteres

if __name__ == "__main__":
    import os
    os.system("cls")
    solicitar_nome()       