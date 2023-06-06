import random

palavras = ["casa", "tenda", "terreno", "computador", "programacao"]

random_palavra = random.choice(palavras)

print(random_palavra)
vida = 6

display = []

for numero in range(len(random_palavra)):
    display.append("_")



while "_" in display and vida>0:
    print(display)
    acertou = False
    count = 0
    chute = input("Digite uma letra: ")
    for letra in random_palavra:
        if chute == letra:
            display[count] = chute
            acertou = True
        count += 1
    if acertou == False:
        vida -= 1

    print(vida)
