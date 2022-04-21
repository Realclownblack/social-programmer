import Funcoes_Carregamento
import Funcoes_animaçao
import Funcoes_cores
import Programador_social


def tela(user_name):
    lista_dados_usuario = Funcoes_Carregamento.perfil_logando(user_name)
    seguidores_user = Funcoes_Carregamento.perfil_logado_seguidores(user_name)
    seguindo_user = Funcoes_Carregamento.perfil_logado_seguindo(user_name)
    coracoes = Funcoes_Carregamento.perfil_login_coracoes(user_name)
    while(True):
        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
        print(Funcoes_cores.famarelo+"< [1]- Postar > < [2]- Feed > < [3]- Perfil > < [4]- Jogos > < [5]- Achar Amigos > < [6]- Sair >".center(100),Funcoes_cores.original)
        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
        print("| Seguidores {} -------- Seguindo {} -------- Corações ❤ {} -------- Juditi_Cash {} -------- (◕‿◕✿) ".format(seguidores_user,seguindo_user,coracoes,lista_dados_usuario[0]))
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        escolha_usuario = int(input("(Juditi) >>> Escolhe Funçoes Do Feed >>> "))
        if(escolha_usuario == 1):
            contador_post = 0
            while(True):
                if(contador_post == 0):
                    print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                    print(Funcoes_cores.famarelo + "".center(100), Funcoes_cores.original)
                    print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                    print("| Seguidores {} -------- Seguindo {} -------- Corações ❤ {} -------- Juditi_Cash {} -------- (◕‿◕✿) ".format(seguidores_user,seguindo_user,coracoes,lista_dados_usuario[0]))
                    print("(Juditi) >>>  Pensando Alguma Coisa <<<")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    nome_assunto_escolhido = str(input("(Juditi) >>>  Digite o Assunto  >>> "))
                    contador_post += 1
                    if(contador_post == 1):
                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                        print(Funcoes_cores.famarelo + "".center(100), Funcoes_cores.original)
                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                        print("| Seguidores {} -------- Seguindo {} -------- Corações ❤ {} -------- Juditi_Cash {} -------- (◕‿◕✿) ".format(seguidores_user,seguindo_user,coracoes,lista_dados_usuario[0]))
                        print("(Juditi) >>>  Pensando Alguma Coisa <<<")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        post_do_usuario = str(input("(Juditi) >>> Digite Aqui >>>"))
                        with open('feed_Principal', 'a', encoding='utf8') as feed_Programador_social:
                            feed_Programador_social.write("\n{} Falando Sobre {} >>> ({}) ".format(user_name,nome_assunto_escolhido,post_do_usuario))
                        with open(f"funcoes_feed\{user_name}.txt", "a") as tre:
                            tre.write("\n{} Falando Sobre {} >>> ({}) ".format(user_name,nome_assunto_escolhido,post_do_usuario))
                        escolha_Funcao_feed = str(input("(Juditi) Continuar Postando No Feed [S/N] >>> ").upper())
                        if (escolha_Funcao_feed == "N"):
                            tela(user_name)
                        elif (escolha_Funcao_feed == "S"):
                            continue



        elif(escolha_usuario == 2):
            while(True):
                with open("name_users.txt","r",encoding="utf8")as nome_users:
                    nome_users = nome_users.read()
                    nome_users = nome_users.split("\n")
                with open('feed_Principal', 'r', encoding='utf8') as feed_Programador_social:
                    feed_Programador_social = feed_Programador_social.read()
                    feed_Programador_social = feed_Programador_social.split("\n")
                for decer in range(0, len(feed_Programador_social)):
                    if (decer % 1 == 0):
                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                        print(Funcoes_cores.famarelo + "< [1]- Decer A Barrinha > < [2]- Sair >".center(100), Funcoes_cores.original)
                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                        print("| Seguidores {} -------- Seguindo {} -------- Corações ❤ {} -------- Juditi_Cash {} -------- (◕‿◕✿) ".format(seguidores_user,seguindo_user,coracoes,lista_dados_usuario[0]))
                        try:
                            print("")
                            print("(Juditi) Post  {} ".format(feed_Programador_social[decer+1]).center(10))
                            print("=="*5)
                            print("(Juditi) Post  {} ".format(feed_Programador_social[decer+2]).center(10))
                            print("=="*5)
                            print("(Juditi) Post  {} ".format(feed_Programador_social[decer+3]).center(10))
                            print("")
                        except IndexError:
                            print("(Juditi) >>> Acabou os Post <<<")
                            True
                        escolha_decer_feed = str(input("(Juditi) Para dar Coraçãozinho Digite Nome Usuario >>> ").upper())
                        if (escolha_decer_feed == "2"):
                            tela(user_name)
                        elif (escolha_decer_feed == '1'):
                            True
                        elif(escolha_decer_feed in nome_users):
                            with open(f"funcoes_coracoes\{escolha_usuario}.txt", "a", encoding="utf8") as aquivoO:
                                aquivoO.write(f"\n{user_name}")
                                True

        elif(escolha_usuario == 3):
            while(True):
                elementos_de_perfil = Funcoes_Carregamento.perfil_carregamentos(user_name)
                try:
                    print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                    print(Funcoes_cores.fazul + "< [1]- Editar Bio > < [2]- Minhas Publicação > < [3]- Seguindo > < [4]- Senguidores > < [5]- chat > < [6]- Sair >".center(100), Funcoes_cores.original)
                    print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                    print("| Seguidores {}  ".format(seguidores_user),end="|"),print(".--------------------------------------------------------------------------------.")
                    print("| Seguindo {} ".format(seguindo_user),end="   |"),print(f"| {elementos_de_perfil[1]}                                       ")
                    print("| Corações {} ".format(coracoes),end="      |"),print(f"| {elementos_de_perfil[2]}                                             ")
                    print("| Juditi_Cash {}".format(lista_dados_usuario[0]),end=" |"),print("| ______________________________________________________________________________ |")
                    print("| ------------- |")
                    print(f"|     {user_name}")
                    print(f"|     {user_name}")
                    print("| ------------- |")
                    escolha_usuario = int(input("(Juditi) >>> Escolhe Funçoes Do Feed >>> "))
                except(IndexError):
                    True
                if(escolha_usuario == 1):
                    while(True):
                        contador_modificarcoes = 0
                        try:
                            print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                            print(Funcoes_cores.famarelo + "__" * 50, Funcoes_cores.original)
                            print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                            print("| Seguidores {}  ".format(seguidores_user), end="|"), print(".--------------------------------------------------------------------------------.")
                            print("| Seguindo {} ".format(seguindo_user), end="   |"), print(f"| {elementos_de_perfil[1]}                                              ")
                            print("| Corações {}  ".format(coracoes), end="      |"), print(f"| {elementos_de_perfil[2]}                                               ")
                            print("| Juditi_Cash {}".format(lista_dados_usuario[0]), end=" |"), print("| ______________________________________________________________________________ |")
                            print("| ------------- |")
                            print(f"|     {user_name}")
                            print(f"|     {user_name}")
                            print("| ------------- |")
                        except(IndexError):
                            print("(Juditi) >>> Erro 333 [Digitar Ate 75 Caracter Por Linha]")
                            True
                        Nova_bio = str(input("(Juditi) >>> Digite sua bio nova [De Ate 75 Caracter Por Linha] >>>"))
                        tamanho = Funcoes_Carregamento.saber_tamanho(Nova_bio)
                        if(tamanho <= 75):
                            with open(f"funcoes_internas_bio\{user_name}_bio.txt", "w") as dus:
                                pass
                            with open(f"funcoes_internas_bio\{user_name}_bio.txt", "a") as dus:
                                dus.write(f"\n{Nova_bio}")
                                contador_modificarcoes += 1

                        if(contador_modificarcoes == 1):
                                    print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                    print("| Seguidores {}  ".format(seguidores_user),end="|"), print(".---------------------------------------------------------------------------------.")
                                    print("| Seguindo {} ".format(seguindo_user), end="   |"), print(f"| {elementos_de_perfil[1]}                                             ")
                                    print("| Corações {} ".format(coracoes), end="      |"), print(f"| {elementos_de_perfil[2]}                                            ")
                                    print("| Juditi_Cash {}".format(lista_dados_usuario[0]), end=" |"), print("| ______________________________________________________________________________ |")
                                    print("| ------------- |")
                                    print(f"|     {user_name}")
                                    print(f"|     {user_name}")
                                    print("| ------------- |")
                                    Nova_bio = str(input("(Juditi) >>> Digite sua bio nova [De Ate 75 Caracter Por Linha] >>>"))
                                    tamanho = Funcoes_Carregamento.saber_tamanho(Nova_bio)
                                    if (tamanho <= 75):
                                        with open(f"funcoes_internas_bio\{user_name}_bio.txt", "a") as dus:
                                            dus.write(f"\n{Nova_bio}")
                                            tela(user_name)
                                    else:
                                        print("(Juditi) >>> Erro 333 [Digitar Ate 75 Caracter Por Linha]")
                                        True
                elif(escolha_usuario == 2):
                    while(True):
                        with open(f"funcoes_feed\{user_name}.txt","r",encoding="utf8")as tis:
                            publicacoes = tis.read()
                            publicacoes = publicacoes.split("\n")
                            for decer in range(len(publicacoes)):
                                if(decer % 1 == 0):
                                    try:
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print(Funcoes_cores.fazul + "< [1]- Apagar As Puplicação > < [2]- Decer Os Post > < [3]- Sair > ".center(100), Funcoes_cores.original)
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print("| Seguidores {}  ".format(seguidores_user),end="|"), print(".--------------------------------------------------------------------------------.")
                                        print("| Seguindo {} ".format(seguindo_user),end="   |"), print(f"| {elementos_de_perfil[decer+1]}")
                                        print("| Corações {} ".format(coracoes),end="      |"), print(f"| {elementos_de_perfil[decer+2]}")
                                        print("| Juditi_Cash {}".format(lista_dados_usuario[0]),end=" |"), print("| ______________________________________________________________________________ |")
                                        print("| ------------- |")
                                        print(f"|     {user_name}",end="    |"),print(f"{publicacoes[decer+1]}")
                                        print(f"|     {user_name}",end="    |"),print(f"{publicacoes[decer+2]}")
                                        print("| ------------- |")
                                        print("")
                                    except(IndexError ):
                                        print("".center(100))
                                        print("(Juditi) >>> Acabou Os Post <<<".center(100))
                                        True
                                    escolha_usuario = int(input("(Juditi) >>> Escolhe Um Funçoes >>> "))
                                    if(escolha_usuario == 1):
                                        with open(f"funcoes_feed\{user_name}.txt", "w", encoding="utf8"):
                                            True
                                    elif(escolha_usuario == 2):
                                            True
                                    elif(escolha_usuario == 3):
                                            tela(user_name)
                elif (escolha_usuario == 3):
                    while(True):
                        with open(f"funcoes_seguindo\{user_name}.txt", "r", encoding="utf8") as tis:
                            seguindo = tis.read()
                            seguindo = seguindo.split("\n")
                            for decer in range(len(seguindo)):
                                if (decer % 1 == 0):
                                    try:
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print(Funcoes_cores.famarelo + "< [1]- Decer Barrinha > < [2]- Sair >".center(100), Funcoes_cores.original)
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print("(Juditi) >>> Pessoas Que Você Segui <<< ")
                                        print("(Juditi) >>> Para Deixar De Seguir Alguem Digite Seu Nome <<<")
                                        print("==" * 10)
                                        print(f"{seguindo[decer+1]}")
                                        print(f"{seguindo[decer+2]}")
                                        print(f"{seguindo[decer+3]}")
                                        print(f"{seguindo[decer+4]}")
                                        print("==" * 10)
                                    except(IndexError):
                                        print("(Juditi) >>> Você So Esta Seguindo Esses <<<")
                                        True
                                    escolha_usuario = str(input("(Juditi) >>> Para Deixar De Seguir Alguem Digite O Nome >>> ").upper())
                                    if (escolha_usuario == "1"):
                                        True
                                    elif (escolha_usuario in seguindo):
                                            with open(f"funcoes_seguindo\{user_name}.txt", "r", encoding="utf8") as lod:
                                                lod = lod.read()
                                                lod = lod.split("\n")
                                                novos_apagar = lod.index(escolha_usuario)
                                                nova_lista = lod.pop(novos_apagar)
                                                nova_lista = str(nova_lista)
                                            with open(f"funcoes_seguindo\{user_name}.txt","w",encoding="utf8")as aquivoss:
                                                aquivoss.write(f"\n{nova_lista}")
                                            with open(f"funcoes_seguidores\{escolha_usuario}.txt", "r",encoding="utf8") as aquivop:
                                                aquivop = aquivop.read()
                                                aquivop = aquivop.split("\n")
                                                novos_apagar = aquivop.index(user_name)
                                                lista_nova = aquivop.pop(novos_apagar)
                                                lista_nova =str(lista_nova)
                                            with open(f"funcoes_seguidores\{escolha_usuario}.txt", "w",encoding="utf8") as aquivoo:
                                                aquivoo.write(f"\n{lista_nova}")
                                                True
                                    elif (escolha_usuario == "2"):
                                        tela(user_name)
                elif(escolha_usuario == 4):
                    while (True):
                        with open(f"funcoes_seguidores\{user_name}.txt", "r", encoding="utf8") as tis:
                            seguidores = tis.read()
                            seguidores = seguidores.split("\n")
                            for decer in range(len(seguidores)):
                                if (decer % 1 == 0):
                                    try:
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print(Funcoes_cores.famarelo + "< [1] - Decer Barrinha > < [2]- Sair >".center(100), Funcoes_cores.original)
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print("(Juditi) >>> Pessoas Que Segue Você  <<< ")
                                        print("(Juditi) >>> Para Bloquear Pessoas Que Te Segue <<<")
                                        print("==" * 10)
                                        print(f"{seguidores[decer+1]}")
                                        print(f"{seguidores[decer+2]}")
                                        print(f"{seguidores[decer+3]}")
                                        print(f"{seguidores[decer+4]}")
                                        print("==" * 10)
                                    except(IndexError):
                                        print("(Juditi) >>> So esses Estão Te Seguindo <<<")
                                        True
                                    escolha_usuario = str(input("(Juditi) >>> Para Bloquear Alguem Que Te Segue Digite O Nome >>> ").upper())
                                    if (escolha_usuario == "1"):
                                        True
                                    elif(escolha_usuario == "2"):
                                        tela(user_name)
                                    elif (escolha_usuario in seguidores):
                                            with open(f"funcoes_seguindo\{user_name}.txt", "r", encoding="utf8") as lod:
                                                lod = lod.read()
                                                lod = lod.split("\n")
                                                novos_apagar = lod.index(escolha_usuario)
                                                nova_lista = lod.pop(novos_apagar)
                                                nova_lista = str(nova_lista)
                                            with open(f"funcoes_seguindo\{user_name}.txt", "w",encoding="utf8") as aquivoss:
                                                aquivoss.write(f"\n{nova_lista}")
                                            with open(f"funcoes_seguidores\{escolha_usuario}.txt", "r",encoding="utf8") as aquivop:
                                                aquivop = aquivop.read()
                                                aquivop = aquivop.split("\n")
                                                novos_apagar = aquivop.index(user_name)
                                                lista_nova = aquivop.pop(novos_apagar)
                                                lista_nova = str(lista_nova)
                                            with open(f"funcoes_seguidores\`{escolha_usuario}.txt", "w",encoding="utf8") as aquivoo:
                                                aquivoo.write(f"\n{lista_nova}")
                                                True
                elif(escolha_usuario == 5):
                    while (True):
                        with open(f"funcoes_seguindo\{user_name}.txt", "r", encoding="utf8") as tis:
                            seguindo = tis.read()
                            seguindo = seguindo.split("\n")
                            for decer in range(len(seguindo)):
                                if (decer % 1 == 0):
                                    try:
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print(Funcoes_cores.famarelo + "< [1]- Decer Barrinha > < [2]- Sair >".center(100), Funcoes_cores.original)
                                        print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                                        print("(Juditi) >>> Pessoas Que Você Segui <<< ")
                                        print("(Juditi) >>> Para Abri Chat Digite Nome Da Pessoa <<<")
                                        print("==" * 10)
                                        print("")
                                        print("")
                                        print("")
                                        print("")
                                        print("==" * 10)
                                    except(IndexError):
                                        print("(Juditi) >>> Você So Esta Seguindo Esses <<<")
                                        True
                                    escolha_usuario = str(input("(Juditi) >>> Para Deixar De Seguir Alguem Digite O Nome >>> ").upper())
                elif(escolha_usuario == 6):
                    tela(user_name)

        elif(escolha_usuario == 4):
            True
        elif(escolha_usuario == 5):
            while(True):
                with open("name_users.txt", "r", encoding="utf8") as tis:
                    Para_Seguir = tis.read()
                    Para_Seguir = Para_Seguir.split("\n")
                    for decer in range(len(Para_Seguir)):
                        if (decer % 1 == 0):
                            print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                            print(Funcoes_cores.fazul + "< [1]- Decer Barrinha > < [2]- Sair >".center(100), Funcoes_cores.original)
                            print(Funcoes_cores.ciano + "__" * 50, Funcoes_cores.original)
                            try:
                                print("(Juditi) >>>  Para Seguir Alguem Digite Seu Nome <<<")
                                print("")
                                print("")
                                print(f"{Para_Seguir[decer+1]}")
                                print(f"{Para_Seguir[decer+2]}")
                                print(f"{Para_Seguir[decer+3]}")
                                print(f"{Para_Seguir[decer+4]}")
                                print("")
                            except(IndexError):
                                    print("(Juditi) >>> Acabou os Amiguinhos Para Seguir <<<")
                            escolha_usuario = str(input("(Juditi) >>> Para Seguir Alguem Digite Seu Nome >>> ").upper())
                            str(escolha_usuario)
                            if(escolha_usuario == "1"):
                                True
                            elif(escolha_usuario == "2"):
                                tela(user_name)
                            elif(escolha_usuario in Para_Seguir):
                                with open(f"funcoes_seguindo\{user_name}.txt","a",encoding="utf8")as trep:
                                    trep.write(f"\n{escolha_usuario}")
                                with open(f"funcoes_seguidores\{escolha_usuario}.txt", "a",encoding="utf8") as aquivob:
                                    aquivob.write(f"\n{user_name}")

                                True
        elif(escolha_usuario == 6):
            Funcoes_animaçao.animaçao1()
            Programador_social.app()














