print("*"*35)
print("Bem Vindo ao jogo de Adivinhação!")
print("*"*35)

numero_secreto = 43
total_tentativas = 3


for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    usuario = int(input("Digite o seu número: "))
    print("Você digitou", usuario)

    maior = usuario > numero_secreto
    menor = usuario < numero_secreto
    acertou = usuario == numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior!")
        elif menor:
            print("Você errou! O seu chute foi menor!")

print("Game Over")
