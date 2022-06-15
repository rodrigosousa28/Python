# Algoritmo para colocar uma sequência de números em ordem crescente e
# decrescente


numbers = []
qtd = 0
while True:
    try:
        n = float(input("Digite um número (ou outra coisa para parar): "))
        numbers.append(n)
        qtd += 1
    except ValueError:
        break


i = len(numbers) - 1
while i >= 0:
    c = 0
    bigger = numbers[0]
    posmax = 0
    while c <= i:
        if numbers[c] > bigger:
            bigger = numbers[c]
            posmax = c
        c += 1
    x = numbers[i]
    numbers[i] = numbers[posmax]
    numbers[posmax] = x
    i -= 1

# Formatar os números que são inteiros, mas
# estão no formato float, para o formato int
for c in range(len(numbers)):
    if int(numbers[c]) == float(numbers[c]):
        numbers[c] = int(numbers[c])

# Inverter para a ordem decrescente
i = len(numbers) - 1
inv = []
while i >= 0:
    inv.append(numbers[i])
    i -= 1

print(f'Lista na ordem crescente: {numbers}')
print(f'Lista na ordem decrescente: {inv}')
