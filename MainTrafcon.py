import sys

import cv2
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.uic import loadUi


class TrafCon(QMainWindow):
    def __init__(self):
        super(TrafCon, self).__init__()
        loadUi('MainTrafcon.ui', self)
        self.video_size = QSize(600, 400)
        self.image = None
        self.processedImage = None
        self.startButton.clicked.connect(self.startButtonEvent)
        self.stopButton.clicked.connect(self.stop_webcam)
        self.openDatafile.clicked.connect(self.openDatafileCfg)
        self.openConfigfile.clicked.connect(self.openConfigfileCfg)
        self.openWeightfile.clicked.connect(self.openWeightfileCfg)
        self.openStaticfile.clicked.connect(self.selectStaticfileCfg)
        self.openVideooutput.clicked.connect(self.selectVideoOutputDir)
        self.openCaptureimg.clicked.connect(self.selectCaptureImgDir)

    @pyqtSlot()
    def openDatafileCfg(self):
        fname, filter = QFileDialog.getOpenFileName(
            self, 'Open File', '', 'Data File (*.data)')
        self.lineEdit_DataFile.setText(fname)

    @pyqtSlot()
    def openConfigfileCfg(self):
        fname, filter = QFileDialog.getOpenFileName(
            self, 'Open File', '', "Config File (*.cfg)")
        self.lineEdit_ConfigFile.setText(fname)

    @pyqtSlot()
    def openWeightfileCfg(self):
        fname, filter = QFileDialog.getOpenFileName(
            self, 'Open File', '', "Weights File (*.weights)")
        self.lineEdit_WeightFile.setText(fname)

    @pyqtSlot()
    def selectStaticfileCfg(self):
        selectDir = str(QFileDialog.getExistingDirectory(
            self, caption='Select Directory'))
        self.lineEdit_StaticFile.setText(selectDir)

    @pyqtSlot()
    def selectVideoOutputDir(self):
        selectDir = str(QFileDialog.getExistingDirectory(
            self, caption='Select Directory'))
        self.lineEdit_VideoOut.setText(selectDir)

    @pyqtSlot()
    def selectCaptureImgDir(self):
        selectDir = str(QFileDialog.getExistingDirectory(
            self, caption='Select Directory'))
        self.lineEdit_Capture.setText(selectDir)

    def startButtonEvent(self):
        radioStatus = self.vidFileRadButton.isChecked()
        # print(radioStatus)
        if (radioStatus == True):
            print('siap putar video')
            videoCamPath = self.lineEdit_Addr.text()
            print(videoCamPath)
            self.start_webcam(videoCamPath)
        else:
            print('RTSP belum siap')
            message = QMessageBox.warning(self, "Warning", "RTSP Mode is not ready",
                                          QMessageBox.Ok)

    def start_webcam(self, videopath):
        # 0 =default #1,2,3 =Extra Webcam
        # print(videopath)
        if videopath.endswith('.mp4'):
            self.capture = cv2.VideoCapture('{}'.format(videopath))
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,
                             self.video_size.height())

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(5)
        else:
            print('Check format or location video file')
            message = QMessageBox.warning(self, "Warning", "Check format or location video file",
                                          QMessageBox.Ok)

    def update_frame(self):
        ret, frame = self.capture.read()
        frame = cv2.cvtColor(frame, 1)
        self.image = cv2.flip(frame, 1)
        self.processedImage = self.image
        self.displayImage(1)

    def stop_webcam(self):
        self.timer.stop()

    def displayImage(self, window=1):
        qformat = QImage.Format_Indexed8

        if len(self.processedImage.shape) == 3:  # rows[0],cols[1],channels[2]
            if (self.processedImage.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.processedImage, self.processedImage.shape[1], self.processedImage.shape[0],
                     self.processedImage.strides[0], qformat)
        # BGR > RGB
        img = img.rgbSwapped()
        if window == 1:
            self.cameraLabel.setPixmap(QPixmap.fromImage(img))
            self.cameraLabel.setScaledContents(True)
        if window == 2:
            self.processedLabel.setPixmap(QPixmap.fromImage(img))
            self.processedLabel.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrafCon()
    window.setWindowTitle('TrafCon')
    window.show()
    sys.exit(app.exec_())
