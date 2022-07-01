from PyQt6 import uic, QtWidgets

app = QtWidgets.QApplication([])
# importando as telas.
inicio = uic.loadUi('./telas/tela_inicio.ui')
loginAdm = uic.loadUi('./telas/tela_loginAdm.ui')
loginCliente = uic.loadUi('./telas/tela_loginCliente.ui')
cadastroAdm = uic.loadUi('./telas/tela_cadastroAdm.ui')
cadastroCliente = uic.loadUi('./telas/tela_cadastroCliente.ui')
perfilAdm = uic.loadUi('./telas/tela_perfilAdm.ui')
postarEvento = uic.loadUi('./telas/tela_postEvento.ui')

tela = 'Tela atual: Inicio'

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

def abrirperfilAdm():
    loginAdm.hide() or cadastroAdm.hide()
    perfilAdm.show()
    global tela
    tela = 'Tela atual: Perfil do Adm'
    print(tela)

def abrirPostarEvento():
    perfilAdm.hide()
    postarEvento.show()
    global tela
    tela = 'Tela atual: Postando Evento'
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

#ADM
# botões da tela de início:
inicio.bt_vender.clicked.connect(abrirloginAdm)
inicio.bt_comprar.clicked.connect(abrirloginCliente)

# botões da tela de Login do Adm:
loginAdm.bt_loginAdm.clicked.connect(abrirperfilAdm)
loginAdm.bt_cadastrarAdm.clicked.connect(abrirCadastroAdm)

# botões da tela de Cadastro do Adm:
cadastroAdm.bt_salvarloginAdm.clicked.connect(abrirperfilAdm)
cadastroAdm.bt_voltarAdm.clicked.connect(voltar_cadastroAdm)

#botões da tela de Perfil do Adm:
perfilAdm.bt_voltarperfilAdm.clicked.connect(voltar_perfilAdm)

# botões da tela de Login do Cliente:
#loginCliente.bt_loginCliente.clicked.connect(abrirperfilCliente) >> tela ainda não criada.
loginCliente.bt_cadastrarCliente.clicked.connect(abrirCadastroCliente)

print(tela)
inicio.show()
app.exec()
