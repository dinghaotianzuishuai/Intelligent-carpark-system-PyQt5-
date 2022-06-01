import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class CarParkMainWindow(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题
        self.setWindowTitle('Carpark system')
        # 设置窗口尺寸
        self.resize(1500, 800)
        #self.setGeometry(1500, 800, 200, 300)
        # 获得状态栏
        self.status = self.statusBar()
        # 在状态栏上显示消息
        self.status.showMessage('Number of Available slots:')

        # 设置控件提示信息
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('Carpark system')

        # 添加button
        button1 = QPushButton('button1')
        button2 = QPushButton('button2')

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)





# 防止其他脚本调用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CarParkMainWindow()
    # 显示主窗口
    main.show()
    # 进入程序的主循环
    sys.exit(app.exec_())