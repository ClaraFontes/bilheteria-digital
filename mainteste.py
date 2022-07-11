from PyQt6 import uic, QtWidgets
import sqlite3
import time

######################################################################################
app = QtWidgets.QApplication([])
tela = 'Tela atual: Inicio'
# importando as telas.
inicio = uic.loadUi('./telas/tela_inicio.ui')
loginAdm = uic.loadUi('./telas/tela_loginAdm.ui')
loginCliente = uic.loadUi('./telas/tela_loginCliente.ui')
cadastroAdm = uic.loadUi('./telas/tela_cadastroAdm.ui')
cadastroCliente = uic.loadUi('./telas/tela_cadastroCliente.ui')
perfilAdm = uic.loadUi('./telas/tela_perfilAdm.ui')
perfilCliente = uic.loadUi('./telas/tela_perfilCliente.ui')
postarEvento = uic.loadUi('./telas/tela_postEvento.ui')
######################################################################################

# 1 banco, 3 tabelas (adm; cliente; eventos.)
banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS adm (usuario TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, telefone TEXT UNIQUE NOT NULL, senha TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS cliente (usuario TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, telefone TEXT UNIQUE NOT NULL, cpf TEXT UNIQUE NOT NULL, senha TEXT NOT NULL)")
#cursor.execute("CREATE TABLE IF NOT EXISTS eventos (xxx)")   

def esperarAdm():
    cadastroAdm.usuarioAdm.setText('')
    cadastroAdm.emailAdm.setText('')
    cadastroAdm.telefoneAdm.setText('')
    cadastroAdm.senhaAdm.setText('')
    cadastroAdm.confirmasenhaAdm.setText('')
    time.sleep(1)
    cadastroAdm.hide()
    perfilAdm.show() 

def salvar_dadosAdm():
    usuario = cadastroAdm.usuarioAdm.text()
    email = cadastroAdm.emailAdm.text()
    telefone = cadastroAdm.telefoneAdm.text() 
    senha = cadastroAdm.senhaAdm.text()
    confirmacao = cadastroAdm.confirmasenhaAdm.text()

    if (senha != '') and (usuario != '') and (email != '') and (telefone != '') and (senha == confirmacao):
        try:
            cursor.execute("INSERT INTO adm (usuario, email, telefone, senha) VALUES (?,?,?,?)", (usuario, email, telefone, senha))         
            banco.commit()
            esperarAdm()
            
        except sqlite3.Error as erro:
            print('Erro ao inserir dados:', erro)
            cadastroAdm.erro.setText(f'{erro} já está em uso.')

    else: 
        cadastroAdm.erro.setText('Campos vazios ou confirmação de senha inválida.')

def salvar_dadosACliente():
    usuario = cadastroCliente.usuarioCliente.text()
    email = cadastroCliente.emailCliente.text()
    telefone = cadastroCliente.telefoneCliente.text()
    cpf = cadastroCliente.cpfCliente.text()
    senha = cadastroCliente.senhaCliente.text()
    confirmacao = cadastroCliente.confirmasenhaCliente.text()

    if (senha != '') and (usuario != '') and (email != '') and (telefone != '') and (cpf != '') and (senha == confirmacao):
        try:
            cursor.execute("INSERT INTO cliente (usuario, email, telefone, senha) VALUES (?,?,?,?)", (usuario, email, telefone, cpf, senha))         
            banco.commit()
            esperarAdm()
            
        except sqlite3.Error as erro:
            print('Erro ao inserir dados:', erro)
            cadastroCliente.erro.setText(f'{erro} já está em uso.')

    else: 
        cadastroCliente.erro.setText('Campos vazios ou confirmação de senha inválida.')

def abrirloginAdm():
    inicio.hide()
    loginAdm.show()
    global tela
    tela = 'Tela atual: Login do Adm'
    print(tela)

def abrirloginCliente():
    inicio.hide()
    loginCliente.show()
    global tela
    tela = 'Tela atual: Login do Cliente'
    print(tela)

def abrirCadastroAdm():
    loginAdm.hide()
    cadastroAdm.show()
    global tela
    tela = 'Tela atual: Cadastro do Adm'
    print(tela)

def abrirCadastroCliente():
    loginCliente.hide()
    cadastroCliente.show()
    global tela
    tela = 'Tela atual: Cadastro do Cliente'
    print(tela)

def abrirperfilAdm(): # SERÁ APAGADA QUANDO O CADASTRO E LOGIN ESTIVER OK
    loginAdm.hide() or cadastroAdm.hide()
    perfilAdm.show()
    global tela
    tela = 'Tela atual: Perfil do Adm'
    print(tela)

def abrirperfilCliente():
    loginCliente.hide() or cadastroCliente.hide()
    perfilCliente.show()
    global tela
    tela = 'Tela atual: Perfil do Cliente'
    print(tela)

def abrirPostarEvento():
    perfilAdm.hide()
    postarEvento.show()
    global tela
    tela = 'Tela atual: Postando Evento'
    print(tela)

def sair():
    banco.close()
    perfilAdm.close() 
    perfilCliente.close()

# botões de voltar adm.
def voltar_loginAdm():
    loginAdm.hide()
    inicio.show()
    global tela
    tela = 'Tela atual: Voltou à tela de início'
    print(tela)

def voltar_cadastroAdm():
    cadastroAdm.hide()
    loginAdm.show()
    global tela
    tela = 'Tela atual: Voltou ao login do Adm'
    print(tela)

def voltar_perfilAdm():
    perfilAdm.hide()
    loginAdm.show()
    global tela
    tela = 'Tela atual: Voltou ao login do Adm'
    print(tela)


# botões de voltar cliente.
def voltar_loginCliente():
    loginCliente.hide()
    inicio.show()
    global tela
    tela = 'Tela atual: Voltou à tela de início'
    print(tela)

def voltar_cadastroCliente():
    cadastroCliente.hide()
    loginCliente.show()
    global tela
    tela = 'Tela atual: Voltou ao login do Cliente'
    print(tela)

def voltar_perfilCliente(): # deve voltar para a tela dos eventos, mas de início volta para o login.
    perfilCliente.hide()
    loginCliente.show()
    global tela
    tela = 'Tela atual: Voltou ao login do Cliente'
    print(tela)


# botões da tela de início:
inicio.bt_vender.clicked.connect(abrirloginAdm)
inicio.bt_comprar.clicked.connect(abrirloginCliente)

# >> BUTTON CLICKED ADM
# TELA DE LOGIN:
loginAdm.bt_loginAdm.clicked.connect(abrirperfilAdm)
loginAdm.bt_cadastrarAdm.clicked.connect(abrirCadastroAdm)
loginAdm.bt_voltarloginAdm.clicked.connect(voltar_loginAdm)

# TELA DE CADASTRO:
cadastroAdm.bt_salvarloginAdm.clicked.connect(salvar_dadosAdm) # <<<<<<<<<<<
cadastroAdm.bt_voltarcadastroAdm.clicked.connect(voltar_cadastroAdm)

# TELA DE PERFIL:
perfilAdm.bt_sairAdm.clicked.connect(sair)
perfilAdm.bt_voltarperfilAdm.clicked.connect(voltar_perfilAdm)

# >> BUTTON CLICKED CLIENTE
# TELA DE LOGIN:
loginCliente.bt_loginCliente.clicked.connect(abrirperfilCliente)
loginCliente.bt_cadastrarCliente.clicked.connect(abrirCadastroCliente)
loginCliente.bt_voltarloginCliente.clicked.connect(voltar_loginCliente)

# TELA DE CADASTRO:
cadastroCliente.bt_salvarloginCliente.clicked.connect(salvar_dadosACliente) # <<<<<<<<<<<
cadastroCliente.bt_voltarCliente.clicked.connect(voltar_cadastroCliente)

# TELA DE PERFIL:
perfilCliente.bt_sairCliente.clicked.connect(sair)
perfilCliente.bt_voltarperfilCliente.clicked.connect(voltar_perfilCliente)


print(tela)
inicio.show()
app.exec()