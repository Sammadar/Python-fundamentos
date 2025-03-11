def tratar_erro_conversao_string_nao_inteira():
    try: 
        numero = int(input("digite o número: "))
    except Exception as erro:
        print("Deu erro na conversão do número")
        print("Mensagem do erro: ", erro)

    print("Programa encerrado com sucesso") 

if __name__ == "__main__":
    import os
    os.system("cls")
    tratar_erro_conversao_string_nao_inteira()   