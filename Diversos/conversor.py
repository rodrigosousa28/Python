# Algoritmo para converter números entre as principais bases numéricas


def dectother(a, n):
    other = []
    other2 = []
    while a >= 1:
        b = int(a % n)
        a = a / n
        if b == 10:
            b = 'A'
        elif b == 11:
            b = 'B'
        elif b == 12:
            b = 'C'
        elif b == 13:
            b = 'D'
        elif b == 14:
            b = 'E'
        elif b == 15:
            b = 'F'
        other.append(str(b))
    i = len(other) - 1
    while i >= 0:
        other2.append(other[i])
        i -= 1
    variavel = ''.join(other2)
    if variavel.isnumeric():
        variavel = int(variavel)
    return variavel


def othertodec(a, n):
    others = []
    soma = 0
    i = len(a) - 1
    while i >= 0:
        others.append(int(a[i]))
        i -= 1
    for i, k in enumerate(others):
        soma += (n ** i) * k
    return soma


def hextodec(a):
    hexadecimais = []
    hexadecimais2 = []
    soma = 0
    i = len(a) - 1
    while i >= 0:
        hexadecimais.append(a[i])
        i -= 1
    for i, h in enumerate(hexadecimais):
        if h == 'A':
            hexadecimais[i] = '10'
        elif h == 'B':
            hexadecimais[i] = '11'
        elif h == 'C':
            hexadecimais[i] = '12'
        elif h == 'D':
            hexadecimais[i] = '13'
        elif h == 'E':
            hexadecimais[i] = '14'
        elif h == 'F':
            hexadecimais[i] = '15'
    for h in hexadecimais:
        hexadecimais2.append(int(h))
    for i, h in enumerate(hexadecimais2):
        soma += (16 ** i) * h
    return soma


j = 1
possibilidades = ['decimal', 'binario', 'octal', 'hexadecimal']
for c in range(len(possibilidades)):
    for r in range(0, 4):
        if possibilidades[c] != possibilidades[r]:
            print(
                f'{j}. {possibilidades[c].capitalize()} para {possibilidades[r]}')
            j += 1

esc = int(input('Escolha uma das opções acima: '))

if esc == 1:
    choice = int(input('Insira o número em decimal: '))
    var = dectother(choice, 2)
    print(f'O número decimal {choice} em binário vale: {var}')
elif esc == 2:
    choice = int(input('Insira o número em decimal: '))
    var = dectother(choice, 8)
    print(f'O número decimal {choice} em octal vale: {var}')
elif esc == 3:
    choice = int(input('Insira o número em decimal: '))
    var = dectother(choice, 16)
    print(f'O número decimal {choice} em hexadecimal vale: {var}')
elif esc == 4:
    choice = str(input('Insira o número em binário: ')).strip()
    var = othertodec(choice, 2)
    print(f'O número binário {choice} em decimal vale {var}')
elif esc == 5:
    choice = str(input('Insira o número em binário: ')).strip()
    var = othertodec(choice, 2)
    var2 = dectother(var, 8)
    print(f'O número binário {choice} em octal vale: {var2}')
elif esc == 6:
    choice = str(input('Insira o número em binário: ')).strip()
    var = othertodec(choice, 2)
    var2 = dectother(choice, 16)
    print(f'O número binário {choice} em hexadecimal vale: {var2}')
elif esc == 7:
    choice = str(input('Insira o número em octal: ')).strip()
    var = othertodec(choice, 8)
    print(f'O número octal {choice} em decimal vale: {var}')
elif esc == 8:
    choice = str(input('Insira o número em octal: ')).strip()
    var = othertodec(choice, 8)
    var2 = dectother(var, 2)
    print(f'O número octal {choice} em binário vale: {var2}')
elif esc == 9:
    choice = str(input('Insira o número em octal: ')).strip()
    var = othertodec(choice, 8)
    var2 = dectother(choice, 16)
    print(f'O número octal {choice} em hexadecimal vale: {var2}')
elif esc == 10:
    choice = str(input('Insira o número em hexadecimal: ')).strip()
    var = hextodec(choice)
    print(f'O número hexadecimal {choice} em decimal vale: {var}')
elif esc == 11:
    choice = str(input('Insira o número em hexadecimal: ')).strip()
    var = hextodec(choice)
    var2 = dectother(var, 2)
    print(f'O número hexadecimal {choice} em binário vale: {var2}')
elif esc == 12:
    choice = str(input('Insira o número em hexadecimal: ')).strip()
    var = hextodec(choice)
    var2 = dectother(var, 8)
    print(f'O número hexadecimal {choice} em octal vale: {var2}')
