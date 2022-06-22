def jogar():
    print("*" * 35)
    print('{:''^35}'.format("Bem Vindo ao jogo de Forca!"))
    print("*" * 35)

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while not enforcou and not acertou:

        usuario = input("Qual Letra? ")
        usuario = usuario.strip()

        index = 0
        for letra in palavra_secreta:
            if usuario.upper() == letra.upper():
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim de Jogo")


if __name__ == "__main__":
    jogar()
