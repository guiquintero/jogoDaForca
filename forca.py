import random

palavras = ["casa", "tenda", "terreno", "computador", "programacao", "evento"]

palavra_escolhida = random.choice(palavras)

display = []

for n in range(len(palavra_escolhida)):
    display.append("_")
print(display)

vidas = 6

while vidas > 0 and "_" in display:
    chute = input("Digite uma letra: ")
    cont = 0
    acertou = False
    for letra in palavra_escolhida:
        if chute == letra:
            display[cont] = chute
            acertou = True
        cont += 1
    if not acertou:
        vidas -= 1
        print('Vidas restantes: ' + vidas)
    print(display)

if vidas > 0:
    print('Voce ganhou!!!!')
else:
    print('Voce perdeu :(')