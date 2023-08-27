import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets

def cvt_bw(self):
    try:
        img = self.gray_img.copy()
        bw_image = img.copy()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] < 128:
                bw_image[i, j] = 0
            else:
                bw_image[i, j] = 255

    plt.subplot(1, 2, 1)
    plt.imshow(self.image)
    plt.subplot(1, 2, 2)
    plt.imshow(bw_image, cmap='gray')
    plt.show()   


def cvt_gray(self):
    try:
        plt.subplot(1, 2, 1)
        plt.imshow(self.image)
        plt.subplot(1, 2, 2)
        plt.imshow(self.gray_img, cmap='gray')
        plt.show()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None

def negative(self):
    try:
        negative_img = 1 - self.gray_img
        plt.subplot(1, 2, 1)
        plt.imshow(self.gray_img, cmap='gray')
        plt.subplot(1, 2, 2)
        plt.imshow(negative_img, cmap='gray')
        plt.show()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None

def mean(self):
    try:
        n = int(self.kernel_size_lineEdit.text())
    except:
        kernel_size_message = QtWidgets.QMessageBox()
        kernel_size_message.warning(self, "Kernel size error", "You did't specified the kernel size properly", QtWidgets.QMessageBox.Ok)
        return None
    try:
        kernel = np.ones((n, n), np.float32) / n**2   # mean kernel
        mean_img = cv2.filter2D(self.image.copy(), -1, kernel)
        plt.subplot(1, 2, 1)
        plt.imshow(self.image)
        plt.subplot(1, 2, 2)
        plt.imshow(mean_img)
        plt.show()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None

def median(self):
    try:
        n = int(self.kernel_size_lineEdit.text())
    except:
        kernel_size_message = QtWidgets.QMessageBox()
        kernel_size_message.warning(self, "Kernel size error", "You did't specified the kernel size properly", QtWidgets.QMessageBox.Ok)
        return None
    try:
        median_img = cv2.medianBlur(self.image.copy(), n)
        plt.subplot(1, 2, 1)
        plt.imshow(self.image)
        plt.subplot(1, 2, 2)
        plt.imshow(median_img)
        plt.show()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None


def edge_lap(self):
    try:
        image = self.gray_img.copy()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None

    kernel = np.array([[1, 1, 1],
                       [1, -8, 1],
                       [1, 1, 1]])
    
    lap_img = cv2.filter2D(image, -1, kernel)
    plt.subplot(1, 2, 1)
    plt.imshow(self.image)
    plt.subplot(1, 2, 2)
    plt.imshow(lap_img)
    plt.show()
    

def gamma(self):  # gamma > 1 => darker, gamma < 1 => brighter
    try:
        gamma_value = float(self.gamma_lineEdit.text())
    except:
        gamma_value_message = QtWidgets.QMessageBox()
        gamma_value_message.warning(self, "gamma value error", "You did't specified the gamma value properly", QtWidgets.QMessageBox.Ok)
        return None
    try:
        c_value = float(self.c_gamma_lineEdit.text())
    except:
        c_gamma_value_message = QtWidgets.QMessageBox()
        c_gamma_value_message.warning(self, "\"c\" value error", "You did't specified the \"c\" value properly", QtWidgets.QMessageBox.Ok)
        return None
    try:
        img_norm = cv2.normalize(self.image.copy().astype("float"), None, 0, 1, norm_type=cv2.NORM_MINMAX)
        img_gamma = c_value * img_norm ** gamma_value
        plt.subplot(1, 2, 1)
        plt.imshow(self.image)
        plt.subplot(1, 2, 2)
        plt.imshow(img_gamma)
        plt.show()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None
    

def gaussian(self):
    try:
        img = self.image.copy()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)
        return None
    
    try:
        n = int(self.kernel_size_lineEdit.text())
    except:
        kernel_size_message = QtWidgets.QMessageBox()
        kernel_size_message.warning(self, "Kernel size error", "You did't specified the kernel size properly", QtWidgets.QMessageBox.Ok)
        return None
    
    try:
        sigma = int(self.sigma_lineEdit.text())
    except:
        sigma_message = QtWidgets.QMessageBox()
        sigma_message.warning(self, "sigma error", "You did't specified the sigma properly", QtWidgets.QMessageBox.Ok)
        return None
    
    img_gauss = cv2.GaussianBlur(img, (n, n), sigma)
    plt.subplot(1, 2, 1)
    plt.imshow(self.image)
    plt.subplot(1, 2, 2)
    plt.imshow(img_gauss)
    plt.show()


def bilateral(self):
    try:
        n = int(self.kernel_size_lineEdit.text())
    except:
        kernel_size_message = QtWidgets.QMessageBox()
        kernel_size_message.warning(self, "Kernel size error", "You did't specified the kernel size properly", QtWidgets.QMessageBox.Ok)
        return None
    try:
        img_bilateral = cv2.bilateralFilter(self.image.copy(), n, 75, 75)
        plt.subplot(1, 2, 1)
        plt.imshow(self.image)
        plt.subplot(1, 2, 2)
        plt.imshow(img_bilateral)
        plt.show()
    except:
        image_message = QtWidgets.QMessageBox()
        image_message.warning(self, "Somthing is wrong", "You probably didn't choose an image", QtWidgets.QMessageBox.Ok)