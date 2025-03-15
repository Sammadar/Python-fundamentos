import time

def exemplo_for_apresentar_numeros():

    for indice in range(0, 5):
        print(indice)


def exemplo_for_incrementar_dois_em_dois():

    for indice in range(0, 10, 3):
        print(indice)        

def exemplo_solicitar_dados():
    quantidade_desejada = int(input("Digite a quantidade desejada: "))
    for i in range(0, quantidade_desejada):
        nome = input("Digite o nome: ").strip()
        sobrenome = input("Digite o sobrenome: ").strip()
        nome_completo = nome + " " + sobrenome
        print("Nome completo:", nome_completo)
          

def exemplo_apresentar_contagem_regressiva():
    for i in range(10, -1, -1):
        print(i)
        time.sleep(1)


def exemplo_relogio():
    for hora in range(0, 24):
        for minuto in range (0, 60):
            for segundo in range (0, 60):
                print(hora, minuto, segundo, sep=":")
                time.sleep(1)            
     

if __name__ == "__main__":
    import os
    os.system("cls")
    exemplo_for_incrementar_dois_em_dois()       