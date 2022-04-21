from tqdm import tqdm
import Funcoes_cores
import time
from time import sleep
import Programador_social
import Juditi_funcoes
import os

def perfil_cadastrando(Qual_nome_carregar):
    with open(f"funcoes_juditi_cash\{Qual_nome_carregar}.txt","a") as per:
        per.write("15.00")
    with open(f"funcoes_internas_bio\{Qual_nome_carregar}_bio.txt", "a") as dus:
         dus.write("\n (Juditi) ... Fale Sobre Você"+"\n ............... ")
    with open(f"funcoes_seguindo\{Qual_nome_carregar}.txt", "a", encoding="utf8") as trep:
        trep.write("")
    with open(f"funcoes_seguidores\{Qual_nome_carregar}.txt", "a", encoding="utf8") as aquivob:
        aquivob.write("")
    with open(f"funcoes_coracoes\{Qual_nome_carregar}.txt", "a", encoding="utf8") as aquivoO:
        aquivoO.write("")

def perfil_logando(Qual_nome_login):
        with open(f"funcoes_juditi_cash\{Qual_nome_login}.txt","r") as perfiller:
            perfiller = perfiller.read()
            perfiller = perfiller.split("\n")
        return perfiller
def perfil_logado_seguidores(Qual_nome_login):
    with open(f"funcoes_seguidores\{Qual_nome_login}.txt", "r", encoding="utf") as furg:
        furg = furg.read()
        lista_seguidores = furg.split("\n")
    for elementos in  range(len(lista_seguidores)):
        pass
    return elementos
def perfil_logado_seguindo(Qual_nome_login):
    with open(f"funcoes_seguindo\{Qual_nome_login}.txt", "r", encoding="utf") as furg:
        furg = furg.read()
        lista_seguindo = furg.split("\n")
    for elementos1 in  range(len(lista_seguindo)):
        pass
    return elementos1
def perfil_login_coracoes(Qual_nome_login):
    with open(f"funcoes_coracoes\{Qual_nome_login}.txt", "r", encoding="utf8") as aquivoO:
        aquivoO = aquivoO.read()
        aquivoO = aquivoO.split("\n")
    for elementos2 in range(len(aquivoO)):
        pass
    return elementos2

def perfil_carregamentos(Qual_nome_login):
    with open(f"funcoes_internas_bio\{Qual_nome_login}_bio.txt","r") as dus:
        dus = dus.read()
        dus = dus.split("\n")
    return dus

def carregamento_secreto():
    for i in tqdm(range(101), desc=" Carregando… ", ascii=False, ncols=75):
        time.sleep(0.09)
    print(
        Funcoes_cores.vermelho + "(Juditi) (▀̿Ĺ̯▀̿̿) >>> Sr Clown  Funçoes Adimnistrador Sendo Abilitada" + Funcoes_cores.original)


def carregando_login():
    for i in tqdm(range(100), desc="Loading…", ascii=False, ncols=75):
        time.sleep(0.1)
    print("(Juditi) (ღ˘⌣˘ღ) >>> loadind feito com sucesso .... ")


def carregamento_cadastrando():
    sleep(0.04)
    for i in tqdm(range(100), desc="Cadastrando >>> ", ascii=False, ncols=75):
        time.sleep(0.04)
    print("(Juditi) (◕‿◕✿) >>> Parabens você foi cadastrado com sucesso <<<")
    sleep(0.09)
    salvamento_arquivos()
    Programador_social.app()
def saber_tamanho(Qual_tamanho):
    for tamanho in range(len(Qual_tamanho)):
     return tamanho


def carregamento_normal():
    for i in tqdm(range(101), desc="Loading >>> ", ascii=False, ncols=75):
        time.sleep(0.01)


def apagar():
    os.system('cls' if os.name == 'nt' else 'clear')
    # os.system('clear') or None


def salvamento_arquivos():
    print("(Juditi) " + Juditi_funcoes.juditi_verde + Juditi_funcoes.icone_juditi_6 + ">>> Esperando salvamento dos arquivos <<< ")
    for i in tqdm(range(100), desc="Salvando >>> ", ascii=False, ncols=85):
        time.sleep(0.09)



