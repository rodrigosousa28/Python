# Algoritmo para verificar quantos divisores um número tem

n = int(input('Digite um número: '))
number = n
div = 2
primos = []
# Divisão por números primos
while n > 1:
    if n % div == 0:
        primos.append(div)
        n = int(n / div)
    else:
        for c in range(1, n+1):
            if n % c == 0:
                qtd = 0
                for i in range(1, c+1):
                    if c % i == 0:
                        qtd += 1
                if qtd == 2:  # Testando se o número é primo
                    div = c
                    break

primos.append(0)
fatores = []
i = 1
for c in range(len(primos)):
    try:
        if primos[c] == primos[c+1]:
            i += 1
        else:
            fatores.append(i)
            i = 1
    except IndexError:
        break

# Número de divisores:
cont = 1
for c in fatores:
    cont *= c+1
print(f'O número {number} tem {cont} divisores.')
