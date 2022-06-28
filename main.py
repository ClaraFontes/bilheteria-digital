from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic, QtWidgets 

def func_teste():
    print('botao funcionando')

app = QtWidgets.QApplication([])
inicio = uic.loadUi('./telas/tela_inicio.ui')
inicio.bt_vender.clicked.connect(func_teste)


inicio.show()
app.exec()


