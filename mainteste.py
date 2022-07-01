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

# validando.
telainicio = True
telaloginAdm = False
telaloginCliente = False
telacadastroAdm = False
telacadastroCliente = False
telaperfilAdm = False
telapostarEvento = False

tela = 'Tela atual: Inicio'


def func_abrirloginAdm():
    inicio.hide()
    loginAdm.show()
    global tela, telaloginAdm, telainicio
    tela = 'Tela atual: Login do Adm'
    telainicio = False
    telaloginAdm = True
    print(telaloginAdm)
    print(tela)


def func_abrirloginCliente():
    inicio.hide()
    loginCliente.show()
    global tela, telaloginCliente
    telaloginCliente = True
    tela = 'Tela atual: Login do Cliente'
    print(tela)


def func_abrirCadastroAdm():
    loginAdm.hide()
    cadastroAdm.show()
    global tela, telacadastroAdm
    telacadastroAdm = True
    tela = 'Tela atual: Cadastro do Adm'
    print(tela)


def func_abrirCadastroCliente():
    loginCliente.hide()
    cadastroCliente.show()
    global tela, telacadastroCliente
    telacadastroCliente = True
    tela = 'Tela atual: Cadastro do Cliente'
    print(tela)


'''
def func_abrirPerfilAdm():
    loginAdm.hide()
    perfilAdm.show()
    global tela
    tela = 'Tela atual: Perfil do Adm'
    print(tela)

def func_abrirPostarEvento():
    perfilAdm.hide()
    postarEvento.show()
    global tela
    tela = 'Tela atual: Postando Evento'
    print(tela)

print(telaloginAdm) # False antes da função ser executada
func_abrirloginAdm()
print(telaloginAdm) # True depois da função ser executada
'''
if inicio.bt_vender.clicked(True):
    func_abrirloginAdm()
elif inicio.bt_comprar.clicked(True):
    func_abrirloginCliente()

# inicio.bt_vender.clicked.connect(func_abrirloginAdm) # abre login adm.
# inicio.bt_comprar.clicked.connect(func_abrirloginCliente) # abre login cliente.

# arrumar um jeito do programa reconhecer que a função de tornar a tela de início falsa foi executada quando o botão foi clicado.
if telainicio != True:
    if telaloginAdm != False:
        print(f'telaloginAdm = {telaloginAdm}')
    elif telaloginCliente != False:
        print(f'telaloginCliente = {telaloginCliente}')

print(tela)
inicio.show()
app.exec()
