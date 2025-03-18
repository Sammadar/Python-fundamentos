def exemplo_if_simples():
    idade = int(input("Digite a sua idade: "))

    if idade <= 17:
        print("Menor de idade")
    elif idade <= 64:
        print("Adulto")
    else:
        print("Idoso")     

def exemplo_if_operador_e():
    valor_produto = 100.00
    quantidade = int(input("Digite a quantidade de produtos: "))

    percentual_desconto = 0
    if quantidade >= 5 and quantidade <= 10:
        percentual_desconto = 5
    elif quantidade >= 11 and quantidade <= 50:
        percentual_desconto = 10
    elif quantidade > 50:
        percentual_desconto = 15      


    valor_compra_sem_desconto = quantidade * valor_produto
    valor_desconto = valor_compra_sem_desconto * (percentual_desconto / 100) 
    valor_total_compra = valor_compra_sem_desconto - valor_desconto


    print("Valor compra: ", valor_compra_sem_desconto)    
    print("Percentual de desconto: ", percentual_desconto, "%")
    print("Valor desconto: ", valor_desconto)
    print("Valor total: ", valor_total_compra)   

def exemplo_if_operador_ou():
    nome = input("Digite o nome do jogo: ").strip()
    categoria = input("Digite a categoria: ").strip()

    categoria_sanitizada = categoria.lower()

    if categoria_sanitizada == "rpg" or categoria_sanitizada == "ação":
        preco = 150.99
    elif categoria_sanitizada == "esports" or categoria_sanitizada == "moba":
         preco = 99.99
    else:
        preco = 200.00

    print ("Nome: ", nome)
    print ("Categoria: ", categoria)
    print ("Preço: ", preco)


    # Tabela verdade operador lógico ou
    #V ou V -> V
    #V ou F -> V
    #F ou V -> V
    #F ou F -> F

def verificar_numero_par():
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        print("Par")
    else:
        print("Não é par")

def verificar_numero_impar():
    numero = int(input("Digite o número: "))
    if numero % 2 != 0:
        print("Ímpar")
    else:
        print("Não é ímpar")            

if __name__ == "__main__":
    verificar_numero_par()          