import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()


        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(patette)
        # 设置文本居中对齐
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        label2.setAlignment(Qt.AlignCenter)
        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/base.jpg"))



        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)


        label2.linkHovered.connect(self.linkHovered)


        self.setLayout(vbox)
        self.setWindowTitle('label控件演示')

    #当鼠标划过标签2时调用
    def linkHovered(self):
        print("当鼠标划过标签2时调用,触发事件")

    # 当鼠标单击标签4时调用
    def linkClicked(self):
        print("当鼠标单击标签4时调用,触发事件")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    # 显示主窗口
    main.show()
    # 进入程序的主循环
    sys.exit(app.exec_())
