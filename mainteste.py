from PyQt6 import uic, QtWidgets
import sqlite3
import time

######################################################################################
app = QtWidgets.QApplication([])
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
            cadastroAdm.erro.setText('')
            cadastroAdm.usuarioAdm.setText('')
            cadastroAdm.emailAdm.setText('')
            cadastroAdm.telefoneAdm.setText('')
            cadastroAdm.senhaAdm.setText('')
            cadastroAdm.confirmasenhaAdm.setText('')
            
        except sqlite3.Error as erro:
            print('Erro ao inserir dados:', erro)
            cadastroAdm.erro.setText(f'{erro} já está em uso.')
        except ValueError:
            cadastroAdm.erro.setText('Telefone inválido.')

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
            telefone = int(telefone)
            cpf = int(cpf)
            cursor.execute("INSERT INTO cliente (usuario, email, telefone, cpf, senha) VALUES (?,?,?,?,?)", (usuario, email, telefone, cpf, senha))         
            banco.commit()
            esperarCliente()
            cadastroCliente.erro2.setText('')
            cadastroCliente.usuarioCliente.setText('')
            cadastroCliente.emailCliente.setText('')
            cadastroCliente.telefoneCliente.setText('')
            cadastroCliente.senhaCliente.setText('')
            cadastroCliente.confirmasenhaCliente.setText('')

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
                loginAdm.userloginAdm.setText('')
                loginAdm.senhaloginAdm.setText('')
                loginAdm.texto_erro.setText('')
            else: 
                loginAdm.texto_erro.setText('Campo de senha vazio ou senha inválida.')

        except IndexError:
            loginAdm.texto_erro.setText('Usuário inválido ou senha incorreta.')
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
                loginCliente.userloginCliente.setText('')
                loginCliente.senhaloginCliente.setText('')
                loginCliente.texto_erro.setText('')
            else:
                loginCliente.texto_erro.setText('Campo de senha vazio ou senha inválida.')

        except IndexError:
            loginCliente.texto_erro.setText('Usuário inválido ou senha incorreta.')
    else:
        loginCliente.texto_erro.setText('Preencha o campo de usuário.')

def abrirloginAdm():
    inicio.hide()
    loginAdm.show()

def abrirloginCliente():
    inicio.hide()
    loginCliente.show()

def abrirCadastroAdm():
    loginAdm.hide()
    cadastroAdm.show()

def abrirCadastroCliente():
    loginCliente.hide()
    cadastroCliente.show()

def abrirPostarEvento():
    perfilAdm.hide()
    postarEvento.show()

def sair():
    banco.close()
    perfilAdm.close() 
    perfilCliente.close()

# botões de voltar adm.
def voltar_loginAdm():
    loginAdm.hide()
    inicio.show()

def voltar_cadastroAdm():
    cadastroAdm.hide()
    loginAdm.show()

def voltar_perfilAdm():
    perfilAdm.hide()
    loginAdm.show()

# botões de voltar cliente.
def voltar_loginCliente():
    loginCliente.hide()
    inicio.show()

def voltar_cadastroCliente():
    cadastroCliente.hide()
    loginCliente.show()

def voltar_perfilCliente(): # deve voltar para a tela dos eventos, mas de início volta para o login.
    perfilCliente.hide()
    loginCliente.show()


# botões da tela de início:
inicio.bt_vender.clicked.connect(abrirloginAdm)
inicio.bt_comprar.clicked.connect(abrirloginCliente)

# >> BUTTON CLICKED ADM
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

# >> BUTTON CLICKED CLIENTE
# TELA DE LOGIN:
loginCliente.bt_loginCliente.clicked.connect(entrarCliente) 
loginCliente.bt_cadastrarCliente.clicked.connect(abrirCadastroCliente)
loginCliente.bt_voltarloginCliente.clicked.connect(voltar_loginCliente)

# TELA DE CADASTRO:
cadastroCliente.bt_salvarloginCliente.clicked.connect(salvar_dadosACliente)
cadastroCliente.bt_voltarCliente.clicked.connect(voltar_cadastroCliente)

# TELA DE PERFIL:
perfilCliente.bt_sairCliente.clicked.connect(sair)
perfilCliente.bt_voltarperfilCliente.clicked.connect(voltar_perfilCliente)

inicio.show()
app.exec()