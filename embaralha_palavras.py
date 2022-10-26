import random


def main():
    print("Embaralha Palavras")
    var_tema_input = input("Selecione um tema:\n1- Cidades, 2- Objetos ou 3- Países\n")
    var_dificuldade_input = input(
        "Selecione a dificuldade:\n1- Fácil, 2- Médio ou 3- Dificil\n"
    )

    funcao_tentativas(
        embaralha_palavra(var_dificuldade_input, escolhe_tema(var_tema_input))
    )


def escolhe_tema(par_tema):
    cidades = [
        "Itu",
        "Natal",
        "Belém",
        "Manaus",
        "Maceió",
        "Goiânia",
        "Salvalor",
        "Joinville",
        "Porto Alegre",
    ]
    objetos = [
        "Bola",
        "Meia",
        "Rede",
        "Quadro",
        "Garrafa",
        "Esmalte",
        "Microfone",
        "Isqueiro",
        "Microondas",
    ]
    paises = [
        "Peru",
        "China",
        "Egito",
        "Iraque",
        "França",
        "Rússia",
        "Alemanha",
        "Vaticano",
        "Argentina",
    ]

    if par_tema == "1":
        print("Tema Cidades")
        return cidades
    elif par_tema == "2":
        print("Tema Objetos")
        return objetos
    elif par_tema == "3":
        print("Tema Países")
        return paises


def escolhe_dificuldade(par_dificuldade, par_tema):
    palavras_em_tema_dificuldade = []
    if par_dificuldade == "1":
        for item in par_tema:
            if len(item) <= 5:
                palavras_em_tema_dificuldade.append(item)

    if par_dificuldade == "2":
        for item in par_tema:
            if len(item) > 5 and len(item) < 8:
                palavras_em_tema_dificuldade.append(item)

    if par_dificuldade == "3":
        for item in par_tema:
            if len(item) >= 8:
                palavras_em_tema_dificuldade.append(item)

    return palavras_em_tema_dificuldade


def embaralha_palavra(par_dificuldade, par_tema):
    palavra_aleatoria = random.choice(escolhe_dificuldade(par_dificuldade, par_tema))
    embaralha_palavra = random.sample(palavra_aleatoria, len(palavra_aleatoria))
    juntar_palavra_embaralhada = "".join(embaralha_palavra)
    print(
        f"Você tem 5 tentativas para acertar a palavra a seguir:\n{juntar_palavra_embaralhada}"
    )

    return palavra_aleatoria


def funcao_tentativas(par_palavra_aleatoria):
    tentativas = 4
    resposta = input("Qual é essa palavra?\n")
    while tentativas != 0:
        if resposta == par_palavra_aleatoria:
            print(f"Parabens! Você acertou!")
            break
        else:
            tentativas -= 1
            lista_erro = f"Tente novamente!", f"Não desista!" f"Você está indo bem!"
            print(random.choice(lista_erro))
            resposta = input("")
            if tentativas == 0:
                print(f"A palavra era {par_palavra_aleatoria}")


def erro(par_palavra_aleatoria, par_tentativas):
    tentativas -= 1
    lista_erro = f"Tente novamente!", f"Não desista!" f"Você está indo bem!"
    print(random.choice(lista_erro))
    resposta = input("")
    if tentativas == 0:
        print(f"A palavra era {par_palavra_aleatoria}")


main()
