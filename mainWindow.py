import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMessageBox, QMenu, QTextEdit


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 主界面
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        #  状态栏
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('Ready')
        # 多个子菜单栏
        exitAct = QAction(QIcon('web.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        menubar = self.menuBar()

        impMenu = QMenu('Import', self)
        impMenu.setStatusTip('Import Menu') # 无效
        impAct = QAction('Import mail', self)
        impAct.setStatusTip('Import Action')
        impMenu.addAction(impAct)

        fileMenu = menubar.addMenu('File')
        fileMenu.setStatusTip('File Menu')
        newAct = QAction('New', self)
        newAct.setStatusTip('New Action')
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        # 勾选菜单
        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        # 工具栏
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('mainWindow')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def closeEvent(self, event):
        """
            单击关闭按钮调用的方法
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def toggleMenu(self, state):
        """
            切换状态栏显示情况
        """
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):

        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
