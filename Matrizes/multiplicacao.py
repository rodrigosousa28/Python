# Algoritmo para realizar a multiplicação de duas matrizes


def matMult(M, N):
    # Verificando se o número de colunas da 1° é
    # igual ao número de linhas da 2°
    if len(M[0]) != len(N):
        return 'Não é possível multiplicar as duas matrizes!'
    aux = []
    multi = []
    soma = 0
    for m in range(len(M)):
        for p in range(len(N[0])):  # Acessando cada elemento da multiplicação
            l1 = m
            c1 = p
            l2 = 0
            c2 = 0
            cont = 0
            while cont < len(N):
                soma += M[l1][c2] * N[l2][c1]
                c2 += 1
                l2 += 1
                cont += 1
            aux.append(soma)
            soma = 0
        multi.append(aux[:])
        aux = []
    return multi


# Alguns testes com exemplos de multiplicação de matrizes
print(matMult([[2, 3, 1], [0, 1, 2]], [[2, 0], [1, -1], [3, 5]]))
print(matMult([[2, 3], [1, 0], [4, 5]], [[3, 1], [2, 4]]))
print(matMult([[2, 4, 1], [2, 1, 3]], [[2, 4, 1, 5], [2, 1, 3, 7]]))
