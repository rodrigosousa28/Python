# Algoritmo para descobrir o CPF completo de uma pessoa
# a partir dos 9 primeiros dígitos

cpf = str(input('Digite os 9 primeiros dígitos do seu CPF: ')).strip()
while len(cpf) != 9 or (not cpf.isnumeric()):
    cpf = str(input('Digite os 9 primeiros dígitos NUMÉRICOS do seu CPF: ')).strip()
cpf = list(cpf)  # No error!
for c in range(0, len(cpf)):
    cpf[c] = int(cpf[c])

i = len(cpf) - 1
multiplicador = 2
aux = []
while i >= 0:
    aux.append(cpf[i] * multiplicador)
    multiplicador += 1
    i -= 1

soma = 0
for c in aux:
    soma += c

divint = soma//11
resto = soma % 11

if resto < 2:
    cpf.append(0)
elif resto >= 2:
    cpf.append(11 - resto)

i = len(cpf) - 1
multiplicador = 2
aux = []
while i >= 0:
    aux.append(cpf[i] * multiplicador)
    multiplicador += 1
    i -= 1

soma = 0
for c in aux:
    soma += c

divint = soma//11
resto = soma % 11

if resto < 2:
    cpf.append(0)
elif resto >= 2:
    cpf.append(11 - resto)


for c in range(len(cpf)):
    cpf[c] = str(cpf[c])

cpf.insert(3, '.')
cpf.insert(7, '.')
cpf.insert(11, '-')

cpfinal = ''

for c in cpf:
    cpfinal += c

print(f'Seu CPF é {cpfinal}')
