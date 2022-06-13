# Algoritmo para calcular o desvio padrão de uma amostra de dados

media = atual = 0
valores = []
desvios = []
while True:
    try:
        atual = float(input())
        valores.append(atual)
    except ValueError:
        break
media = sum(valores)/len(valores)
for i, c in enumerate(valores):
    desvios.append((valores[i] - media)**2)
desvtot = (sum(desvios)/(len(valores)-1))**0.5
print(f'O desvio padrão é {desvtot}')
