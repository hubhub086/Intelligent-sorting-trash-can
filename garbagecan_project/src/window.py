from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from Ui_test import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qimage2ndarray
import cv2

from thread import cameraThread, garbage
from plot import drawplot, fig2data
CAMERA = 1
DATA_PLOT = 0


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('智能垃圾分类')
        self.input = QLabel(self)
        self.input.resize(400, 100)
        self.setObjectName('win')  # 设置窗口名，相当于CSS中的ID
        self.setStyleSheet('#win{border-image:url(../data/background.jpg);}')  # 设置图片的相对路径
        # 播放器
        self.playerlist = QMediaPlaylist()
        self.playerlist.addMedia(QMediaContent(
            QUrl.fromLocalFile("/home/caosongliang/VSCodeProject/python/garbagecan_project/data/garbage_sorting.mp4")))
        self.playerlist.setPlaybackMode(3)  # loop play mode
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playerlist)
        self.player.setVideoOutput(self.wgt_player)
        # self.player.setMedia(QMediaContent(
        #     QUrl.fromLocalFile("/home/caosongliang/VSCodeProject/python/garbagecan_project/data/garbage_sorting.mp4")))
        self.player.play()
        self.player.pause()
        # 按钮
        self.data_camera_flag = CAMERA
        self.btn_select.clicked.connect(self.open)
        self.btn_play.clicked.connect(self.playPlay)
        self.btn_pause.clicked.connect(self.playPause)
        self.data_analyze.clicked.connect(self.dataflagchange)
        self.showcarmera.clicked.connect(self.carmeraflagchange)
        # 进度条
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.sld_duration.sliderMoved.connect(self.updatePosition)
        # 表格
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止用户编辑表格
        self.tableWidget.verticalHeader().setVisible(False)  # 隐藏列标题
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().resizeSection(0, 10)
        self.tableWidget.horizontalHeader().resizeSection(1, 80)
        self.tableWidget.horizontalHeader().resizeSection(2, 10)
        self.tableWidget.horizontalHeader().resizeSection(3, 80)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(['序号', '垃圾信息', '数量', '投放状态'])
        font = self.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)
        # self.tabelDisplay()

        self.initUI()

    def initUI(self):
        # 创建线程
        self.thread = QThread()

        self.camera = cameraThread()
        # 连接信号
        self.camera.items.connect(self.tabelDisplay)
        self.camera.img.connect(self.showimageordata)
        self.camera.moveToThread(self.thread)

        # 开始线程
        self.thread.started.connect(self.camera.run)
        self.thread.start()

    def dataflagchange(self):
        print("flag_data")
        self.data_camera_flag = DATA_PLOT
        self.showplot(garbage)

    def carmeraflagchange(self):
        print("flag_camera")
        self.data_camera_flag = CAMERA

    def showimageordata(self, img):
        if self.data_camera_flag == CAMERA:
            img = cv2.resize(img, (420, 280))
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            showframe = qimage2ndarray.array2qimage(frame)
            # showframe = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.carmeralabel.setPixmap(QPixmap.fromImage(showframe))
            self.carmeralabel.show()
        '''else:
            figure = drawplot(garbage)
            img = fig2data(figure)
            img = cv2.resize(img, (420, 280))
            frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            showframe = qimage2ndarray.array2qimage(frame)
            self.carmeralabel.setPixmap(QPixmap.fromImage(showframe))
            self.carmeralabel.show()
        '''

    # 修改表格信息 & show plot
    def tabelDisplay(self, items):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for i in range(len(items)):
            item = items[i]
            row = self.tableWidget.rowCount()
            # row = i
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(row, j, item)

        if self.data_camera_flag == DATA_PLOT:
            self.showplot(items)

    def showplot(self, items):
        figure = drawplot(items)
        img = fig2data(figure)
        img = cv2.resize(img, (420, 280))
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        showframe = qimage2ndarray.array2qimage(frame)
        self.carmeralabel.setPixmap(QPixmap.fromImage(showframe))
        self.carmeralabel.show()

    """video player"""
    def open(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()

    def playPause(self):
        self.player.pause()

    def playPlay(self):
        self.player.play()

    # 视频总时长获取
    def getDuration(self, d):
        """d是获取到的视频总时长（ms）"""
        self.sld_duration.setRange(0, d)
        self.sld_duration.setEnabled(True)
        self.displayTime(d)

    # 视频实时位置获取
    def getPosition(self, p):
        self.sld_duration.setValue(p)
        self.displayTime(self.sld_duration.maximum() - p)
        if self.sld_duration.maximum() - p == 0:
            print("finish video")
            # self.player.play()

    # 显示剩余时间
    def displayTime(self, ms):
        minutes = int(ms / 60000)
        seconds = int((ms - minutes * 60000) / 1000)
        self.lab_duration.setText('{}:{}'.format(minutes, seconds))

    # 用进度条更新视频位置
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(self.sld_duration.maximum() - v)
