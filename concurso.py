quant_candidatos, quant_aprovados = map(int, input('').split())
notas = map(int, input('').split())
notas = list(notas)

notas.sort(reverse=True)
for i in range(quant_aprovados):
    nota_de_corte = notas[i]

print(nota_de_corte)