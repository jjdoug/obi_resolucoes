k, n = map(int, input().split())
alfabeto = input()
msg = input()

resposta = 'S'
for caractere in msg:
    if caractere not in alfabeto:
        resposta = 'N'
        break

print(resposta)
