## 显示控件提示信息
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class TooltipForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 静态方法设置字体
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('Today is Monday')
        self.setGeometry(500,300,200,300)
        self.setWindowTitle('设置控件提示消息')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())
