from Bit import Bit
from BinaryNumber import BinaryNumber
from Matriz import Matriz

def gerar_matriz_multiplicacao(vetor1: str, vetor2: str):
    # Dividir os vetores em listas de elementos
    vetor1 = vetor1.split("\t")
    vetor2 = vetor2.split("\t")

    # Criar a matriz resultante
    matriz_resultante = Matriz()

    # Preencher a matriz resultante com os produtos dos elementos dos vetores
    for i, el1 in enumerate(vetor1):
        for j, el2 in enumerate(vetor2, i):  # Começar a multiplicação uma coluna depois
            produto = el1 + el2
            matriz_resultante.append(i, j, produto)

    return matriz_resultante

m = gerar_matriz_multiplicacao("4	3	2	1", "4	3	2	1")
print(m)
    


