from ui import Ui_MainWindow
import cv2
from functions import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtWidgets
import sys

class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Loading UI
        self.setupUi(self)
        # Button clicking
        self.input_button.clicked.connect(self.input_image)
        self.bw_button.clicked.connect(lambda : cvt_bw(self))
        self.gray_button.clicked.connect(lambda : cvt_gray(self))
        self.negative_button.clicked.connect(lambda : negative(self))
        self.gamma_button.clicked.connect(lambda : gamma(self))
        self.mean_button.clicked.connect(lambda : mean(self))
        self.median_button.clicked.connect(lambda : median(self))
        self.gaussian_button.clicked.connect(lambda : gaussian(self))
        self.laplacian_button.clicked.connect(lambda : edge_lap(self))
        self.bilateral_button.clicked.connect(lambda : bilateral(self))

        self.show()
        

    def input_image(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileName(None, 'Open a file', '','All Files (*.*)')
            self.image = cv2.imread(path[0])
            self.image = cv2.cvtColor(self.image.copy(), cv2.COLOR_BGR2RGB)
            self.gray_img = cv2.cvtColor(self.image.copy(), cv2.COLOR_BGR2GRAY)
        except:
            image_message = QtWidgets.QMessageBox()
            image_message.warning(self, "Choosing image", "Please choose an image", QtWidgets.QMessageBox.Ok)
        return None


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    ui.setWindowTitle("Image Processing Toolkit")
    ui.setWindowIcon(QtGui.QIcon("icon.png"))
    sys.exit(app.exec_())
