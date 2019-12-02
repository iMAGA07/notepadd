import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap


class fileeki(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        uic.loadUi('uineweki.ui', self)

        self.path = None

        self.pushButton.clicked.connect(self.opening_run)
        self.pushButton_2.clicked.connect(self.saving_run)
        self.pushButton_3.clicked.connect(self.saveac)
        self.pushButton_5.clicked.connect(self.new_run)

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def opening_run(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text files (*.txt)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.plainTextEdit.setPlainText(text)

    def saving_run(self):
        if self.path is None:

            return self.saveac()

        self._save_to_path(self.path)

    def saveac(self):
        path = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")

        if not path:

            return

        self._save_to_path(self.path)

    def _save_to_path(self, path):
        text = self.plainTextEdit.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path

    def new_run(self):
        self.plainTextEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = fileeki()
    ex.show()
    sys.exit(app.exec())