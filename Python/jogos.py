import forca
import advinhacao_aleatorio_niveis


def escolhe_jogo():
    print("*"*35)
    print('{:''^35}'.format("Escolha o seu Jogo!"))
    print("*"*35)

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual Jogo? "))

    if jogo == 1:
        print("Jogando Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Advinhação")
        advinhacao_aleatorio_niveis.jogar()
    else:
        print("Opção Inválida!")

if (__name__ == "__main"):
    escolhe_jogo()
