import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton

class QuitApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(300,120)

        self.setWindowTitle('退出应用程序')

        # 添加button
        self.button1 = QPushButton('退出应用程序')
        # 绑定信号与槽
        self.button1.clicked.connect(self.onClick_Button)

        # 创建水平布局
        layout = QHBoxLayout()
        # 将button组件加到水平布局中
        layout.addWidget(self.button1)
        # 创建一个根QWidget实例,所有的控件都要放到QWidget实例上
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        # 使mainFrame充满整个窗口？？？
        self.setCentralWidget(mainFrame)

        ## 控件实例放在layout实例上，layout实例放在QWidget实例上，QWidget实例最终充满整个窗口


    # 按钮单击事件的方法,相当于槽
    def  onClick_Button(self):
        # 通过sender获得button发出的信号
        sender = self.sender()
        # 输出button的文本
        print(sender.text() + '按钮被按下')
        # 得到QApplication实例
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())