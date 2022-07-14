from PyQt6 import uic, QtWidgets, QtGui
from PyQt6.QtCore import Qt
import sqlite3
import time
import qrcode

###################################################################
app = QtWidgets.QApplication([])
admAtual = ''
email_admAtual = ''
clienteAtual = ''
email_clienteAtual = ''
eventoAtual = ''
tipo = ''
qtd = 0
comprados = 0                                                         
# importando as telas.
inicio = uic.loadUi('./telas/tela_inicio.ui')
loginAdm = uic.loadUi('./telas/tela_loginAdm.ui')
loginCliente = uic.loadUi('./telas/tela_loginCliente.ui')
cadastroAdm = uic.loadUi('./telas/tela_cadastroAdm.ui')
cadastroCliente = uic.loadUi('./telas/tela_cadastroCliente.ui')
perfilAdm = uic.loadUi('./telas/tela_perfilAdm.ui')
perfilCliente = uic.loadUi('./telas/tela_perfilCliente.ui')
postarEvento = uic.loadUi('./telas/tela_postEvento.ui')
dadosAdm = uic.loadUi('./telas/tela_dadosAdm.ui')
dadosCliente = uic.loadUi('./telas/tela_dadosCliente.ui')
principal = uic.loadUi('./telas/tela_principal.ui')
detalhes_eventos = uic.loadUi('./telas/tela_detalheEvento.ui')
###################################################################

# 1 banco, 3 tabelas principais (adm; cliente; eventos.)
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS adm (usuario TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, telefone TEXT UNIQUE NOT NULL, senha TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS cliente (usuario TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, telefone TEXT UNIQUE NOT NULL, cpf TEXT UNIQUE NOT NULL, senha TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS eventos (ID INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT UNIQUE NOT NULL, tipo TEXT NOT NULL, data NOT NULL, hora NOT NULL, local TEXT NOT NULL, qtdIngr INTEGER NOT NULL, contato TEXT NOT NULL, comprado INTEGER NOT NULL)")   

def atualizaLista():
    cursor.execute("SELECT * FROM eventos")
    dados_lidos = cursor.fetchall()
    principal.relatorio.setColumnCount(4)
    principal.relatorio.setRowCount(len(dados_lidos))
            
    for i in range(0, len(dados_lidos)):
        for j in range(0,4):
            principal.relatorio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def esperarAdm():
    time.sleep(1)
    cadastroAdm.hide() or loginAdm.hide()
    perfilAdm.show() 

def esperarCliente():
    time.sleep(1)
    cadastroCliente.hide() or loginCliente.hide()
    perfilCliente.show() 

def salvar_dadosAdm():
    usuario = cadastroAdm.usuarioAdm.text()
    email = cadastroAdm.emailAdm.text()
    telefone = cadastroAdm.telefoneAdm.text() 
    senha = cadastroAdm.senhaAdm.text()
    confirmacao = cadastroAdm.confirmasenhaAdm.text()

    if (senha != '') and (usuario != '') and (email != '') and (telefone != '') and (senha == confirmacao):
        try:
            telefone = int(telefone)
            cursor.execute("INSERT INTO adm (usuario, email, telefone, senha) VALUES (?,?,?,?)", (usuario, email, telefone, senha))         
            banco.commit()
            esperarAdm()
            cursor.execute(f"SELECT email FROM adm WHERE usuario = '{usuario}'")
            global admAtual, email_admAtual
            admAtual = usuario
            email_admAtual = cursor.fetchall()
            perfilAdm.olaAdm.setText(f'Olá, {admAtual}!')
            perfilAdm.emailAdm.setText(f'{email_admAtual[0][0]}')
            #-=-=-=--=-=-=---=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=
            cadastroAdm.erro.setText('')
            cadastroAdm.usuarioAdm.setText('')
            cadastroAdm.emailAdm.setText('')
            cadastroAdm.telefoneAdm.setText('')
            cadastroAdm.senhaAdm.setText('')
            cadastroAdm.confirmasenhaAdm.setText('')
            #-=-=-=--=-=-=---=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=
            dadosAdm.nome.setText(f'{usuario}')
            dadosAdm.email.setText(f'{email}')
            dadosAdm.telefone.setText(f'{telefone}')
            dadosAdm.senha.setText(f'{senha}')
            
        except sqlite3.Error as erro:
            print('Erro ao inserir dados:', erro)
            cadastroAdm.erro.setText(f'{erro} já está em uso.')
        except ValueError:
            cadastroAdm.erro.setText('Telefone inválido.')

    else: 
        cadastroAdm.erro.setText('Campos vazios ou confirmação de senha inválida.')

def salvar_dadosCliente():
    usuario = cadastroCliente.usuarioCliente.text()
    email = cadastroCliente.emailCliente.text()
    telefone = cadastroCliente.telefoneCliente.text()
    cpf = cadastroCliente.cpfCliente.text()
    senha = cadastroCliente.senhaCliente.text()
    confirmacao = cadastroCliente.confirmasenhaCliente.text()

    if (senha != '') and (usuario != '') and (email != '') and (telefone != '') and (cpf != '') and (senha == confirmacao):
        try:
            telefone = int(telefone)
            cpf = int(cpf)
            cursor.execute("INSERT INTO cliente (usuario, email, telefone, cpf, senha) VALUES (?,?,?,?,?)", (usuario, email, telefone, cpf, senha))         
            banco.commit()
            esperarCliente()
            cursor.execute(f"SELECT email FROM cliente WHERE usuario = '{usuario}'")
            global clienteAtual, email_clienteAtual
            clienteAtual = usuario
            email_clienteAtual = cursor.fetchall()
            perfilCliente.olaCliente.setText(f'Olá, {clienteAtual}!')
            perfilCliente.emailCliente.setText(f'{email_clienteAtual[0][0]}')
            #-=-=-=--=-=-=---=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=
            cadastroCliente.erro2.setText('')
            cadastroCliente.usuarioCliente.setText('')
            cadastroCliente.emailCliente.setText('')
            cadastroCliente.telefoneCliente.setText('')
            cadastroCliente.senhaCliente.setText('')
            cadastroCliente.confirmasenhaCliente.setText('')
            #-=-=-=--=-=-=---=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=
            dadosCliente.nome.setText(f'{usuario}')
            dadosCliente.email.setText(f'{email}')
            dadosCliente.telefone.setText(f'{telefone}')
            dadosCliente.cpf.setText(f'{cpf}')
            dadosCliente.senha.setText(f'{senha}')

        except sqlite3.Error as erro:
            print('Erro ao inserir dados:', erro)
            cadastroCliente.erro2.setText(f'{erro} já está em uso.')
        except ValueError:
            cadastroCliente.erro2.setText('Telefone ou CPF inválido.')

    else: 
        cadastroCliente.erro2.setText('Campos vazios ou confirmação de senha inválida.')

def entrarAdm():
    usuario = loginAdm.userloginAdm.text()
    senha = loginAdm.senhaloginAdm.text()
    if (usuario != ''):
        try:
            cursor.execute(f"SELECT senha FROM adm WHERE usuario = '{usuario}'")
            senhacorreta = cursor.fetchall()
            if (senha != '') and senha == senhacorreta[0][0]:
                esperarAdm()
                cursor.execute(f"SELECT email FROM adm WHERE usuario = '{usuario}'")
                global admAtual, email_admAtual
                admAtual = usuario
                email_admAtual = cursor.fetchall()
                perfilAdm.olaAdm.setText(f'Olá, {admAtual}!')
                perfilAdm.emailAdm.setText(f'{email_admAtual[0][0]}')
                # =-=-=-==-=----=--=-=-=--=-=---=-=-=
                loginAdm.userloginAdm.setText('')
                loginAdm.senhaloginAdm.setText('')
                loginAdm.texto_erro.setText('')
                # =-=-=-==-=----=--=-=-=--=-=---=-=-=
                dadosAdm.nome.setText(f'{usuario}')
                dadosAdm.email.setText(f'{email_admAtual[0][0]}')
                cursor.execute(f"SELECT telefone FROM adm WHERE usuario = '{usuario}'")
                telefone = cursor.fetchall()
                dadosAdm.telefone.setText(f'{telefone[0][0]}')
                dadosAdm.senha.setText(f'{senha}')
            else: 
                loginAdm.texto_erro.setText('Campo de senha vazio ou senha inválida.')

        except IndexError:
            loginAdm.texto_erro.setText('Usuário ou senha incorretos.')
    else:
        loginAdm.texto_erro.setText('Preencha o campo de usuário.')

def entrarCliente():
    usuario = loginCliente.userloginCliente.text()
    senha = loginCliente.senhaloginCliente.text()

    if (usuario != ''):
        try:
            cursor.execute(f"SELECT senha FROM cliente WHERE usuario = '{usuario}'")
            senhacorreta = cursor.fetchall()
            if (senha != '') and senha == senhacorreta[0][0]:
                esperarCliente()
                cursor.execute(f"SELECT email FROM cliente WHERE usuario = '{usuario}'")
                global clienteAtual, email_clienteAtual
                clienteAtual = usuario
                email_clienteAtual = cursor.fetchall()
                perfilCliente.olaCliente.setText(f'Olá, {clienteAtual}!')
                perfilCliente.emailCliente.setText(f'{email_clienteAtual[0][0]}')
                # =-=-=-==-=----=--=-=-=--=-=---=-=-=
                loginCliente.userloginCliente.setText('')
                loginCliente.senhaloginCliente.setText('')
                loginCliente.texto_erro.setText('')
                # =-=-=-==-=----=--=-=-=--=-=---=-=-=
                dadosCliente.nome.setText(f'{usuario}')
                dadosCliente.email.setText(f'{email_clienteAtual[0][0]}')
                cursor.execute(f"SELECT telefone FROM cliente WHERE usuario = '{usuario}'")
                telefone = cursor.fetchall()
                dadosCliente.telefone.setText(f'{telefone[0][0]}')
                cursor.execute(f"SELECT cpf FROM cliente WHERE usuario = '{usuario}'")
                cpf = cursor.fetchall()
                dadosCliente.cpf.setText(f'{cpf[0][0]}')
                dadosCliente.senha.setText(f'{senha}')
            else:
                loginCliente.texto_erro.setText('Campo de senha vazio ou senha inválida.')

        except IndexError:
            loginCliente.texto_erro.setText('Usuário ou senha incorretos.')
    else:
        loginCliente.texto_erro.setText('Preencha o campo de usuário.')

def abrirloginAdm():
    inicio.hide()
    loginAdm.show()
    global clienteAtual
    clienteAtual = ''

def abrirloginCliente():
    inicio.hide() or perfilAdm.hide()
    loginCliente.show()
    global admAtual
    admAtual = ''

def abrirCadastroAdm():
    loginAdm.hide()
    cadastroAdm.show()
    loginAdm.userloginAdm.setText('')
    loginAdm.senhaloginAdm.setText('')
    loginAdm.texto_erro.setText('')

def abrirCadastroCliente():
    loginCliente.hide()
    cadastroCliente.show()
    loginCliente.userloginCliente.setText('')
    loginCliente.senhaloginCliente.setText('')
    loginCliente.texto_erro.setText('')

def abrirdadosAdm():
    dadosAdm.erro.setText('')
    perfilAdm.hide()
    dadosAdm.show()

def abrirdadosCliente():
    dadosCliente.erro.setText('')
    perfilCliente.hide()
    dadosCliente.show()

def deleteAdm():
    telefone = dadosAdm.telefone.text()
    senha = dadosAdm.senha.text()
    confirmacao = dadosAdm.confirmacao.text()
    if senha == confirmacao:
        try:
            cursor.execute(f"DELETE FROM adm WHERE telefone = {telefone}")
            banco.commit()
            dadosAdm.hide()
            loginAdm.show()
            #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            dadosAdm.nome.setText('')
            dadosAdm.email.setText('')
            dadosAdm.telefone.setText('')
            dadosAdm.senha.setText('')
            dadosAdm.confirmacao.setText('')
        except sqlite3.Error as erro:
            print(erro)
    else:
        dadosAdm.erro.setText('Insira a senha correta para continuar.')

def deleteCliente():
    cpf = dadosCliente.cpf.text()
    senha = dadosCliente.senha.text()
    confirmacao = dadosCliente.confirmacao.text()
    if (senha == confirmacao):
        try:
            cursor.execute(f"DELETE FROM cliente WHERE cpf = {cpf}")
            banco.commit()
            dadosCliente.hide()
            loginCliente.show()
            #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            dadosCliente.nome.setText('')
            dadosCliente.email.setText('')
            dadosCliente.telefone.setText('')
            dadosCliente.senha.setText('')
            dadosCliente.confirmacao.setText('')
        except sqlite3.Error as erro:
            print(erro)
    else:
        dadosCliente.erro.setText('Insira a senha correta para continuar.')          

def abrirPostarEvento():
    perfilAdm.hide()
    postarEvento.show()

# FUNÇÕES DE POST
def confereEvento():
    nome = postarEvento.nomeEvento.text()
    data = postarEvento.dataEvento.date()
    hora = postarEvento.horaEvento.time()
    local = postarEvento.localEvento.text()
    qtd_ingressos = postarEvento.qtd_Ingressos.text()
    global tipo
    #print(hora.toString(Qt.DateFormat.ISODate))
    #print(data.toString(Qt.DateFormat.ISODate))

    if postarEvento.tipoDanca.isChecked():
        postarEvento.imagem.setPixmap(QtGui.QPixmap('./imgs/dance.png'))
        tipo = 'Evento de Dança'

    elif postarEvento.tipoPeca.isChecked():
        postarEvento.imagem.setPixmap(QtGui.QPixmap('./imgs/peca.png'))
        tipo = 'Peça Teatral'

    elif postarEvento.tipoMusical.isChecked():
        postarEvento.imagem.setPixmap(QtGui.QPixmap('./imgs/musical.png'))
        tipo = 'Evento Musical'
    
    postarEvento.descricao.setText(f'Nome: {nome}\nData: {data.toString(Qt.DateFormat.ISODate)}\nHora: {hora.toString(Qt.DateFormat.ISODate)}\nLocal: {local}\nQtd Ingressos: {qtd_ingressos}\n{tipo}')
    
def salvaEvento(): 
    nome = postarEvento.nomeEvento.text()
    data = postarEvento.dataEvento.date()
    hora = postarEvento.horaEvento.time()
    local = postarEvento.localEvento.text()
    qtd_ingressos = postarEvento.qtd_Ingressos.text()
    radiobt = postarEvento.tipoDanca.isChecked() or postarEvento.tipoPeca.isChecked() or postarEvento.tipoMusical.isChecked()
    global tipo, email_admAtual, comprados

    if (nome != '') and (local != '') and (qtd_ingressos != '') and radiobt:
        try:
            data = data.toString(Qt.DateFormat.ISODate)
            hora = hora.toString(Qt.DateFormat.ISODate)
            qtd_ingressos = int(qtd_ingressos)
            email = email_admAtual[0][0]

            cursor.execute("INSERT INTO eventos (nome, tipo, data, hora, local, qtdingr, contato, comprado) VALUES (?,?,?,?,?,?,?,?)", (nome, tipo, data, hora, local, qtd_ingressos, email, comprados))         
            banco.commit()
            #-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=--
            postarEvento.nomeEvento.setText('')
            postarEvento.localEvento.setText('')
            postarEvento.qtd_Ingressos.setText('')
            #-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=--
            cursor.execute("SELECT * FROM eventos")
            dados_lidos = cursor.fetchall()
            principal.relatorio.setColumnCount(4)
            principal.relatorio.setRowCount(len(dados_lidos))
            
            for i in range(0, len(dados_lidos)):
                for j in range(0,4):
                    principal.relatorio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

            time.sleep(1)
            postarEvento.hide()
            principal.show()

        except ValueError:
            postarEvento.texto_erro.setText('Insira somente números na quantidade de ingressos.')
        except sqlite3.Error as erro:
            print('Erro ao inserir dados:', erro)
    
    else:
        postarEvento.texto_erro.setText('preencha os campos para salvar!')    
#-=-=--=-=-=-=-=-=-=-=-=-=

def abrirprincipal():
    perfilAdm.hide() or perfilCliente.hide()
    principal.show()

def selecionado(selecionado):
    for i in selecionado.indexes():
        print('Local de célula selecionada Linha: {0}, Coluna: {1}'.format(i.row(), i.column()))
        global eventoAtual
        eventoAtual = i.row() + 1

def detalhes():
    global eventoAtual
    id = eventoAtual
    try:
        nome = cursor.execute(f"SELECT nome FROM eventos WHERE ID = {id}").fetchall()
        tipo = cursor.execute(f"SELECT tipo FROM eventos WHERE ID = {id}").fetchall()
        data = cursor.execute(f"SELECT data FROM eventos WHERE ID = {id}").fetchall()
        hora = cursor.execute(f"SELECT hora FROM eventos WHERE ID = {id}").fetchall()
        local = cursor.execute(f"SELECT local FROM eventos WHERE ID = {id}").fetchall()
        contato = cursor.execute(f"SELECT contato FROM eventos WHERE ID = {id}").fetchall()

        if (tipo[0][0] == 'Evento de Dança'):
            detalhes_eventos.imagem.setPixmap(QtGui.QPixmap('./imgs/dance.png'))
        elif (tipo[0][0] == 'Peça Teatral'):
            detalhes_eventos.imagem.setPixmap(QtGui.QPixmap('./imgs/peca.png'))
        elif (tipo[0][0] == 'Evento Musical'):
            detalhes_eventos.imagem.setPixmap(QtGui.QPixmap('./imgs/musical.png'))

        detalhes_eventos.nome.setText(f'{nome[0][0]}')
        detalhes_eventos.tipo.setText(f'{tipo[0][0]}')
        detalhes_eventos.data.setText(f'{data[0][0]}')
        detalhes_eventos.hora.setText(f'{hora[0][0]}')
        detalhes_eventos.local.setText(f'{local[0][0]}')
        detalhes_eventos.contato.setText(f'Email para contato: {contato[0][0]}')

        time.sleep(1)
        principal.hide()
        detalhes_eventos.show()

    except sqlite3.OperationalError:
        principal.erro.setText('Selecione uma célula.')

def geraQrcode():
    global qtd
    imagens = []
    x = 0
    while x < qtd:
        imagens.append(x)
        x += 1

    i = len(imagens)
    for i in imagens:
        meu_qrcode = qrcode.make([i])
        meu_qrcode.save(f"./qrcodes/qrcode_ingresso{i}.png")

def finalizar():
    global admAtual, clienteAtual, eventoAtual,qtd
    if admAtual == '':
        usuario = clienteAtual
    elif clienteAtual == '':
        usuario = admAtual
    id = eventoAtual
    qtd = detalhes_eventos.ingressos.text()
    senha = detalhes_eventos.confirmacao.text()

    if (senha != '') and (qtd != '') and (senha == usuario):
            try:
                qtd = int(qtd)
                x = cursor.execute(f"SELECT comprado FROM eventos WHERE ID = {id}").fetchall()
                qtd_comprada = x[0][0]
                qtd_comprada += qtd 

                y = cursor.execute(f"SELECT qtdIngr FROM eventos WHERE ID = {id}").fetchall()
                qtd_disp = y[0][0]
                qtd_disp -= qtd_comprada

                cursor.execute(f"UPDATE eventos SET comprado = {qtd_comprada} WHERE ID = {id}")
                cursor.execute(f"UPDATE eventos SET qtdIngr = {qtd_disp} WHERE ID = {id}")
                banco.commit()

                time.sleep(1)
                detalhes_eventos.hide()
                principal.show()                
                #-=-=-=-=-=-=-=-=-=-=-=-=-=
                detalhes_eventos.ingressos.setText('')
                detalhes_eventos.confirmacao.setText('')
                #-=-=-=-=-=-=-=-=-=-=-=-=-=
                geraQrcode()

            except ValueError:
                detalhes_eventos.erro.setText('Insira somente números na quantidade de ingressos.')
            except sqlite3.Error as erro:
                print(erro)
                detalhes_eventos.erro.setText('Houve algum problema.')

    else:
        detalhes_eventos.erro.setText('Campos vazios ou usuario incorreto')

def sair():
    banco.close()
    perfilAdm.close() 
    perfilCliente.close()

# para botões de voltar adm.
def voltar_loginAdm():
    loginAdm.hide()
    inicio.show()
    loginAdm.userloginAdm.setText('')
    loginAdm.senhaloginAdm.setText('')
    loginAdm.texto_erro.setText('')

def voltar_cadastroAdm():
    cadastroAdm.hide()
    loginAdm.show()
    cadastroAdm.erro.setText('')
    cadastroAdm.usuarioAdm.setText('')
    cadastroAdm.emailAdm.setText('')
    cadastroAdm.telefoneAdm.setText('')
    cadastroAdm.senhaAdm.setText('')
    cadastroAdm.confirmasenhaAdm.setText('')

def voltar_perfilAdm():
    perfilAdm.hide()
    loginAdm.show()

def voltar_postEvento():
    postarEvento.hide()
    perfilAdm.show()
    postarEvento.nomeEvento.setText('')
    postarEvento.localEvento.setText('')
    postarEvento.qtd_Ingressos.setText('')

def voltar_dadosAdm():
    dadosAdm.hide()
    perfilAdm.show()

# para botões de voltar cliente.
def voltar_loginCliente():
    loginCliente.hide()
    inicio.show()
    loginCliente.userloginCliente.setText('')
    loginCliente.senhaloginCliente.setText('')
    loginCliente.texto_erro.setText('')

def voltar_cadastroCliente():
    cadastroCliente.hide()
    loginCliente.show()
    cadastroCliente.erro2.setText('')
    cadastroCliente.usuarioCliente.setText('')
    cadastroCliente.emailCliente.setText('')
    cadastroCliente.telefoneCliente.setText('')
    cadastroCliente.senhaCliente.setText('')
    cadastroCliente.confirmasenhaCliente.setText('')

def voltar_perfilCliente(): 
    perfilCliente.hide()
    loginCliente.show()

def voltar_dadosCliente():
    dadosCliente.hide()
    perfilCliente.show()

# -=-=-=-=
def voltar_principal():
    principal.hide()
    if admAtual == '':
        perfilCliente.show()
    elif clienteAtual == '':
        perfilAdm.show()

def voltar_detalhes():
    detalhes_eventos.hide()
    principal.show()
    detalhes_eventos.nome.setText('')
    detalhes_eventos.tipo.setText('')
    detalhes_eventos.data.setText('')
    detalhes_eventos.hora.setText('')
    detalhes_eventos.local.setText('')
    detalhes_eventos.contato.setText('')
    detalhes_eventos.ingressos.setText('')
    detalhes_eventos.confirmacao.setText('')

# botões da tela de início:
inicio.bt_vender.clicked.connect(abrirloginAdm)
inicio.bt_comprar.clicked.connect(abrirloginCliente)

# >>>> BUTTON CLICKED ADM <<<<
# TELA DE LOGIN:
loginAdm.bt_loginAdm.clicked.connect(entrarAdm) 
loginAdm.bt_cadastrarAdm.clicked.connect(abrirCadastroAdm)
loginAdm.bt_voltarloginAdm.clicked.connect(voltar_loginAdm)

# TELA DE CADASTRO:
cadastroAdm.bt_salvarloginAdm.clicked.connect(salvar_dadosAdm) 
cadastroAdm.bt_voltarcadastroAdm.clicked.connect(voltar_cadastroAdm)

# TELA DE PERFIL:
perfilAdm.bt_sairAdm.clicked.connect(sair)
perfilAdm.bt_voltarperfilAdm.clicked.connect(voltar_perfilAdm) 
perfilAdm.bt_dadosAdm.clicked.connect(abrirdadosAdm)
perfilAdm.bt_postarevento.clicked.connect(abrirPostarEvento)
perfilAdm.bt_navegarAdm.clicked.connect(abrirprincipal)


# TELA DE DADOS
dadosAdm.bt_deleteAdm.clicked.connect(deleteAdm)
dadosAdm.bt_voltardadosAdm.clicked.connect(voltar_dadosAdm)

# TELA DE POST DE EVENTOS:
postarEvento.bt_confereEvento.clicked.connect(confereEvento)
postarEvento.bt_postarEvento.clicked.connect(salvaEvento) 
postarEvento.bt_voltar.clicked.connect(voltar_postEvento)

# >>>> BUTTON CLICKED CLIENTE <<<<
# TELA DE LOGIN:
loginCliente.bt_loginCliente.clicked.connect(entrarCliente) 
loginCliente.bt_cadastrarCliente.clicked.connect(abrirCadastroCliente)
loginCliente.bt_voltarloginCliente.clicked.connect(voltar_loginCliente)

# TELA DE CADASTRO:
cadastroCliente.bt_salvarloginCliente.clicked.connect(salvar_dadosCliente)
cadastroCliente.bt_voltarCliente.clicked.connect(voltar_cadastroCliente)

# TELA DE PERFIL:
perfilCliente.bt_eventos.clicked.connect(abrirprincipal)
perfilCliente.bt_dadosCliente.clicked.connect(abrirdadosCliente)
perfilCliente.bt_sairCliente.clicked.connect(sair)
perfilCliente.bt_voltarperfilCliente.clicked.connect(voltar_perfilCliente)

# TELA DE DADOS
dadosCliente.bt_deleteCliente.clicked.connect(deleteCliente)
dadosCliente.bt_voltardados.clicked.connect(voltar_dadosCliente)

# >>>> BUTTON CLICKED PRINCIPAL
principal.bt_voltarPrincipal.clicked.connect(voltar_principal)
principal.bt_detalhes.clicked.connect(detalhes)
#########
principal.relatorio.selectionModel().selectionChanged.connect(selecionado)

# >>>> BUTTON CLICKED DETALHES
detalhes_eventos.bt_finalizar.clicked.connect(finalizar)
detalhes_eventos.bt_voltardetalhe.clicked.connect(voltar_detalhes)


atualizaLista()
inicio.show()
app.exec()