import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtGui #inserir imagens

app = QApplication(sys.argv)

janela = QWidget()

janela.show()
sys.exit(app.exec())
