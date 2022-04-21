from time import sleep
import Funcoes_app_feed
import Funcoes_cores
import Juditi_funcoes
import Programador_social
import Funcoes_Carregamento
def login_usuario():
    with open("password_users.txt", "r") as password_users:
        password_user = password_users.read()
        password_user = password_user.split("\n")
    with open("name_users.txt", "r") as name_users:
        names_user = name_users.read()
        names_user = names_user.split("\n")
    try:
        print("< [1]- Fazer login > < [2]- Cadastra Novo User > < [3]- Caixa De ideias >".center(100))
        opcoes_user_inicio = int(input(Funcoes_cores.vermelho + "< [5]-(✿´‿`) info juditi >".center(100) + Funcoes_cores.original))
    except(ValueError,UnboundLocalError):
        print("(Juditi) (◕‿◕✿) >>> Esse Opção Não Existe")
        login_usuario()
    if (opcoes_user_inicio == 1):
        global names_user_digitado
        print(Funcoes_cores.ciano + "--" * 50, Funcoes_cores.original + "\n")
        names_user_digitado = input("(Juditi) (◕‿◕✿) >>> Digite seu nome de usuario >>> ").upper()
        password_digitado = input(("(Juditi) (◕‿◕✿) >>> Digite sua senha >>> "))
        password_digitado = str((password_digitado))
        names_user_digitado = str((names_user_digitado))

        if (names_user_digitado in names_user, password_digitado in password_user):
            sleep(0.5)
            Funcoes_Carregamento.carregando_login()
            sleep(5)
            Funcoes_app_feed.tela(names_user_digitado)
        else:
            print("(Juditi) (◕‿◕✿) >>> Nome de usuario ou senhas incorretas  <<<")
            Programador_social.app()
    elif (opcoes_user_inicio == 2):
        sleep(0.7)
        print("(Juditi) (◕‿◕✿) >>> Ola meu nome é juditi estou aqui para te ajudar se cadastrar com segurança <<<")
        nome_digitado_novos = input("(Juditi) (◕‿◕✿) >>> Digite um nome de usuario >>> ").upper()
        nome_digitado_novos = str((nome_digitado_novos))
        while (nome_digitado_novos in names_user):
            if (nome_digitado_novos in names_user):
                print("(Juditi) (｡◕‿‿◕｡) >>> Esse nome ja esta cadastrado no nosso App <<<")
                sleep(0.8)
                nome_digitado_novos = input("(Juditi) ლ(ಠ益ಠლ) >>> Digite nome de usuario valido >>> ").upper()
                nome_digitado_novos = str((nome_digitado_novos))
        else:
            print("(Juditi) (◕‿◕✿) >>> Nome de usuario valido <<< ")
            password_novos = str((input("(Juditi) (◕‿◕✿) >>> Agora digite uma senha >>> ")))
            while (password_novos in password_user):
                if (password_novos in password_user):
                    print("(Juditi) (◕‿◕✿) >>> Essa senha ja esta cadastrada para outro usuario <<<")
                    sleep(0.7)
                password_novos = input("(Juditi) ლ(ಠ益ಠლ) >>> Digite uma senha valida >>> ")
                password_novos = str((password_novos))
            else:
                Funcoes_Carregamento.perfil_cadastrando(nome_digitado_novos)
                with open("name_users.txt", "a") as aquivo:
                    aquivo.write("\n" + nome_digitado_novos)
                with open("password_users.txt", "a") as aquivo2:
                    aquivo2.write("\n" + password_novos)
                    Funcoes_Carregamento.carregamento_cadastrando()
    elif (opcoes_user_inicio == 3):
        print(Funcoes_cores.fbranco + "(◕‿◕✿) Ideias Para Juditi".center(100), Funcoes_cores.original)
        nome_secreto = str(input("(Juditi) (◕‿◕✿) >>> Digite nome secreto para anexar na sua ideia >>> ").center(100))
        if(nome_secreto == ''):
            print("(Juditi) ლ(ಠ益ಠლ) >>> Digita nome secreto >>>".center(100))
            nome_secreto = str(input("(Juditi) (◕‿◕✿) >>> Digite nome secreto para anexar na sua ideia >>> ").center(100))
            ideia_user = str(input("(Juditi) (◕‿◕✿) >>> Digite sua ideia >>> ").center(100))
        if(ideia_user == ''):
            print("(Juditi) ლ(ಠ益ಠლ) >>> Digita Sua ideia  >>>".center(100))
            ideia_user = str(input("(Juditi) (◕‿◕✿) >>> Digite sua ideia >>> ").center(100))
        sleep(0.05)
        with open("ideias_users.txt", "a") as arquivo3:
            arquivo3.write(f"\n({nome_secreto} >>> {ideia_user})")
        # print(cores.ciano+ "__" * 50, cores.original)
        Funcoes_Carregamento.salvamento_arquivos()
        Programador_social.app()
    elif (opcoes_user_inicio == 4):
        Juditi_funcoes.info_juditi()
    elif (opcoes_user_inicio == 32553257):
        sleep(5)
        while (True):
            with open("name_users.txt", "r") as aquivo9:
                ler_arquivos = aquivo9.read()
                ler_arquivos = ler_arquivos.split("\n")
                conta = 0
                for i in range(len(ler_arquivos)):
                    conta += 1
            print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
            sleep(0.01)
            Funcoes_Carregamento.carregamento_secreto()
            sleep(8)
            # print(cores.famarelo + "__" * 50, cores.original+"\n")
            print(Funcoes_cores.preto + Funcoes_cores.famarelo + "SALA CONFIGURAÇÃO DO CLOWN".center(100) + Funcoes_cores.original)
            print("(Juditi) (｡◕‿‿◕｡) >>> Seja Bem-vindo Sr Clown 🤡 >>>".center(100))
            print(f"(Juditi) ｡◕‿‿◕｡ >>> Estamos Com ({conta}) Cadastrados No Programador_Social Sr Clown 🤡 >>>".center(
                100))
            print(Funcoes_cores.famarelo + "__" * 50, Funcoes_cores.original)
            sleep(0.9)

            print(
                "< 1-ver Post Publicados 🗂️ > < 2-Ver Usuarios Cadastrados 🧑 > < 3-Altera Banco De Dados 🗒️ > \n < 4-"
                "Adicior Um Info No Mural 📍 > < 5-Adiministração Juditi_cash 💵 > < 6-Banco De Sujestão 🔊 >")
            escolha_clown = int(input(Funcoes_cores.vermelho + "< 7-(✿´‿`) Controles Da Juditi>".center(100) + Funcoes_cores.original))
            if (escolha_clown == 1):
                print()
            elif (escolha_clown == 2):
                with open("name_users.txt", "r") as aquivo7:
                    aquivo7 = aquivo7.read()
                    aquivo7 = aquivo7.split()
                with open("password_users.txt", "r") as aquivo4:
                    aquivo4 = aquivo4.read()
                    aquivo4 = aquivo4.split("\n")
                print(Funcoes_cores.famarelo + "__" * 50, Funcoes_cores.original + "\n")
                print("(Juditi) (｡◕‿‿◕｡) >>> Sr Clown Estou Varrendo Nosso Banco De Daddos <<<")
                sleep(5)
                print("(Juditi) (｡◕‿‿◕｡) >>> Sr Clown Estou Carregando ... <<<")
                print(Funcoes_cores.famarelo + "__" * 50, Funcoes_cores.original + "\n")
                sleep(5)
                for pos in range(0, len(aquivo7)):
                    if (pos % 1 == 0):
                        print("User >>> {}°{}".format(pos, aquivo7[pos]))
                print("(Juditi) (｡◕‿‿◕｡) >>> Sr Clown Esses São Usuarios ")
                sleep(9)
            elif (escolha_clown == 3):
                print("(Juditi) >>> ")
            elif (escolha_clown == 4):
                print()
            elif (escolha_clown == 5):
                Juditi_funcoes.contreles_juditi()
                print()
            elif (escolha_clown == 6):
                print()
            elif (escolha_clown == 7):
                carregamento_normal()
                Juditi_funcoes.contreles_juditi()
            elif (escolha_clown == 8, 9,):
                return 0
            else:
                True

