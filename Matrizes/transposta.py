# Algoritmo para transformar uma matriz na sua transposta


def matTransp(M):
    # Verificar se é mesmo uma matriz:
    erros = 0
    ajuda = len(M[0])
    for i in range(len(M)):
        if len(M[i]) != ajuda:
            erros += 1
            return 'ERRO! Você não digitou uma matriz'

    # Transformando M na matriz transposta Mt
    Mt = []
    auxiliar = []
    i = len(M)
    j = 0
    while True:
        for cont in range(0, i):
            for c in range(j, len(M[0])):
                auxiliar.append(M[cont][c])
                break
        Mt.append(auxiliar[:])
        auxiliar = []
        j += 1
        if j == len(M[0]):
            break
    return Mt


# Testes com alguns exemplos de matrizes
print(matTransp([[2, 4.1, 3], [1, 1, 1], [2.0, 4.3, 9]]))
print(matTransp([[2.2, 4], [5, 6], [9, 2.0]]))
print(matTransp([[5, 6.8, 4], [3, 1, 2.1]]))
print(matTransp([[2, 3, 3.3], [4.2, 3.1]]))
