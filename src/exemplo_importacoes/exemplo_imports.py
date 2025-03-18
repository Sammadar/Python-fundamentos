# importação1: importanto arquivo, tendo que passar o caminho completo
import src.exemplo07_metodos_parametros

#importação2: importando do src o arquivo exemplo06_metodos
from src import exemplo_05_metodos

#importanção3: importnado um metodo de arquivo exemplo05_for
from src.exemplo_for import exemplo_relogio, exemplo_apresentar_contagem_regressiva

def executar():
    #importação1: utilizado da importação devo passar o caminho completo e metodo
    src.exemplo07_metodos_parametros.calculadora

    #importação2: utilização da importação de vo passr o nomedo arquivo e metodo
    exemplo_05_metodos.apresentar_nome_completo()

    #importação3: utilização da importação devo chamar os metodos importados
    exemplo_relogio()
    exemplo_apresentar_contagem_regressiva()

def executar_calculos_matematicos():
    import math
    print("Raiz quadrada de 114: ", math.sqrt(114))