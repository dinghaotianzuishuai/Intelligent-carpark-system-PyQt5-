import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUi()
    def initUi(self):
        self.setWindowTitle('buttonDemo')

        layout = QVBoxLayout()
        self.button1 = QPushButton('1st button')
        self.button1.setCheckable(True)
        self.button1.toggle()
        #self.button1.clicked.connect(lambda :self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)


        layout.addWidget(self.button1)
        # 在文本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.resize(400,300)

        self.button3 = QPushButton('不可用按钮')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)


        self.setLayout(layout)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮一已经被选中')
        else:
            print('按钮一未被选中')
    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    # 显示主窗口
    main.show()
    # 进入程序的主循环
    sys.exit(app.exec_())

