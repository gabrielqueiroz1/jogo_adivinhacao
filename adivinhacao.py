from random import randint

def painel_niveis():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

def mensagem_saudação():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

continuar_jogando = "S"
venceu = perdeu = 0

while continuar_jogando == "S":
    numero_secreto = randint(1, 50)
    pontos = 1000
    pontos_perdidos = nivel = total_de_tentativas = 0

    while nivel <= 0 or nivel >= 4:
        mensagem_saudação()
        painel_niveis()
        nivel = int(input("Defina o nível: "))

        if nivel == 1: 	
            total_de_tentativas = 20
        elif nivel == 2:
            total_de_tentativas = 10
        elif nivel == 3:
            total_de_tentativas = 5
        else:
            print("***"*14)
            print("Digite um dos níveis descritos no painel!")
            print("***"*14)

        for rodada in range(1, total_de_tentativas + 1):
            print(f"Tentativa {rodada} de {total_de_tentativas}")

            chute = int(input("Digite um número entre 1 e 100: "))
            print("Você digitou", chute)

            while chute < 1 or chute > 100:
                print("***"*15)
                print("Você deve digitar um número entre 1 e 100!")
                print("***"*15)
                chute = int(input("Digite um número entre 1 e 100: "))
                print("Você digitou", chute)

            maior = chute > numero_secreto
            menor = chute < numero_secreto

            if chute == numero_secreto:
                print(f"Você acertou e fez {pontos} pontos!")
                print("***"*5)
                print("Fim do jogo!")
                print("***"*5)
                venceu += 1
                break
            if total_de_tentativas == rodada and chute != numero_secreto:
                print(f"Você não acertou e o número secreto era {numero_secreto}")
                perdeu += 1
                break
            else:
                if maior:
                    print("Você errou! O seu chute foi maior do que o número secreto.")
                elif menor:
                    print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
        continuar_jogando = ""
        while continuar_jogando != "S" or continuar_jogando != "N":
            continuar_jogando = input("Você deseja continuar jogando [S/N]? ").upper()[0]
            if continuar_jogando == "S":
                break
            elif continuar_jogando == "N":
                print("***" * 13)
                print(f"Você acertou {venceu} vezes, parabéns!")
                print(f"Você acabou perdendo {perdeu} vezes.")
                print("Muito obrigado por jogar o nosso jogo!")
                print("***" * 13)
                break
        break
