import random


def jogar():
    print("*" * 35)
    print('{:''^35}'.format("Bem Vindo ao jogo de Adivinhação!"))
    print("*" * 35)

    numero_secreto = random.randint(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de Dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o Nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        usuario = int(input("Digite o seu número entre 1 e 100: "))
        print("Você digitou", usuario)

        if usuario < 1 or usuario > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        maior = usuario > numero_secreto
        menor = usuario < numero_secreto
        acertou = usuario == numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior!")
            elif menor:
                print("Você errou! O seu chute foi menor!")
            pontos_perdidos = abs(numero_secreto - usuario)
            pontos = pontos - pontos_perdidos

    print("O número era {}".format(numero_secreto))
    print("Game Over")

if(__name__ == "__main__"):
    jogar()
