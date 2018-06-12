import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGridLayout, QApplication,QPushButton)
from PyQt5 import QtWidgets,QtGui,QtCore
import play

class ProcessRunnable(QtCore.QRunnable):
    def __init__(self, target, args):
        QtCore.QRunnable.__init__(self)
        self.t = target
        self.args = args

    def run(self):
        self.t(*self.args)

    def start(self):
        QtCore.QThreadPool.globalInstance().start(self)



def changeImg(imagelabel,path):
	imagelabel.setPixmap(QtGui.QPixmap(""))
	pixmap = QtGui.QPixmap(path)
	scaredPixmap = pixmap.scaled(800, 400, aspectRatioMode=QtCore.Qt.KeepAspectRatio)
	imagelabel.setPixmap(scaredPixmap)

def changeText(label,text):
	label.setText(str(text)+'s')
class Example(QWidget):
    signal1 = QtCore.pyqtSignal(int)
    wJump=play.wechatJump()
    def __init__(self):
        super().__init__()
        # signal1=QtCore.pyqtSignal()
        self.initUI()

    def click(self,checked):
    	# play.main(self.wLineEdit.text(),self.hLineEdit.text(),self.signal1)
    	self.p = ProcessRunnable(target=self.wJump.main, args=(self.wLineEdit.text(),self.hLineEdit.text(),self.signal1))
    	self.p.start()
    	# self.p.finishe()

    def stop(self,checked):
    	self.wJump.runSig.emit()
    	print('stopppppp')

    def signalCall1(self,press_time):
        print("signal1 emit")
        self.p0 = ProcessRunnable(target=changeImg, args=(self.imageLabel,'../phone.png'))
        self.p1 = ProcessRunnable(target=changeImg, args=(self.imageLabel2,'last.png'))
        self.p2 = ProcessRunnable(target=changeText,args=(self.timeLineLabel,press_time))
        self.p0.start()
        self.p1.start()
        self.p2.start()
    def initUI(self):

        layout = QGridLayout()

        wLabel = QLabel("phone width")
        self.wLineEdit = QLineEdit("1080")
        self.wLineEdit.setFixedWidth(100)

        hLabel = QLabel("phone height")
        self.hLineEdit = QLineEdit("1920")
        self.hLineEdit.setFixedWidth(100)

        timeLabel = QLabel("press_time")
        self.timeLineLabel = QLabel("700s")
        self.imageLabel = QLabel()

        button = QPushButton("Play", self)
        stopbt=QPushButton("Stop",self)
        button.clicked.connect(self.click)
        stopbt.clicked.connect(self.stop)
        self.imageLabel2 = QLabel()


        self.signal1.connect(self.signalCall1)


        leftlable=QLabel('<---------origin')
        rightlable=QLabel('last----------->')


        layout.setSpacing(10)
        layout.addWidget(wLabel,0,0)
        layout.addWidget(self.wLineEdit,0,1)
        layout.addWidget(hLabel,0,3)
        layout.addWidget(self.hLineEdit,0,4)


        layout.addWidget(self.imageLabel,1,0,8,2)
        layout.addWidget(leftlable,3,2)
        layout.addWidget(rightlable,5,2)
        layout.addWidget(self.imageLabel2,1,3,8,4)

        layout.addWidget(button,8,2)
        layout.addWidget(stopbt,9,2)
        layout.addWidget(timeLabel,10,0)
        layout.addWidget(self.timeLineLabel,10,1)

        layout.setColumnStretch(1, 10)

        self.setLayout(layout)

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Jump')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())