#Hello world! Time for a Tic Tac Toe project!
#Fernando Santos

import numpy as np

#Hello World
print("\n       **OLÁ LUCINHAA!!** \n **Vamos jogar o jogo da velha?**\n")
print(" \nPara jogar, basta digitar 'a', 'b', 'c', etc... assim como o abaixo: \n \n  \
(a b c) \n  (d e f) \n  (g h i) \n \n *BOA SORTE* \n")


#Rules
while True:
    n_match = input("Quantas partidas você que jogar? (Responda com: 1, 3, 5, 7, 9,...):")
    try:
        n_match=int(n_match)
        while (int(n_match) % 2 == 0):
            print("\n **Por favor, responda com números ímpares** \n")
            n_match = input("Quantas partidas você que jogar? **(RESPONDA COM: 1, 3, 5, 7, 9,...)**:")


        break
    except ValueError:
       print("\n **Por favor, responda com números ímpares** \n")
n_match=int(n_match)
if n_match % 2 == 1 and n_match == 1:
    print("\n  **TUDO OU NADA** ")

elif n_match % 2 == 1:
    print("\n  **MELHOR DE ", n_match, "**")


#Add names of players
p1 = input("Nome do Jogador 1: ")
p2 = input("Nome do Jogador 2: ")
p1 = p1.upper()
p2 = p2.upper()


#Board game
r1 = [0, 0, 0]
r2 = [0, 0, 0]
r3 = [0, 0, 0]


#Print table
def new_table():

    r1_np = np.array(r1)
    r2_np = np.array(r2)
    r3_np = np.array(r3)
    print(r1_np)
    print(r2_np)
    print(r3_np, "\n")
def clean_table():
    r1[0]=0 ; r1[1]=0 ; r1[2]=0 ; r2[0]=0 ; r2[1]=0 ;\
    r2[2]=0 ; r3[0]=0 ; r3[1]=0 ; r3[2]=0


#Plays
def play_1():
    print(p1 + ", é sua vez")
    turn_1 = input("Escolha onde jogar, " + p1 + ":  ")

    while turn_1!="a" and turn_1!="b" and turn_1!="c" and turn_1!="d" and turn_1!="e" and turn_1!="f" and turn_1!="g"\
    and turn_1!="h" and turn_1!="i":
        print("VOCÊ NÃO PODE JOGAR AÍ! \n    TENTE NOVAMENTE")
        turn_1 = input("Escolha onde jogar, " + p1 + ":  ")

    while (turn_1 == "a" and r1[0]!=0) or (turn_1 == "b" and r1[1]!=0) or (turn_1 == "c" and r1[2]!=0) \
            or (turn_1 == "d" and r2[0]!=0) or (turn_1 == "e" and r2[1]!=0) or (turn_1 == "f" and r2[2]!=0)\
            or (turn_1 == "g" and r3[0]!=0) or (turn_1 == "h" and r3[1]!=0) or (turn_1 == "i" and r3[2]!=0):
        print("YOCÊ NÃO PODE JOGAR AÍ! \n    TENTE NOVAMENTE")
        turn_1 = input("Escolha onde jogar, " + p1 + ":  ")

    if turn_1 == "a":
        r1[0] = 1
    if turn_1 == "b":
        r1[1] = 1
    elif turn_1 == "c":
        r1[2] = 1
    elif turn_1 == "d":
        r2[0] = 1
    elif turn_1 == "e":
        r2[1] = 1
    elif turn_1 == "f":
        r2[2] = 1
    elif turn_1 == "g":
        r3[0] = 1
    elif turn_1 == "h":
        r3[1] = 1
    elif turn_1 == "i":
        r3[2] = 1
    print("\n")
    new_table()
def play_2():
    print(p2 + ", é sua vez")
    turn_2 = input("Escolha onde jogar, " + p2+ ":  ")

    while turn_2 != "a" and turn_2 != "b" and turn_2 != "c" and turn_2 != "d" and turn_2 != "e" and turn_2 != "f" and turn_2 != "g" \
               and turn_2 != "h" and turn_2 != "i":
           print("VOCÊ NÃO PODE JOGAR AÍ! \n    TENTE NOVAMENTE")
           turn_2 = input("Escolha onde jogar, " + p2 + ":  ")
    while (turn_2 == "a" and r1[0]!=0) or (turn_2 == "b" and r1[1]!=0) or (turn_2 == "c" and r1[2]!=0) \
            or (turn_2 == "d" and r2[0]!=0) or (turn_2 == "e" and r2[1]!=0) or (turn_2 == "f" and r2[2]!=0)\
            or (turn_2 == "g" and r3[0]!=0) or (turn_2 == "h" and r3[1]!=0) or (turn_2 == "i" and r3[2]!=0):
        print("VOCÊ NÃO PODE JOGAR AÍ! \n    TENTE NOVAMENTE")
        turn_2 = input("Escolha onde jogar, " + p2 + ":  ")
    if turn_2 == "a":
        r1[0] = 2
    elif turn_2 == "b":
        r1[1] = 2
    elif turn_2 == "c":
        r1[2] = 2
    elif turn_2 == "d":
        r2[0] = 2
    elif turn_2 == "e":
        r2[1] = 2
    elif turn_2 == "f":
        r2[2] = 2
    elif turn_2 == "g":
        r3[0] = 2
    elif turn_2 == "h":
        r3[1] = 2
    elif turn_2 == "i":
        r3[2] = 2
    print("\n")
    new_table()


#Score Board
results=[]
turns_till_end = n_match - results.count(1) - results.count(2) - results.count(3)
def score_board():

    if (r1[0] == r1[1] == r1[2] == 1) or (r2[0] == r2[1] == r2[2] == 1) or (r3[0] == r3[1] == r3[2] == 1) or \
            (r1[0] == r2[0] == r3[0] == 1) or (r1[1] == r2[1] == r3[1] == 1) or (r1[2] == r2[2] == r3[2] == 1) \
            or (r1[0] == r2[1] == r3[2] == 1) or (r1[2] == r2[1] == r3[0] == 1):
        results.append(1)
    elif (r1[0] == r1[1] == r1[2] == 2) or (r2[0] == r2[1] == r2[2] == 2) or (r3[0] == r3[1] == r3[2] == 2) or \
        (r1[0] == r2[0] == r3[0] == 2) or (r1[1] == r2[1] == r3[1] == 2) or (r1[2] == r2[2] == r3[2] == 2) \
        or (r1[0] == r2[1] == r3[2] == 2) or (r1[2] == r2[1] == r3[0] == 2):
        results.append(2)
    else:
        results.append(3)
    print("\n\n     **PLACAR DO JOGO** \n        **", results.count(1), "X", results.count(2), "**\n \n")
    turns_till_end=n_match - results.count(1) - results.count(2) - results.count(3)


#Games mechanics
def game_mechanics1():
    for x in range(1,10):
        table = r1 + r2 + r3

        if all([v > 0 for v in table]):
            print("TIE")
            break
        else:
            play_1()
            if (r1[0] == r1[1] == r1[2] == 1) or (r2[0] == r2[1] == r2[2] == 1) or (r3[0] == r3[1] == r3[2] == 1) or \
            (r1[0] == r2[0] == r3[0] ==1) or (r1[1] == r2[1] == r3[1] ==1) or (r1[2] == r2[2] == r3[2] ==1)\
            or (r1[0] == r2[1] == r3[2] ==1) or (r1[2] == r2[1] == r3[0] ==1) :
                print("\n   *" + p1 + " GANHOU ESSA PARTIDA!*")
                break
            else:
                table = r1 + r2 + r3
                if all([v > 0 for v in table]):
                    print("          **EMPATE**")
                    break
                else:
                    play_2()
                    if (r1[0] == r1[1] == r1[2] == 2) or (r2[0] == r2[1] == r2[2] == 2) or (
                        r3[0] == r3[1] == r3[2] == 2) or \
                        (r1[0] == r2[0] == r3[0] == 2) or (r1[1] == r2[1] == r3[1] == 2) or (
                        r1[2] == r2[2] == r3[2] == 2) \
                        or (r1[0] == r2[1] == r3[2] == 2) or (r1[2] == r2[1] == r3[0] == 2):
                        print("\n   *" + p2 + " GANHOU ESSA PARTIDA!")
                        break
def game_mechanics2():
    for x in range(1,10):
        table = r1 + r2 + r3

        if all([v > 0 for v in table]):
            print("EMPATE")
            break
        else:
            play_2()
            if (r1[0] == r1[1] == r1[2] == 2) or (r2[0] == r2[1] == r2[2] == 2) or (r3[0] == r3[1] == r3[2] == 2) or \
            (r1[0] == r2[0] == r3[0] ==2) or (r1[1] == r2[1] == r3[1] ==2) or (r1[2] == r2[2] == r3[2] ==2)\
            or (r1[0] == r2[1] == r3[2] ==2) or (r1[2] == r2[1] == r3[0] ==2) :
                print("\n   *" + p2 + " GANHOU ESSA PARTIDA!*")
                break
            else:
                table = r1 + r2 + r3
                if all([v > 0 for v in table]):
                    print("          **EMPATE**")
                    break
                else:
                    play_1()
                    if (r1[0] == r1[1] == r1[2] == 1) or (r2[0] == r2[1] == r2[2] == 1) or (
                        r3[0] == r3[1] == r3[2] == 1) or \
                        (r1[0] == r2[0] == r3[0] == 1) or (r1[1] == r2[1] == r3[1] == 1) or (
                        r1[2] == r2[2] == r3[2] == 1) \
                        or (r1[0] == r2[1] == r3[2] == 1) or (r1[2] == r2[1] == r3[0] == 1):
                        print("\n   *" + p1 + " GANHOU ESSA PARTIDA!*")
                        break


#Game
def game():
    print("\n ", p1, "começa o jogo =D \n")

    for q in range (n_match) :
        turns_till_end = n_match - results.count(1) - results.count(2) - results.count(3)
        if turns_till_end > results.count(1) and results.count(2) < turns_till_end\
                or (results.count(1) == results.count(2) or results.count(1) + results.count(2) < n_match):
            new_table()
            game_mechanics1()
            score_board()
            if results.count(1) == int((n_match / 2 + 0.5)) or results.count(1) == int(
                    (n_match / 2 - 0.5)) and results.count(3) == 2:
                break
            if results.count(3) == n_match or results.count(1) + results.count(2) + results.count(3) == n_match:
                break

            else:
                print("\n PRÓXIMA PARTIDA \n")
            clean_table()
            new_table()
            game_mechanics2()
            score_board()

            if results.count(1) == int((n_match / 2 + 0.5)) or results.count(1) == int(
                    (n_match / 2 - 0.5)) and results.count(3) == 2:
                break
            if results.count(3) == n_match or results.count(1) + results.count(2) + results.count(3) == n_match:
                break

            else:
                print("\n PRÓXIMA PARTIDA \n")
            clean_table()



    if results.count(1) > results.count(2):
        print(" **", p1, "GANHOU O JOGO ** \n       ** PARABÉNS **")

    elif results.count(2) > results.count(1):
        print("  **", p2, "GANHOU O JOGO ** \n       ** PARABÉNS **")

    elif results.count(3)==n_match or results.count(1)+results.count(2)+results.count(3)==n_match:
        print("         **EMPATE** \n VOCÊS DOIS JOGAM SUPER BEM!!")

game()
print("        FIM DO JOGO")