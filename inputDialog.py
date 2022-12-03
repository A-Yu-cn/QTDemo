from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication, QFrame, QColorDialog, QFontDialog, QVBoxLayout, QSizePolicy,
                             QLabel, QTextEdit, QAction, QFileDialog, QMainWindow)
import sys


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 输入文字信息显示
        self.btn_mes = QPushButton('Dialog message', self)
        self.btn_mes.move(20, 20)
        self.btn_mes.clicked.connect(self.showDialogMes)

        self.le = QLineEdit(self)
        self.le.move(200, 22)
        # 颜色选择
        col = QColor(0, 0, 0)

        self.btn_col = QPushButton('Dialog color', self)
        self.btn_col.move(20, 120)
        self.btn_col.clicked.connect(self.showDialogCol)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(230, 120, 100, 100)
        # 字体选择
        self.btn_font = QPushButton('Dialog font', self)
        self.btn_font.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)
        self.btn_font.move(20, 220)
        self.btn_font.clicked.connect(self.showDialogFont)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(150, 220)
        # 文件选择
        self.textEdit = QTextEdit(self)
        self.textEdit.move(150, 320)
        self.statusBar()
        openFile = QAction(QIcon('web.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialogFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialogMes(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

    def showDialogCol(self):

        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                                   % col.name())

    def showDialogFont(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
            self.lbl.adjustSize()

    def showDialogFile(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())






