import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("button")

def onClick_Button():
## 包含标题栏
    print('1')
## x,y为整个窗口左上角
    print("widget.x() = %d" % widget.x()) #窗口横坐标
    print("widget.y() = %d" % widget.y()) #窗口纵坐标
## 此时高度不含标题栏
    print("widget.widht() = %d" % widget.width())
    print("widget.height() = %d" % widget.height())

## 不包含标题栏
    print('2')
## x,y 为工作区左上角
    print("widget.geometry().x() = %d" % widget.geometry().x())#工作区横坐标
    print("widget.geometry().y() = %d" % widget.geometry().y())#工作区纵坐标
## 此时高度不含标题栏
    print("widget.geometry().widht() = %d" % widget.geometry().width())
    print("widget.geometry().height() = %d" % widget.geometry().height())

##
    print('2')
    print("widget.framegeometry().x() = %d" % widget.frameGeometry().x())
    print("widget.framegeometry().y() = %d" % widget.frameGeometry().y())
    print("widget.framegeometry().widht() = %d" % widget.frameGeometry().width())#窗口宽度
    print("widget.framegeometry().height() = %d" % widget.frameGeometry().height())#窗口高度，包含标题栏

btn.clicked.connect(onClick_Button)


btn.move(24,52)
# 设置工作区的尺寸，不包含标题栏，并不是整个窗口的尺寸
widget.resize(300,240)
widget.move(250,200)
widget.setWindowTitle('Screen Geometry')
widget.show()
sys.exit(app.exec_())

