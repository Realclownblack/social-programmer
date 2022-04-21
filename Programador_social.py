from time import sleep
import Funcoes_app_menu
import Funcoes_animaçao
import Funcoes_cores
def app():
    while(True):
        print(Funcoes_cores.ciano+"__"*50)
        print(Funcoes_cores.verde+"(✿´‿`) Programador_Social".center(100).upper())
        sleep(0.4)
        print(Funcoes_cores.ciano+"--"*50,Funcoes_cores.original)
        Funcoes_animaçao.frase_dia()
        sleep(0.9)
        Funcoes_app_menu.login_usuario()
if __name__ == '__main__':
    app()
