from random import choice
from time import sleep
import Funcoes_cores

def animaçao1():
    for contador_animacao in range(0,6):
        if(contador_animacao == 0):
            print("(づ｡◕‿‿◕｡)づ", end=" 👣"*2)
            sleep(0.8)
        elif(contador_animacao == 1):
            print("(づ｡◕‿‿◕｡)づ",end=" 👣"*2)
            sleep(0.8)
        elif (contador_animacao == 2):
            print("(づ｡◕‿‿◕｡)づ", end=" 👣" * 2)
            sleep(0.8)
        elif (contador_animacao == 3):
            print("(づ｡◕‿‿◕｡)づ", end=" 👣" * 2)
            sleep(0.8)
        elif (contador_animacao == 4):
            print("(づ｡◕‿‿◕｡)づ", end=" 👣"*1)
            sleep(0.8)
        elif (contador_animacao == 5):
            print("",end=""*2)
            sleep(0.8)
            print("\n")
        elif(contador_animacao == 6):
            print(" ", end="" * 2)
            print("\n")
def animaçao2():
    for contador2 in range(0,8):
        print("",end=""*1)
def frase_dia():
    with open("frases_dia.txt","r",encoding="utf8")as frases:
        frases_dia = frases.read()
        frases_dia = frases_dia.split("\n")
        frases_dia = choice(frases_dia)
        sleep(0.7)
        print(Funcoes_cores.amarelo+"{}".format(frases_dia).center(100).upper(),Funcoes_cores.original)
        #escolha = choice(lista_palavras)
        #numero_dica = lista_palavras.index(escolha)
        sleep(0.8)
        print(Funcoes_cores.ciano+"__"*50,Funcoes_cores.original)