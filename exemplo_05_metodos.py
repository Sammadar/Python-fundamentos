def somar() -> int:
    numero1 = 10
    numero2 = 20
    soma = numero1 + numero2
    return soma

def calculadora():
    resultado = somar()
    print("Soma:", resultado)

def solicitar_nome() -> str:
    nome_solicitado = input("Digite o nome: ").strip()
    while len(nome_solicitado) < 3:
        print("Nome inválido, deve conter no mínimo 3 caracteres")
        nome_solicitado = input("Digite o nome: ").strip()
    return nome_solicitado

def solicitar_sobrenome() -> str:
    sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    while len(sobrenome_solicitado) < 3 or len(sobrenome_solicitado) > 100:
        print("Sobrenome inválido, deve conter no mínimo 3 caracteres e no m[aximo 100")
        sobrenome_solicitado = input("Digite o sobrenome: ").strip()
    return sobrenome_solicitado


def  apresentar_nome_completo(): 
    nome = solicitar_nome()
    sobrenome = solicitar_sobrenome()

    nome_completo = nome + " " + sobrenome
    print("Nome completo: ", nome_completo)     


#Criar uma função solicitar_calcular_produto
#Criar uma função solicitar_modelo min: 4
#Criar uma função solicitar_quantidade min: 1 max: 5
#Criar uma função solicitar_preço min: 100, max: 500
#Criar uma função solicitar_calcular_produto, chamar as funções e armazenar em variáveis
#Apresentar o total e as variaveis

def solicitar_modelo():
    modelo = input("Digite o modelo: ").strip()
    while len(modelo) < 4:
        print("Modelo inválido. O modelo deve ter pelo menos 4 caracteres.")
        modelo = input("Digite o modelo: ").strip()
    return modelo

def solicitar_quantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade (mínimo 1, máximo 5): "))
            if 1 <= quantidade <= 5:
                return quantidade
            else:
                print("Quantidade inválida. A quantidade deve ser entre 1 e 5.")
        except ValueError:
            print("Erro! Digite um número inteiro válido.")

def solicitar_preço():
    while True:
        try:
            preco = float(input("Digite o preço (mínimo 100, máximo 500): "))
            if 100 <= preco <= 500:
                return preco
            else:
                print("Preço inválido. O preço deve ser entre 100 e 500.")
        except ValueError:
            print("Erro! Digite um número válido para o preço.")

def solicitar_calcular_produto():
    modelo = solicitar_modelo()
    quantidade = solicitar_quantidade()
    preco = solicitar_preço()
    
    total = preco * quantidade
    
    print("\nResumo da compra:")
    print(f"Modelo: {modelo}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário: R${preco:.2f}")
    print(f"Total: R${total:.2f}")


if __name__ == "__main__":
    import os
    os.system("cls")
    solicitar_calcular_produto()      
