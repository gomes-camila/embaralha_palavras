#Crie um jogo que embaralhe uma palavra e a mostre ao jogador. O objetivo é acertar a palavra em até 5 tentativas. 
#Informe sempre quantas tentativas ele ainda tem. Se ele acertar, dê os parabéns; se errar dê uma palavra de ânimo 
#(que mude de forma aleatória). Ao final, mostre a palavra correta e o número de tentativas que ele utilizou.

import random

tentativa = 5
lista_palavras = 'microfone','garrafa','meia','rede','controle'
palavra_aleatoria = random.choice(lista_palavras)


while tentativa != 0:
    embaralha_palavra = random.sample(palavra_aleatoria, len(palavra_aleatoria))
    juntar_palavra_embaralhada = ''.join(embaralha_palavra)
    print(juntar_palavra_embaralhada)
    resposta = input("Qual é essa palavra? ")
    if resposta == palavra_aleatoria:
        print(f"Parabens! Voce acertou! A palavra era {palavra_aleatoria} e voce acertou em {tentativa} tentativas")
        break
    else:
        tentativa -= 1
        lista_erro = f'Tente novamente, voce consegue! Tentativas restantes: {tentativa}', f'Voce esta quase la! Tentativas restantes: {tentativa}', f'Voce esta indo bem, tente novamente! Tentativas restantes: {tentativa}'
        print(random.choice(lista_erro))
        if tentativa == 0:
            print(f"A palavra era {palavra_aleatoria}")