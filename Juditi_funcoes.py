import Funcoes_cores
import Funcoes_app_menu
from time import *
juditi_cash = 0
juditi_verde = Funcoes_cores.verde
juditi_vermelho = Funcoes_cores.vermelho
icone_juditi_1 = "(✿´‿`)"
icone_juditi_2 = "(◕‿◕✿)"
icone_juditi_3 = "(づ｡◕‿‿◕｡)づ"
icone_juditi_4 = "༼ つ ◕_◕ ༽つ"
icone_juditi_5 = "ლ(ಠ益ಠლ)"
icone_juditi_6 = "(｡◕‿‿◕｡)"
def contreles_juditi():
    while(True):
        print("(Juditi) (◕‿◕✿) >>> Sr Minhas funçoes estão limitadas ainda <<<")
        escolha = str(input("(Juditi) (◕‿◕✿) >>> Sr Clown Deseja Retornar [S/N] >>> ").upper())
        if(escolha == "S"):
            Funcoes_app_menu.login_usuario()
        else:
            True
def juditi_cash_Adimin():
    print()
def juditi_cash():
    print()
def info_juditi():
    while (True):
        print(Funcoes_cores.preto + "__" * 50, Funcoes_cores.original)
        print(juditi_vermelho + "(✿´‿`)" + Funcoes_cores.original + " INFO DA JUDITI".center(100))
        print(Funcoes_cores.preto + "__" * 50, Funcoes_cores.original)
        with open("info_juditi.txt", "r") as arquivo4:
            info_juditi_ler = arquivo4.read()
            info_juditi_ler = info_juditi_ler.split("\n")
        print(info_juditi_ler)
        escolha_voltar = input("(Juditi) (◕‿◕✿) >>> Quer voltar para tela login [S/N] <<").center(100).upper()
        if (escolha_voltar == "S"):
            print("(Juditi) (◕‿◕✿) >>> Obrigado Por ver Mural De Informações <<")
            sleep(4)
            Funcoes_app_menu.login_usuario()
        else:
            True