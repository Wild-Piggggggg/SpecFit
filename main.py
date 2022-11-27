"""此程序用于调用主要操作"""

import csv  # 导入处理csv文件的库
import os  # 导入操作系统库

import numpy as np  # 导入数据处理库
from PyQt5 import QtWidgets, QtCore, QtGui  # 导入控件库
from PyQt5.QtChart import *
from PyQt5.QtGui import QPainter, QCursor, QColor, QBrush, QFont, QPen
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QToolTip, QGraphicsBlurEffect

from intergal_cal import Intergal  # 导入自建类
from painting import Painting
from window import Ui_MainWindow


# import shutil

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """初始化MainWindow"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.origin_path = os.getcwd()  # 获取当前文件夹的路径且不可修改

        self.setFixedSize(1292, 920)
        self.mutiple_parameters()  # 设置好可替换参数
        self.specification()

        self.Theme_change_light()  # 改变界面主题
        self.creat_empty_chart_compare()  # 必须先创建再修改，先创建三角函数法数据可视化的Qchart
        self.creat_empty_chart_accumulate()  # 再创建时程分析的数值可视化的Qchart

        self.agreen_ouput = False
        self.agreen_ouput_1 = False

        self.tabWidget.setCurrentIndex(0)
        self.Chinese_name = ["目标谱", "文件路径", "拟合参数", "时程", "步长", "持时", "随机数", "迭代数", "目标谱点数", "阻尼",
                             "时程分析文件", "文件路径", "设计地震动拟合", "时程分析", "开始拟合", "进行积分", "清除曲线", "导出数据"]

        self.English_name = ["target spectrum", "file path", "fitting parameters", "T_H", "step", "duration", "randit",
                             "iteration", "points", "damper",
                             "time history analysis file", "file path", "design ground motion simulation",
                             "time history analysis", "fit", "intergrate", "clear", "output"]


        # 此处编写业务逻辑代码

        # 按照功能顺序，一个一个写，牢记一个函数实现一个小功能

    def mutiple_parameters(self):
        """由于ICASE的不同
        会导致TRISE、TIVL、A0、ALFA0、BETA0、IPOW这六个参数的不同
        故专门用一个函数来设置新的参量
        """
        self.change_para_list = [self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_14.text(),
                                 self.lineEdit_12.text(), self.lineEdit_13.text(), self.lineEdit_8.text()]

    def change_para_timely(self):
        for n, i in enumerate(
                [self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_14.text(), self.lineEdit_12.text(),
                 self.lineEdit_13.text(), self.lineEdit_8.text()]):
            if i != '' and i != '0':
                self.change_para_list[n] = i

    def ICASE_1(self):
        # ICASE为1时，TRISE、TLVL为0，A0、ALFA0、BETA0、IPOW都不参与计算默认为0
        self.change_para_timely()  # 每次切换按钮都要重新确定一遍self.change_para_list的值

        self.lineEdit_3.setText("0")
        self.lineEdit_3.setEnabled(False)

        self.lineEdit_4.setText("0")
        self.lineEdit_4.setEnabled(False)

        self.lineEdit_14.setText("")
        self.lineEdit_14.setEnabled(False)

        self.lineEdit_13.setText("")
        self.lineEdit_13.setEnabled(False)

        self.lineEdit_12.setText("")
        self.lineEdit_12.setEnabled(False)

        self.lineEdit_8.setText("")
        self.lineEdit_8.setEnabled(False)

    def ICASE_2(self):

        self.change_para_timely()  # 每次切换按钮都要重新确定一遍self.change_para_list的值

        self.lineEdit_3.setText(self.change_para_list[0])
        self.lineEdit_4.setText(self.change_para_list[1])

        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)

        self.lineEdit_14.setText("")
        self.lineEdit_14.setEnabled(False)

        self.lineEdit_13.setText("")
        self.lineEdit_13.setEnabled(False)

        self.lineEdit_12.setText("")
        self.lineEdit_12.setEnabled(False)

        self.lineEdit_8.setText("")
        self.lineEdit_8.setEnabled(False)

    def ICASE_3(self):

        self.change_para_timely()  # 每次切换按钮都要重新确定一遍self.change_para_list的值

        self.lineEdit_14.setText(self.change_para_list[2])
        self.lineEdit_12.setText(self.change_para_list[3])
        self.lineEdit_13.setText(self.change_para_list[4])

        self.lineEdit_14.setEnabled(True)
        self.lineEdit_12.setEnabled(True)
        self.lineEdit_13.setEnabled(True)

        self.lineEdit_3.setText("0")
        self.lineEdit_3.setEnabled(False)

        self.lineEdit_4.setText("0")
        self.lineEdit_4.setEnabled(False)

        self.lineEdit_8.setText("")
        self.lineEdit_8.setEnabled(False)

    def ICASE_4(self):

        self.change_para_timely()  # 每次切换按钮都要重新确定一遍self.change_para_list的值
        # self.radioButton_4.setChecked(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_8.setEnabled(True)
        self.lineEdit_12.setEnabled(True)

        self.lineEdit_3.setText(self.change_para_list[0])
        self.lineEdit_4.setText(self.change_para_list[1])
        self.lineEdit_8.setText(self.change_para_list[5])
        self.lineEdit_12.setText(self.change_para_list[3])

        self.lineEdit_13.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_14.setEnabled(False)

    def specification(self):
        """设置默认状态的按钮"""
        self.radioButton_2.setChecked(True)
        self.ICASE_2()

    def Theme_change_light(self):
        """修改为明亮主题"""
        self.line.setStyleSheet("background-color:#FFFFFF")
        self.label_18.setPixmap(QtGui.QPixmap("logo_white.ico"))
        self.setStyleSheet("#MainWindow{border-image:url(back_blue.png)}")
        self.textBrowser_2.setStyleSheet("background-color:#FFFFFF;border-width:0;border-style:outset")
        self.textBrowser.setStyleSheet("background-color:#FFFFFF;border-width:0;border-style:outset")

    def Theme_change_dark(self):
        """修改为灰暗主题"""
        self.line.setStyleSheet("background-color:#0d0821")
        self.label_18.setPixmap(QtGui.QPixmap("logo_black.ico"))
        self.setStyleSheet("#MainWindow{border-image:url(back_black.png)}")
        self.textBrowser_2.setStyleSheet("background-color:#0d0821;border-width:0;border-style:outset")   #  预期颜色是#0d0821
        self.textBrowser.setStyleSheet("background-color:#0d0821;border-width:0;border-style:outset")

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.8)
        self.listView.setGraphicsEffect(op)
        self.listView.setAutoFillBackground(True)

        op_2 = QtWidgets.QGraphicsOpacityEffect()
        op_2.setOpacity(0.8)
        self.listView_2.setGraphicsEffect(op_2)
        self.listView_2.setAutoFillBackground(True)

        op_4 = QtWidgets.QGraphicsOpacityEffect()
        op_4.setOpacity(0.8)
        self.listView_4.setGraphicsEffect(op_4)
        self.listView_4.setAutoFillBackground(True)

        op_6 = QtWidgets.QGraphicsOpacityEffect()
        op_6.setOpacity(0.8)
        self.listView_6.setGraphicsEffect(op_6)
        self.listView_6.setAutoFillBackground(True)

        op_7 = QtWidgets.QGraphicsOpacityEffect()
        op_7.setOpacity(0.8)
        self.listView_7.setGraphicsEffect(op_7)
        self.listView_7.setAutoFillBackground(True)

        op_8 = QtWidgets.QGraphicsOpacityEffect()
        op_8.setOpacity(0.8)
        self.listView_8.setGraphicsEffect(op_8)
        self.listView_8.setAutoFillBackground(True)

        op_tab = QtWidgets.QGraphicsOpacityEffect()
        op_tab.setOpacity(0.8)
        self.tabWidget.setGraphicsEffect(op_tab)
        self.tabWidget.setAutoFillBackground(True)



    def language_change_EN(self):
        """修改文字为英文"""
        self.groupBox_3.setTitle(self.English_name[0])
        self.label_17.setText(self.English_name[1])
        self.groupBox_4.setTitle(self.English_name[2])
        self.label_2.setText(self.English_name[3])
        self.label_3.setText(self.English_name[4])
        self.label_12.setText(self.English_name[5])
        self.label_13.setText(self.English_name[6])
        self.label_14.setText(self.English_name[7])
        self.label_15.setText(self.English_name[8])
        self.label_16.setText(self.English_name[9])
        self.groupBox_5.setTitle(self.English_name[10])
        self.label_23.setText(self.English_name[11])
        self.tabWidget.setTabText(0, self.English_name[12])
        self.tabWidget.setTabText(1, self.English_name[13])

        self.pushButton.setText(self.English_name[14])
        self.pushButton_3.setText(self.English_name[15])
        self.pushButton_4.setText(self.English_name[16])
        self.pushButton_5.setText(self.English_name[16])
        self.pushButton_2.setText(self.English_name[17])
        self.pushButton_6.setText(self.English_name[17])

    def language_change_ZN(self):
        self.groupBox_3.setTitle(self.Chinese_name[0])
        self.label_17.setText(self.Chinese_name[1])
        self.groupBox_4.setTitle(self.Chinese_name[2])
        self.label_2.setText(self.Chinese_name[3])
        self.label_3.setText(self.Chinese_name[4])
        self.label_12.setText(self.Chinese_name[5])
        self.label_13.setText(self.Chinese_name[6])
        self.label_14.setText(self.Chinese_name[7])
        self.label_15.setText(self.Chinese_name[8])
        self.label_16.setText(self.Chinese_name[9])
        self.groupBox_5.setTitle(self.Chinese_name[10])
        self.label_23.setText(self.Chinese_name[11])
        self.tabWidget.setTabText(0, self.Chinese_name[12])
        self.tabWidget.setTabText(1, self.Chinese_name[13])

        self.pushButton.setText(self.Chinese_name[14])
        self.pushButton_3.setText(self.Chinese_name[15])
        self.pushButton_4.setText(self.Chinese_name[16])
        self.pushButton_5.setText(self.Chinese_name[16])
        self.pushButton_2.setText(self.Chinese_name[17])
        self.pushButton_6.setText(self.Chinese_name[17])



    def find_file(self):
        """查找目标谱文件路径
        目标谱是txt文件，第一列数据为目标谱频率，第二列为目标谱对应的加速度值
        """
        filename1, filetype1 = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                           "Files (*.xlsx *.txt *.dat)")  # 设置文件扩展名过滤,注意用双分号间隔
        # filename1 = 'C:\\Users\\Red Fox\\Desktop\\目标谱.txt'  # 测试语句
        self.lineEdit_15.clear()  # 清除当前文本框内的路径
        self.lineEdit_15.setText(filename1)  # 重新设置新的文件路径

    def find_file_1(self):
        """查找目标时程分析文件路径
               文件是txt文件，第一列数据加速度值,时间间隔默认0.05
               """
        filename2, filetype2 = QFileDialog.getOpenFileName(self, "选取文件", "./",
                                                           "Files (*.xlsx *.txt *.dat)")  # 设置文件扩展名过滤,注意用双分号间隔
        # filename1 = 'C:\\Users\\Red Fox\\Desktop\\目标谱.txt'  # 测试语句
        self.lineEdit_16.clear()  # 清除当前文本框内的路径
        self.lineEdit_16.setText(filename2)  # 重新设置新的文件路径

    def get_information(self):
        """获取当前所有填入参数的值"""
        for button in [self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4]:
            # 获取按钮的值
            if button.isChecked():
                self.ICASE_value = button.text()
                break
        """获取其他参数的值"""
        self.TRISE_value = self.lineEdit_3.text()
        self.TLVL_value = self.lineEdit_4.text()
        self.HOLDING_time_value = self.lineEdit_9.text()
        self.A0_value = self.lineEdit_14.text()
        self.ALFA0_value = self.lineEdit_12.text()
        self.BETA0_value = self.lineEdit_13.text()
        self.IPOW_value = self.lineEdit_8.text()
        self.STEP_value = self.lineEdit_2.text()
        self.GMAX_value = self.lineEdit_5.text()
        self.RAND_value = self.lineEdit_6.text()
        self.ITERATION_value = self.lineEdit_10.text()
        self.TIME_value = self.lineEdit.text()
        self.FREQUENCY_value = self.lineEdit_7.text()
        self.DAMP_value = self.lineEdit_11.text()
        self.temp_information = [self.ICASE_value, self.TRISE_value, self.TLVL_value, self.HOLDING_time_value,
                                 self.A0_value, self.ALFA0_value, self.BETA0_value, self.IPOW_value, self.STEP_value,
                                 self.GMAX_value, self.RAND_value, self.ITERATION_value, self.TIME_value,
                                 self.FREQUENCY_value, self.DAMP_value]  # 打包成一个列表，方便后续处理

        if self.ICASE_value == '1':
            self.temp_information = [self.ICASE_value, self.TRISE_value, self.TLVL_value, self.HOLDING_time_value,
                                     '0', '0', '0', '0', self.STEP_value, self.GMAX_value, self.RAND_value,
                                     self.ITERATION_value,
                                     self.TIME_value, self.FREQUENCY_value, self.DAMP_value]  # 打包成一个列表，方便后续处理
        elif self.ICASE_value == '2':
            self.temp_information = [self.ICASE_value, self.TRISE_value, self.TLVL_value, self.HOLDING_time_value,
                                     '0', '0', '0', '0', self.STEP_value,
                                     self.GMAX_value, self.RAND_value, self.ITERATION_value, self.TIME_value,
                                     self.FREQUENCY_value, self.DAMP_value]  # 打包成一个列表，方便后续处理
        elif self.ICASE_value == '3':
            self.temp_information = [self.ICASE_value, self.TRISE_value, self.TLVL_value, self.HOLDING_time_value,
                                     self.A0_value, self.ALFA0_value, self.BETA0_value, '0', self.STEP_value,
                                     self.GMAX_value, self.RAND_value, self.ITERATION_value, self.TIME_value,
                                     self.FREQUENCY_value, self.DAMP_value]  # 打包成一个列表，方便后续处理
        else:
            self.temp_information = [self.ICASE_value, self.TRISE_value, self.TLVL_value, self.HOLDING_time_value,
                                     '0', self.ALFA0_value, '0', self.IPOW_value, self.STEP_value,
                                     self.GMAX_value, self.RAND_value, self.ITERATION_value, self.TIME_value,
                                     self.FREQUENCY_value, self.DAMP_value]  # 打包成一个列表，方便后续处理

    def calculate(self):  # 开始计算
        """对拼接后的input.dat调用exe进行处理，在目标文件夹生成输出文件"""
        self.get_information()  # 运行时获取当前所有参数信息

        if "" in self.temp_information:  # 判断是否存在参数错误
            QMessageBox.warning(None, '错误', '存在未确定的参数', QMessageBox.Ok)
            return

        for item in self.temp_information:
            try:
                ret = float(item)
            except ValueError:
                QMessageBox.warning(None, '错误', '存在格式错误的输入参数', QMessageBox.Ok)
                return

        if self.lineEdit_15.text():  # 判断文件路径是否填入对话框
            msg_reply = QMessageBox.question(self, "询问", "请问是否去掉目标文件首行数据后再计算？", QMessageBox.Yes | QMessageBox.No)
            """选择是否去掉首行数据"""
            if msg_reply == QMessageBox.Yes:
                head_cal = False
            else:
                head_cal = True

            state = self.generate_input_file(self.lineEdit_15.text(), head_cal)  # 读取input文件，带上head_cal参数
            if state == False:
                return False

        else:
            QMessageBox.warning(None, '错误', '存在未确定的目标谱路径', QMessageBox.Ok)  # 警告文件路径不存在
            return

        os.chdir('running')  # 调用同目录下子文件夹里的exe文件，避免了文件转移
        SIMQuake = 'SIMQKE_interface_v1.exe'  # 获取exe文件名称
        os.system(SIMQuake)  # 执行exe文件

        path_pre = self.lineEdit_15.text()  # 获取目标反应谱文件名

        now_path = os.path.dirname(__file__)  # 获得当前文件夹路径
        # print(now_path)
        path_fit = os.path.join(now_path, 'running\output_simqke.dat')  # 获取设计谱的数据，这里为什么相对路径会出错呢，先试试可行的绝对路径拼接
        # print(path_fit)
        try:
            self.change_chart_compare(self.chart, self.chart_0, path_pre, path_fit, head_cal)  # 根据生成的文件生成新的曲线，进行数据可视化
        except:
            return
        """各参数的意义，"""
        # self.chart是三角函数叠加法的数据可视化结果所在的chart
        # self.chart_0是反应谱与设计谱的差值（理解为脉动波）可视化结果所在的chart
        # path是exe跑出的output文件，即设计谱，只有最后几行是需要的数据
        # path1是选取的原反应谱文件路径

        os.chdir(self.origin_path)  # python程序回到上一级目录

        self.agreen_ouput = True
        self.agreen_ouput_1 = False

        # print('done')   “”“这部分为测试语句”“”
        # path = "./running/output_simqke.dat"
        # path1 = self.lineEdit_15.text()
        # self.creat_chart(path, path1)
        # self.remove_files('./', './running')

    # def remove_files(self, old_path, new_path):
    #     # 移动生成文件到指定文件夹
    #     filelist = ['generated_TH.dat', 'output_process.out', 'output_simqke.dat', 'simqke_input.DAT']
    #     for file in filelist:
    #         src = os.path.join(old_path, file)
    #         dst = os.path.join(new_path, file)
    #         shutil.move(src, dst)

    def generate_input_file(self, filename1, head_cal):
        """拼接生成input.dat文件"""
        with open(filename1)as file:
            if head_cal:  ## 根据head_cal的值确定是否需要首行数据
                contents = file.readlines()  # 读取目标谱的每一行数据
                # print(contents[0].split())
                if len(contents[0].split()) != 2:
                    if self.label_2.text()=='文件路径':
                        QMessageBox.warning(None, '警告', '所选文件数据格式不匹配，请重新选择', QMessageBox.Ok)
                    else:
                        QMessageBox.warning(None, 'warning', 'The data format of the selected file does not match. Please select a new one', QMessageBox.Ok)
                    return False
            else:
                head_content_useless_title = file.readline()  # 提前读取一行用不到的数据，一般是标题
                contents = file.readlines()  # 读取剩下的标题
                if len(contents[0].split()) != 2:
                    QMessageBox.warning(None, '警告', '所选文件数据格式不匹配，请重新选择', QMessageBox.Ok)
                    return False
        contents_length = len(contents)  # 获取数据量大小

        if contents_length != int(self.lineEdit_7.text()):
            # 自动匹配目标谱频率点数
            QMessageBox.information(None, '目标谱频率点数不匹配', f'已从{self.FREQUENCY_value}更正为{contents_length}', QMessageBox.Ok)
            self.lineEdit_7.setText(str(contents_length))  # 修改界面上的呈现数据，一般是程序完全跑完当前所在子函数后才会变化
            self.FREQUENCY_value = self.lineEdit_7.text()  # 获取新的频率点数
            self.temp_information[-2] = self.FREQUENCY_value  # 修改实时信息

        now_path_1 = os.path.dirname(__file__)  # 获取当前所在文件夹路径
        target_path = os.path.join(now_path_1, 'running\simqke_input.dat')  # 这里为什么相对路径会出错呢，先试试可行的绝对路径拼接

        with open(target_path, 'w')as target:
            """写入simqke_input.dat文件"""
            target.write('  '.join(self.temp_information))  # 把参数输入文件
            target.write('\n')
            for line in contents:
                target.write(line)

    def creat_empty_chart_compare(self):
        """先在大框框内绘制拟合功能部分空白图，即不加数据"""
        """这里就暂时不追求代码简洁性了，逻辑写清楚最重要"""
        self.chart = QChartView(self.listView_3)
        self.chart.setGeometry(QtCore.QRect(5, 5, 645, 545))  # 定位

        self.chart_0 = QChartView(self.listView_4)
        self.chart_0.setGeometry(QtCore.QRect(5, 5, 645, 235))  # 定位

        for number, chart in enumerate([self.chart, self.chart_0]):
            chart.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
            chart.raise_()
            chart._chart = QChart()  # 创建折线视图
            chart._chart.setBackgroundBrush(QBrush(QColor("#FFFFFF")))  # 改变图背景色
            chart._chart.setAcceptHoverEvents(
                True)  # 图形项默认无法接收悬停事件，可以使用QGraphicsItem的setAcceptHoverEvents()函数使图形项可以接收悬停事件。

            self.chart_draw_empty(chart)  # 创建空图

            chart._chart.createDefaultAxes()  # 创建默认的轴

            """这部分也可以单独拎出来一个函数"""
            if self.label_17.text()=='文件路径':
                chart._chart.axisX().setTitleText("频率/10^x")  # 设置轴标题
                chart._chart.axisX().setTitleFont(QFont("黑体", 8))  # 设置字体

                chart._chart.axisX().setTickCount(11)
                if number == 0:
                    chart._chart.axisY().setTitleText("加速度/g")  # 设置轴标题
                else:
                    chart._chart.axisY().setTitleText("残差/%")  # 设置轴标题
                chart._chart.axisY().setTitleFont(QFont("黑体", 8))  # 设置字体

            else:
                chart._chart.axisX().setTitleText("frequency/10^x")  # 设置轴标题
                chart._chart.axisX().setTitleFont(QFont("黑体", 8))  # 设置字体

                chart._chart.axisX().setTickCount(11)
                if number == 0:
                    chart._chart.axisY().setTitleText("accleration/g")  # 设置轴标题
                else:
                    chart._chart.axisY().setTitleText("residual/%")  # 设置轴标题
                chart._chart.axisY().setTitleFont(QFont("黑体", 8))  # 设置字体

            chart._chart.axisY().setLabelFormat("%.1f")  # 设置数据格式
            chart._chart.axisX().setTickCount(11)
            chart.setChart(chart._chart)

        # 以下为测试代码
        # self.chart.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # self.chart.raise_()
        # self.chart._chart = QChart()  # 创建折线视图
        # self.chart._chart.setBackgroundBrush(QBrush(QColor("#FFFFFF")))  # 改变图背景色
        # self.chart._chart.setAcceptHoverEvents(
        #     True)  # 图形项默认无法接收悬停事件，可以使用QGraphicsItem的setAcceptHoverEvents()函数使图形项可以接收悬停事件。
        #
        # self.chart_draw_empty(self.chart)
        #
        # self.chart._chart.createDefaultAxes()  # 创建默认的轴
        # self.chart._chart.axisX().setTitleText("频率/10^x")
        # self.chart._chart.axisX().setTitleFont(QFont("黑体", 10))
        # self.chart._chart.axisY().setTitleText("加速度/g")
        # self.chart._chart.axisY().setTitleFont(QFont("黑体", 10))
        # # chart._chart.axisY().setLabelFormat("%f")
        # self.chart.setChart(self.chart._chart)

    def chart_draw_empty(self, chart):
        """与含empty名称的函数一起使用，目的是为了先放一个空图"""
        chart._chart.removeAllSeries()  # 移除原有数据
        series = QLineSeries(chart._chart)  # 新建QLineSeries类，放入数据
        series.setName("empty")  # 命名为空图
        series.setPen(QPen(QColor(5, 5, 6), 0.9))  # 修改线条颜色为褐色，粗细为0.5
        x_empty = np.linspace(0, 20, 20)  # 空图的x数据，随意定制
        y_empty = np.zeros(len(x_empty))  # 空图的y数据，随意定制

        for i in range(len(x_empty)):
            series.append(x_empty[i], y_empty[i])  # 添加

        # series.setPointsVisible(True)  # 显示原点

        series.hovered.connect(self.onSeriesHoverd)  # 鼠标悬停连接事件
        chart._chart.addSeries(series)  # 添加折线到视图窗口
        return chart._chart

    def creat_empty_chart_accumulate(self):
        """再在另外三个框内画上空图，思路和前面的empty一致"""
        self.chart_1 = QChartView(self.listView_6)
        self.chart_2 = QChartView(self.listView_7)
        self.chart_3 = QChartView(self.listView_8)

        for number, small_chart in enumerate([self.chart_1, self.chart_2, self.chart_3]):
            """给三个积分图设置样式，目前这部分一致"""
            small_chart.setGeometry(QtCore.QRect(5, 5, 645, 255))
            small_chart.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
            small_chart.raise_()
            small_chart._chart = QChart()  # 创建折线视图
            small_chart._chart.setBackgroundBrush(QBrush(QColor("#FFFFFF")))  # 改变图背景色
            #  图形项默认无法接收悬停事件，可以使用QGraphicsItem的setAcceptHoverEvents()函数使图形项可以接收悬停事件。
            small_chart._chart.setAcceptHoverEvents(True)

            self.chart_draw_empty(small_chart)

            small_chart._chart.createDefaultAxes()  # 创建默认的轴
            small_chart._chart.axisX().setTitleText("时程 / s")
            small_chart._chart.axisX().setTitleFont(QFont("黑体", 8))
            small_chart._chart.axisX().setTickCount(11)
            if number == 0:
                small_chart._chart.axisY().setTitleText("加速度  g")
            elif number == 1:
                small_chart._chart.axisY().setTitleText("速度  m/s")
            else:
                small_chart._chart.axisY().setTitleText("位移  m")
            small_chart._chart.axisY().setTitleFont(QFont("黑体", 8))
            small_chart._chart.axisY().setLabelFormat("%.4f")
            small_chart.setChart(small_chart._chart)

    def change_chart_compare(self, chart, chart_0, path, path1, head_cal):
        """根据文件路径，绘制拟合图和差值图"""
        self.tabWidget.setCurrentIndex(0)  # 选项卡实时跳转至tab_1
        self.fre_list_pre, self.acc_list_pre, self.fre_list_fit, self.acc_list_fit = Painting().draw(path, path1, int(self.lineEdit_7.text()), head_cal)  # 得到原反应谱和设计谱的数据

        chart._chart.removeAllSeries()  # 移除原有数据
        chart_0._chart.removeAllSeries()  # 移除原有数据
        self.creat_series_fre_acc_pre(self.fre_list_pre, self.acc_list_pre, chart)  # 在QChart里加入反应谱
        self.creat_series_fre_acc_fit(self.fre_list_fit, self.acc_list_fit, chart)  # 在QChart里加入设计谱

        self.creat_series_fre_acc_diff(self.fre_list_fit,
                                       (self.acc_list_fit - self.acc_list_pre) / self.acc_list_pre * 100,
                                       chart_0)  # 在Qchart_0中加入差值谱

        for number, s_chart in enumerate([chart, chart_0]):
            """三个图的相同后处理"""
            s_chart._chart.createDefaultAxes()  # 创建默认的轴
            s_chart._chart.axisX().setTitleText("频率/10^x")
            s_chart._chart.axisX().setTitleFont(QFont("黑体", 8))
            if number == 0:
                s_chart._chart.axisY().setTitleText("加速度/g")
                s_chart._chart.axisY().setLabelFormat("%.2f")
            else:
                s_chart._chart.axisY().setTitleText("残差/%")
            s_chart._chart.axisY().setTitleFont(QFont("黑体", 8))
            s_chart.setChart(s_chart._chart)

        continue_msg_reply = QMessageBox.question(self, "询问", "请问是否对该目标谱生成的结果直接进行时程分析？", QMessageBox.Yes | QMessageBox.No)
        """判断是否去掉首行数据"""
        if continue_msg_reply == QMessageBox.Yes:
            self.continue_accumulate()
        else:
            pass

    def creat_series_fre_acc_pre(self, fre, acc, chart):
        """绘制反应谱"""
        series = QLineSeries(chart._chart)
        series.setName("目标反应谱")
        series.setPen(QPen(QColor(236, 114, 89), 2))
        fre = np.log(fre) / np.log(10)
        for i in range(len(fre)):
            series.append(fre[i], acc[i])
        # 鼠标悬停连接事件
        series.hovered.connect(self.onSeriesHoverd)
        chart._chart.addSeries(series)  # 添加折线到视图窗口
        return chart._chart

    def creat_series_fre_acc_fit(self, fre, acc, chart):
        """绘制设计谱"""
        series = QLineSeries(chart._chart)
        series.setName("设计反应谱")
        series.setPen(QPen(QColor(131, 131, 184), 2))
        fre = np.log(fre) / np.log(10)  # 取对数坐标轴
        for i in range(len(fre)):
            series.append(fre[i], acc[i])
        series.hovered.connect(self.onSeriesHoverd)
        chart._chart.addSeries(series)  # 添加折线到视图窗口
        return chart._chart

    ### 这里我觉得还是分开写清晰一点，毕竟就两个图，要是想进行一些精细化修改还是得分开

    def creat_series_fre_acc_diff(self, fre, acc_diff, chart_0):
        """绘制差值谱"""
        series = QScatterSeries(chart_0._chart)
        series.setName("目标谱与设计谱残差")
        series.setPen(QPen(QColor(131, 131, 184)))
        series.setMarkerSize(3)
        # series.setBorderColor(QColor("#FFFFFF"))
        fre = np.log(fre) / np.log(10)
        for i in range(len(fre)):
            series.append(fre[i], acc_diff[i])
        series.hovered.connect(self.onSeriesHoverd)
        chart_0._chart.addSeries(series)  # 添加折线到视图窗口
        return chart_0._chart

    def change_chart_accumulate(self, chart, t, para, datatype):
        """绘制时程分析的积分图"""
        self.tabWidget.setCurrentIndex(1)
        chart._chart.removeAllSeries()  # 移除原有数据
        series = QLineSeries(chart._chart)
        if datatype == 'acc':
            series.setName("加速度-时程")
        elif datatype == 'vel':
            series.setName("速度-时程")
        elif datatype == 'dis':
            series.setName("位移-时程")

        series.setPen(QPen(QColor(131, 131, 184), 2))
        for i in range(len(t)):
            series.append(t[i], para[i])
        series.hovered.connect(self.onSeriesHoverd)
        chart._chart.addSeries(series)  # 添加折线到视图窗口
        return chart._chart

    def accumulate(self):
        """获取在时程积分中的所有数据并绘图"""
        if self.lineEdit_16.text():  # 判断文件路径是否填入对话框
            path = self.lineEdit_16.text()
        else:
            QMessageBox.warning(None, '错误', '存在未确定的目标谱路径', QMessageBox.Ok)
            return
        msg_reply = QMessageBox.question(self, "询问", "请问是否去掉目标文件首行数据后再进行计算？", QMessageBox.Yes | QMessageBox.No)
        """判断是否去掉首行数据"""
        if msg_reply == QMessageBox.Yes:
            head_cal = False
        else:
            head_cal = True

        example = Intergal()
        self.state_2, self.ground_motion_parameter, self.t1, self.data, self.t2, self.vel, self.t3, self.dis = example.read_data(
            path, head_cal, 1)

        """这部分代码可以单独拎出来重写成一个函数"""
        if self.state_2 == False:
            QMessageBox.warning(None, '警告', '所选文件数据格式不匹配，请重新选择', QMessageBox.Ok)
            return
        self.change_chart_accumulate(self.chart_1, self.t1, self.data, 'acc')
        self.change_chart_accumulate(self.chart_2, self.t2, self.vel, 'vel')
        self.change_chart_accumulate(self.chart_3, self.t3, self.dis, 'dis')

        for number, chart in enumerate([self.chart_1, self.chart_2, self.chart_3]):
            chart._chart.createDefaultAxes()  # 创建默认的轴
            chart._chart.axisX().setTitleText("时程 / s")
            chart._chart.axisX().setTitleFont(QFont("黑体", 8))
            if number == 0:
                chart._chart.axisY().setTitleText("加速度 / g")
            elif number == 1:
                chart._chart.axisY().setTitleText("速度 / m/s")
            elif number == 2:
                chart._chart.axisY().setTitleText("位移 / m")

            chart._chart.axisY().setTitleFont(QFont("黑体", 8))
            chart._chart.axisY().setLabelFormat("%.2f")
            chart.setChart(chart._chart)
            """对，就是上面这部分"""
        self.agreen_ouput = False
        self.agreen_ouput_1 = True

    def continue_accumulate(self):
        """用于直接绘制设计谱生成的加速度谱积分"""
        now_path_1 = os.path.dirname(__file__)  # 获取当前所在文件夹路径
        TH_path = os.path.join(now_path_1, 'running\generated_TH.dat')  # 这里为什么相对路径会出错呢，先试试可行的绝对路径拼接
        example = Intergal()
        head_cal = False
        self.state_3, self.ground_motion_parameter, self.t1, self.data, self.t2, self.vel, self.t3, self.dis = example.read_data(
            TH_path, head_cal, 2)

        self.change_chart_accumulate(self.chart_1, self.t1, self.data, 'acc')
        self.change_chart_accumulate(self.chart_2, self.t2, self.vel, 'vel')
        self.change_chart_accumulate(self.chart_3, self.t3, self.dis, 'dis')

        for number, chart in enumerate([self.chart_1, self.chart_2, self.chart_3]):
            chart._chart.createDefaultAxes()  # 创建默认的轴
            chart._chart.axisX().setTitleText("时程 / s")
            chart._chart.axisX().setTitleFont(QFont("黑体", 8))
            if number == 0:
                chart._chart.axisY().setTitleText("加速度 / g")
            elif number == 1:
                chart._chart.axisY().setTitleText("速度 / m/s")
            elif number == 2:
                chart._chart.axisY().setTitleText("位移 / m")

            chart._chart.axisY().setTitleFont(QFont("黑体", 8))
            chart._chart.axisY().setLabelFormat("%.2f")
            chart.setChart(chart._chart)

    def clear(self):
        """移除拟合框的数据"""
        self.chart._chart.removeAllSeries()  # 移除第一个框原有数据
        self.chart_0._chart.removeAllSeries()  # 移除第二个框原有数据

    def clear_1(self):
        """移除积分框的数据"""
        self.chart_1._chart.removeAllSeries()  # 移除第三个框原有数据
        self.chart_2._chart.removeAllSeries()  # 移除第四个框原有数据
        self.chart_3._chart.removeAllSeries()  # 移除第五个框原有数据

    def output_data(self):
        """生成目标反应谱和设计反应谱的数据存储文件"""
        file_path, file_type = QFileDialog.getSaveFileName(self, "save file", "./projects/untitled_Fit",
                                                           "xlsx files (*.xlsx);;csv files (*.csv);;txt files(*.txt);;all files(*.*)")

        format_type = file_path.split('.')[-1]

        if file_path and self.agreen_ouput==True and self.agreen_ouput_1==False:
            """尝试导出图片失败,这部分的bug我才测试screen的截图限制了tab视图的切换"""
            #     # self.tabWidget.setCurrentIndex(0)
            #     picture_path = file_path.split('.')[0] + '_fit.jpg'
            #     picture_path_0 = file_path.split('.')[0] + '_diff.jpg'
            #
            #     screen = QtWidgets.QApplication.primaryScreen()
            #     pix = screen.grabWindow(self.chart.winId())
            #     pix_0 = screen.grabWindow(self.chart_0.winId())
            #
            #     pix.save(picture_path)
            #     pix_0.save(picture_path_0)

            # if self.agreen_ouput==True and self.agreen_ouput_1==False:
            #     picture_path_1 = file_path.split('.')[0] + '_acc.jpg'
            #     picture_path_2 = file_path.split('.')[0] + '_vel.jpg'
            #     picture_path_3 = file_path.split('.')[0] + '_dis.jpg'
            #
            #     pix_1 = screen.grabWindow(self.chart_1.winId())
            #     pix_2 = screen.grabWindow(self.chart_2.winId())
            #     pix_3 = screen.grabWindow(self.chart_3.winId())
            #
            #     pix_1.save(picture_path_1)
            #     pix_2.save(picture_path_2)
            #     pix_3.save(picture_path_3)

            if format_type == 'xlsx':
                import openpyxl

                wb = openpyxl.Workbook()
                ws = wb.active
                ws.append(['目标反应谱频率(Hz)', '目标反应谱加速度(g)', '设计反应谱频率(Hz)', '设计反应谱加速度(g)'])
                for i in range(len(self.fre_list_fit)):
                    line = [self.fre_list_pre[i], self.acc_list_pre[i], self.fre_list_fit[i], self.acc_list_fit[i]]
                    ws.append(line)

                if self.agreen_ouput == True and self.agreen_ouput_1 == False:
                    ws.append([])
                    ws.append(['时程 (s)', '加速度 (g)', '时程 (s)', '速度 (m/s)', '时程 (s)', '位移(m)'])
                    for j in range(len(self.t3)):
                        line = [self.t1[j], self.data[j], self.t2[j], self.vel[j], self.t3[j], self.dis[j]]
                        ws.append(line)

                    ws.append([self.t1[j + 1], self.data[j + 1], self.t2[j + 1], self.vel[j + 1]])
                    ws.append([self.t1[j + 2], self.data[j + 2]])
                wb.save(file_path)

            elif format_type == 'csv':
                with open(file_path, 'w', encoding='GBK', newline='')as f:
                    writer = csv.writer(f)
                    writer.writerow(['目标反应谱频率(Hz)', '目标反应谱加速度(g)', '设计反应谱频率(Hz)', '设计反应谱加速度(g)'])
                    for i in range(len(self.fre_list_fit)):
                        line = [self.fre_list_pre[i], self.acc_list_pre[i], self.fre_list_fit[i], self.acc_list_fit[i]]
                        writer.writerow(line)

            elif format_type == 'txt':
                with open(file_path, 'w', encoding='UTF-8')as f:
                    f.writelines(['目标反应谱频率(Hz)    ', '目标反应谱加速度(g)    ', '设计反应谱频率(Hz)    ', '设计反应谱加速度(g)    '])
                    f.write('\n')
                    for i in range(len(self.fre_list_fit)):
                        line = [str(self.fre_list_pre[i]), '   ', str(self.acc_list_pre[i]), '   ',
                                str(self.fre_list_fit[i]), '   ', str(self.acc_list_fit[i])]
                        f.writelines(line)
                        f.write('\n')

        else:
            QMessageBox.information(None, '提醒', '当前状态下不可输出数据', QMessageBox.Ok)
            return

    def output_data_1(self):
        """生成时程分析的数据存储文件"""

        file_path, file_type = QFileDialog.getSaveFileName(self, "save file", "./projects/untitled_accumulate",
                                                           "xlsx files (*.xlsx);;csv files (*.csv);;txt files(*.txt);;all files(*.*)")

        format_type = file_path.split('.')[-1]

        if file_path and self.agreen_ouput==False and self.agreen_ouput_1==True:

            if format_type == 'xlsx':
                import openpyxl

                wb = openpyxl.Workbook()
                ws = wb.active

                ws.append(['时程 (s)', '加速度 (g)', '时程 (s)', '速度 (m/s)', '时程 (s)', '位移(m)'])
                for i in range(len(self.t3)):
                    line = [self.t1[i], self.data[i], self.t2[i], self.vel[i], self.t3[i], self.dis[i]]
                    ws.append(line)

            elif format_type == 'csv':
                with open(file_path, 'w', encoding='GBK', newline='')as f:
                    writer = csv.writer(f)
                    writer.writerow(['时程 (s)', '加速度 (g)', '时程 (s)', '速度 (m/s)', '时程 (s)', '位移(m)'])
                    for i in range(len(self.t3)):
                        line = [self.t1[i], self.data[i], self.t2[i], self.vel[i], self.t3[i], self.dis[i]]
                        writer.writerow(line)
                    writer.writerow([self.t1[i + 1], self.data[i + 1], self.t2[i + 1], self.vel[i + 1]])
                    writer.writerow([self.t1[i + 2], self.data[i + 2]])

            elif format_type == 'txt':
                with open(file_path, 'w', encoding='UTF-8')as f:
                    f.writelines(
                        ['时程 (s)        ', '加速度 (g)        ', '时程 (s)        ', '速度 (m/s)        ', '时程 (s)        ',
                         '位移(m)        '])
                    f.write('\n')
                    for i in range(len(self.t3)):
                        # line = [self.fre_list_pre[i], self.acc_list_pre[i], self.fre_list_fit[i],self.acc_list_fit[i]]
                        n_line = [str(self.t1[i]) + '     ', str(self.data[i]) + '     ', str(self.t2[i]) + '     ',
                                  str(self.vel[i]) + '     ', str(self.t3[i]) + '     ', str(self.dis[i])]
                        line = [i[:7] for i in n_line]
                        line = [line[0], '       ', line[1], '       ', line[2], '       ', line[3], '       ', line[4],
                                '       ', line[5]]
                        f.writelines(line)
                        f.write('\n')
                    f.writelines([str(self.t1[i + 1])[:7], '       ', str(self.data[i + 1])[:7], '       ',
                                  str(self.t2[i + 1])[:7], '       ', str(self.vel[i + 1])[:7]])
                    f.write('\n')
                    f.writelines([str(self.t1[i + 2])[:7], '       ', str(self.data[i + 2])[:7]])
            return
        else:
            pass

    def onSeriesHoverd(self, point, state):
        """鼠标悬停事件(底部x,y)"""
        if state:
            try:
                name = self.sender().name()
            except:
                # QCursor.pos()悬停提示文字显示的位置
                name = ""
            QToolTip.showText(QCursor.pos(), "%s\nx: %s\ny: %s" %
                              (name, point.x(), point.y()))


if __name__ == "__main__":
    """程序入口"""
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
