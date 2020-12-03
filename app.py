import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("Connected")
    mbox.setStandardButtons(QMessageBox.Ok)
            
    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(700,400)
    w.setWindowTitle('Masterboard')
    
    label = QLabel(w)
    label.setText("Masterboard app")
    label.move(1,1)
    label.show()

    btn = QPushButton(w)
    btn.setText('Connect')
    btn.move(1,15)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())