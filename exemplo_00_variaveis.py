def exemplo_tipos_primitivos():
    nome: str = "PS5 Pro" #str é string (texto)
    preco: float = 7000.99 # float número real
    quantidade: int = 2
    compra_realizada: bool = True # bool é o operador lógico

    #calcular o total da compra
    total_compra: float = preco * quantidade

    print("Nome:", nome)
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("Compra realizada:", compra_realizada)
    print("Total da compra:", total_compra)

def exemplo_entrada_dados():
        nome: str = input("Digite o nome: ")
        sobrenome: str = input("Digite o sobrenome: ")
        idade: int = int(input("Digite a idade:"))

        nome_completo: str = nome + " " + sobrenome
        texto: str = "Nome completo: " + nome_completo + " tem " + str(idade) + " anos"

        print(texto)

def exercicio_paciente():
            nome: str = input("Nome do paciente: ")
            peso: int = int(input("Peso do paciente: "))
            altura: float = float(input("Altura do paciente: "))
            email: str= input("E-mail: ")

            calculo_imc: float = peso / (altura * altura)

            texto: str = "O calculo do IMC do paciente " + nome + " é: " + str(calculo_imc)

            print(texto)

def exercicio_carro():
    modeloCarro: str = input("Modelo do carro: ")
    quantidadeParcela: int = int(input("Quantidade de parcelas: "))
    valorParcela: float = float(input("Valor da parcela: "))
    valorFipe: float = float(input("Valor da Tabela FIPE: "))

    valorTotal: quantidadeParcela * valorParcela
    valorJuros: valorTotal - valorFipe

    texto: str = "O" + modeloCarro + "paga o total de :" + valorTotal "no carro e paga o valor de juros de " + valorJuros

        

    #esse trecho é chamado quando o arquivo é executado, main é
    # o ponto de entrada (execução) de uma aplicação

if __name__ == "__main__":

    exercicio_paciente()
    #executa a função abaixo, iu seja, executará o código que está dentro da função
    #exemplo_tipos_primitivos()
    #exemplo_entrada_dados()
    