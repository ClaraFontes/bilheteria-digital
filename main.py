#from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic, QtWidgets

app = QtWidgets.QApplication([])
# importando as telas.
inicio = uic.loadUi('./telas/tela_inicio.ui')
loginAdm = uic.loadUi('./telas/tela_loginAdm.ui')
loginCliente = uic.loadUi('./telas/tela_loginCliente.ui')
tela = 'Tela atual: Inicio'
tela2 = ''

def func_abrirloginAdm():
    inicio.hide()
    loginAdm.show()
    global tela , tela2
    tela = 'Tela atual: Login do Adm'
    print(tela)

def func_abrirloginCliente():
    inicio.hide()
    loginCliente.show()
    global tela , tela2
    tela = 'Tela atual: Login do Cliente'
    print(tela)

inicio.bt_vender.clicked.connect(func_abrirloginAdm) # abre login adm.
inicio.bt_comprar.clicked.connect(func_abrirloginCliente) # abre login cliente.

print(tela)

inicio.show()
app.exec()