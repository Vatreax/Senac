import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *


from views.login import Login_MainWindow


app = QApplication(sys.argv)
window = Login_MainWindow()
window.show()
sys.exit(app.exec_())