# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\urw_autotest\urw_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 644)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 491, 621))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.line = QtWidgets.QFrame(self.Main)
        self.line.setGeometry(QtCore.QRect(310, 10, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.Main)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 301, 421))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.A = QtWidgets.QCheckBox(self.groupBox)
        self.A.setEnabled(False)
        self.A.setGeometry(QtCore.QRect(50, 30, 71, 16))
        self.A.setObjectName("A")
        self.B = QtWidgets.QCheckBox(self.groupBox)
        self.B.setEnabled(False)
        self.B.setGeometry(QtCore.QRect(50, 60, 71, 16))
        self.B.setObjectName("B")
        self.C = QtWidgets.QCheckBox(self.groupBox)
        self.C.setEnabled(False)
        self.C.setGeometry(QtCore.QRect(50, 90, 71, 16))
        self.C.setObjectName("C")
        self.D = QtWidgets.QCheckBox(self.groupBox)
        self.D.setEnabled(False)
        self.D.setGeometry(QtCore.QRect(50, 120, 71, 16))
        self.D.setObjectName("D")
        self.E = QtWidgets.QCheckBox(self.groupBox)
        self.E.setEnabled(False)
        self.E.setGeometry(QtCore.QRect(50, 150, 71, 16))
        self.E.setObjectName("E")
        self.G = QtWidgets.QCheckBox(self.groupBox)
        self.G.setEnabled(False)
        self.G.setGeometry(QtCore.QRect(50, 210, 71, 16))
        self.G.setObjectName("G")
        self.F = QtWidgets.QCheckBox(self.groupBox)
        self.F.setEnabled(False)
        self.F.setGeometry(QtCore.QRect(50, 180, 71, 16))
        self.F.setObjectName("F")
        self.H = QtWidgets.QCheckBox(self.groupBox)
        self.H.setEnabled(False)
        self.H.setGeometry(QtCore.QRect(50, 240, 71, 16))
        self.H.setObjectName("H")
        self.I = QtWidgets.QCheckBox(self.groupBox)
        self.I.setEnabled(False)
        self.I.setGeometry(QtCore.QRect(50, 270, 71, 16))
        self.I.setObjectName("I")
        self.J = QtWidgets.QCheckBox(self.groupBox)
        self.J.setEnabled(False)
        self.J.setGeometry(QtCore.QRect(50, 300, 71, 16))
        self.J.setObjectName("J")
        self.K = QtWidgets.QCheckBox(self.groupBox)
        self.K.setEnabled(False)
        self.K.setGeometry(QtCore.QRect(50, 330, 71, 16))
        self.K.setObjectName("K")
        self.L = QtWidgets.QCheckBox(self.groupBox)
        self.L.setEnabled(False)
        self.L.setGeometry(QtCore.QRect(50, 360, 71, 16))
        self.L.setObjectName("L")
        self.M = QtWidgets.QCheckBox(self.groupBox)
        self.M.setEnabled(False)
        self.M.setGeometry(QtCore.QRect(50, 390, 71, 16))
        self.M.setObjectName("M")
        self.N = QtWidgets.QCheckBox(self.groupBox)
        self.N.setEnabled(False)
        self.N.setGeometry(QtCore.QRect(200, 30, 71, 16))
        self.N.setObjectName("N")
        self.O = QtWidgets.QCheckBox(self.groupBox)
        self.O.setEnabled(False)
        self.O.setGeometry(QtCore.QRect(200, 60, 71, 16))
        self.O.setObjectName("O")
        self.P = QtWidgets.QCheckBox(self.groupBox)
        self.P.setEnabled(False)
        self.P.setGeometry(QtCore.QRect(200, 90, 71, 16))
        self.P.setObjectName("P")
        self.Q = QtWidgets.QCheckBox(self.groupBox)
        self.Q.setEnabled(False)
        self.Q.setGeometry(QtCore.QRect(200, 120, 71, 16))
        self.Q.setObjectName("Q")
        self.R = QtWidgets.QCheckBox(self.groupBox)
        self.R.setEnabled(False)
        self.R.setGeometry(QtCore.QRect(200, 150, 71, 16))
        self.R.setObjectName("R")
        self.S = QtWidgets.QCheckBox(self.groupBox)
        self.S.setEnabled(False)
        self.S.setGeometry(QtCore.QRect(200, 180, 71, 16))
        self.S.setObjectName("S")
        self.T = QtWidgets.QCheckBox(self.groupBox)
        self.T.setEnabled(False)
        self.T.setGeometry(QtCore.QRect(200, 210, 71, 16))
        self.T.setObjectName("T")
        self.U = QtWidgets.QCheckBox(self.groupBox)
        self.U.setEnabled(False)
        self.U.setGeometry(QtCore.QRect(200, 240, 71, 16))
        self.U.setObjectName("U")
        self.V = QtWidgets.QCheckBox(self.groupBox)
        self.V.setEnabled(False)
        self.V.setGeometry(QtCore.QRect(200, 270, 71, 16))
        self.V.setObjectName("V")
        self.W = QtWidgets.QCheckBox(self.groupBox)
        self.W.setEnabled(False)
        self.W.setGeometry(QtCore.QRect(200, 300, 71, 16))
        self.W.setObjectName("W")
        self.X = QtWidgets.QCheckBox(self.groupBox)
        self.X.setEnabled(False)
        self.X.setGeometry(QtCore.QRect(200, 330, 71, 16))
        self.X.setObjectName("X")
        self.Z = QtWidgets.QCheckBox(self.groupBox)
        self.Z.setEnabled(False)
        self.Z.setGeometry(QtCore.QRect(200, 390, 71, 16))
        self.Z.setObjectName("Z")
        self.Y = QtWidgets.QCheckBox(self.groupBox)
        self.Y.setEnabled(False)
        self.Y.setGeometry(QtCore.QRect(200, 360, 71, 16))
        self.Y.setObjectName("Y")
        self.Line_2 = QtWidgets.QFrame(self.groupBox)
        self.Line_2.setGeometry(QtCore.QRect(140, 20, 20, 391))
        self.Line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.Line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line_2.setObjectName("Line_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Main)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 0, 141, 581))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.urw_choice = QtWidgets.QComboBox(self.groupBox_2)
        self.urw_choice.setGeometry(QtCore.QRect(10, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.urw_choice.setFont(font)
        self.urw_choice.setEditable(False)
        self.urw_choice.setMaxVisibleItems(2)
        self.urw_choice.setObjectName("urw_choice")
        self.urw_choice.addItem("")
        self.urw_choice.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 80, 81, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.show_all = QtWidgets.QPushButton(self.groupBox_2)
        self.show_all.setGeometry(QtCore.QRect(10, 20, 121, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.show_all.setFont(font)
        self.show_all.setObjectName("show_all")
        self.urw_count = QtWidgets.QLineEdit(self.groupBox_2)
        self.urw_count.setGeometry(QtCore.QRect(10, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.urw_count.setFont(font)
        self.urw_count.setObjectName("urw_count")
        self.urw_start = QtWidgets.QPushButton(self.groupBox_2)
        self.urw_start.setGeometry(QtCore.QRect(10, 350, 121, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.urw_start.setFont(font)
        self.urw_start.setObjectName("urw_start")
        self.urw_stop = QtWidgets.QPushButton(self.groupBox_2)
        self.urw_stop.setGeometry(QtCore.QRect(10, 470, 121, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.urw_stop.setFont(font)
        self.urw_stop.setObjectName("urw_stop")
        self.line_2 = QtWidgets.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(0, 320, 141, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.empty_all = QtWidgets.QPushButton(self.groupBox_2)
        self.empty_all.setGeometry(QtCore.QRect(10, 240, 121, 71))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.empty_all.setFont(font)
        self.empty_all.setObjectName("empty_all")
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setGeometry(QtCore.QRect(0, 220, 141, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.isempty = QtWidgets.QCheckBox(self.groupBox_2)
        self.isempty.setGeometry(QtCore.QRect(20, 200, 91, 16))
        self.isempty.setObjectName("isempty")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Main)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 301, 151))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.output = QtWidgets.QTextEdit(self.groupBox_3)
        self.output.setGeometry(QtCore.QRect(10, 20, 281, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.line_4 = QtWidgets.QFrame(self.Main)
        self.line_4.setGeometry(QtCore.QRect(10, 150, 301, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tabWidget.addTab(self.Main, "")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.label_4 = QtWidgets.QLabel(self.About)
        self.label_4.setGeometry(QtCore.QRect(70, 200, 341, 171))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.About, "")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 620, 291, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "URW AutoTest   Powered by barryblueice, 2024"))
        self.groupBox.setTitle(_translate("Dialog", "盘符选择"))
        self.A.setText(_translate("Dialog", "A:"))
        self.B.setText(_translate("Dialog", "B:"))
        self.C.setText(_translate("Dialog", "C:"))
        self.D.setText(_translate("Dialog", "D:"))
        self.E.setText(_translate("Dialog", "E:"))
        self.G.setText(_translate("Dialog", "G:"))
        self.F.setText(_translate("Dialog", "F:"))
        self.H.setText(_translate("Dialog", "H:"))
        self.I.setText(_translate("Dialog", "I:"))
        self.J.setText(_translate("Dialog", "J:"))
        self.K.setText(_translate("Dialog", "K:"))
        self.L.setText(_translate("Dialog", "L:"))
        self.M.setText(_translate("Dialog", "M:"))
        self.N.setText(_translate("Dialog", "N:"))
        self.O.setText(_translate("Dialog", "O:"))
        self.P.setText(_translate("Dialog", "P:"))
        self.Q.setText(_translate("Dialog", "Q:"))
        self.R.setText(_translate("Dialog", "R:"))
        self.S.setText(_translate("Dialog", "S:"))
        self.T.setText(_translate("Dialog", "T:"))
        self.U.setText(_translate("Dialog", "U:"))
        self.V.setText(_translate("Dialog", "V:"))
        self.W.setText(_translate("Dialog", "W:"))
        self.X.setText(_translate("Dialog", "X:"))
        self.Z.setText(_translate("Dialog", "Z:"))
        self.Y.setText(_translate("Dialog", "Y:"))
        self.groupBox_2.setTitle(_translate("Dialog", "操作"))
        self.urw_choice.setCurrentText(_translate("Dialog", "单次跑圈"))
        self.urw_choice.setItemText(0, _translate("Dialog", "单次跑圈"))
        self.urw_choice.setItemText(1, _translate("Dialog", "多次跑圈"))
        self.label_2.setText(_translate("Dialog", "跑圈次数："))
        self.label.setText(_translate("Dialog", "跑圈方式："))
        self.show_all.setText(_translate("Dialog", "展示所有磁盘"))
        self.urw_start.setText(_translate("Dialog", "开始"))
        self.urw_stop.setText(_translate("Dialog", "停止"))
        self.empty_all.setText(_translate("Dialog", "重置磁盘选项"))
        self.isempty.setText(_translate("Dialog", "仅进行校验"))
        self.groupBox_3.setTitle(_translate("Dialog", "控制台"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), _translate("Dialog", "Main"))
        self.label_4.setText(_translate("Dialog", "URW-AutoTest\n"
"\n"
"Github: https://github.com/barryblueice/urw-autotest\n"
"Gitee: https://gitee.com/barryblueice/urw-autotest\n"
"\n"
"本产品遵照GPL协议开源。\n"
"GPL开源协议位于GitHub/Gitee项目。\n"
"\n"
"Bug反馈可提交Issue或加入反馈QQ群：885871360"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("Dialog", "About"))
        self.label_3.setText(_translate("Dialog", "  Powered by barryblueice, 2024."))
