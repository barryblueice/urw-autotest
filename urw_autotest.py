import sys
import os
import time
import shutil
import psutil
import signal
from PyQt5 import QtCore

from PyQt5.QtCore import (QRegExp,
    QObject,
    QThread,
    pyqtSignal)

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QMainWindow,
    QLineEdit,
    QLabel,
    QPushButton,
    QMessageBox,
    QCheckBox,
    QTextEdit
)

from PyQt5.QtGui import QRegExpValidator

from event import (
    get_disk_info,
    get_drives,
    get_drives_type,
    disk_list_is_empty,
    run_urwtest_single,
    run_urwtest_multi
)

from urw_test_ui import Ui_Dialog

import warnings
 
warnings.filterwarnings("ignore", category=DeprecationWarning)

class WorkerThread(QThread):
    drive_changed = pyqtSignal(list)
    
    def run(self):
        formal_drive_list = get_drives()
        while True:
            now_drive_list = get_drives()
            if len(formal_drive_list) > len(now_drive_list):
                ejected_drive = [item for item in formal_drive_list if item not in now_drive_list]
                formal_drive_list = get_drives()
                for i in ejected_drive:
                    self.drive_changed.emit([i,"ejected"])
            elif len(formal_drive_list) < len(now_drive_list):
                inserted_drive = [item for item in now_drive_list if item not in formal_drive_list]
                formal_drive_list = get_drives()
                for i in inserted_drive:
                    self.drive_changed.emit([i,"inserted"])
            time.sleep(1)
        
class selfForm(QMainWindow, Ui_Dialog):
    
    def __init__(self):
        super(selfForm, self).__init__()
        self.setupUi(self)
        
        self.urw_count: QLineEdit
        self.urw_choice: QComboBox
        self.isempty: QCheckBox
        self.label_2: QLabel
        self.output: QTextEdit
        
        self.empty_all: QPushButton
        self.show_all: QPushButton
        self.urw_start: QPushButton
        self.urw_stop: QPushButton
        count_validator = QRegExpValidator(QRegExp("[0-9]+"))
        
        self.A: QCheckBox
        self.B: QCheckBox
        self.C: QCheckBox
        self.D: QCheckBox
        self.E: QCheckBox
        self.F: QCheckBox
        self.G: QCheckBox
        self.H: QCheckBox
        self.I: QCheckBox
        self.J: QCheckBox
        self.K: QCheckBox
        self.L: QCheckBox
        self.M: QCheckBox
        self.N: QCheckBox
        self.O: QCheckBox
        self.P: QCheckBox
        self.Q: QCheckBox
        self.R: QCheckBox
        self.S: QCheckBox
        self.T: QCheckBox
        self.U: QCheckBox
        self.V: QCheckBox
        self.W: QCheckBox
        self.X: QCheckBox
        self.Y: QCheckBox
        self.Z: QCheckBox
        
        self.check_box_map = {
            'A': self.A, 'B': self.B, 'C': self.C, 'D': self.D, 'E': self.E,
            'F': self.F, 'G': self.G, 'H': self.H, 'I': self.I, 'J': self.J,
            'K': self.K, 'L': self.L, 'M': self.M, 'N': self.N, 'O': self.O,
            'P': self.P, 'Q': self.Q, 'R': self.R, 'S': self.S, 'T': self.T,
            'U': self.U, 'V': self.V, 'W': self.W, 'X': self.X, 'Y': self.Y, 'Z': self.Z
        }
        self.drive_type_list = {}
        self.chosen_list = set({})
        
        
        self.urw_count.setValidator(count_validator)
        self.urw_count.setEnabled(False)
        self.label_2.setEnabled(False)
        
        self.urw_choice.currentIndexChanged.connect(self.on_urw_choice_changed)
        self.show_all.clicked.connect(self.get_disk_list)
        self.empty_all.clicked.connect(self.clear_all)
        
        self.A.stateChanged.connect(self.handleDiskChanged)
        self.B.stateChanged.connect(self.handleDiskChanged)
        self.C.stateChanged.connect(self.handleDiskChanged)
        self.D.stateChanged.connect(self.handleDiskChanged)
        self.E.stateChanged.connect(self.handleDiskChanged)
        self.F.stateChanged.connect(self.handleDiskChanged)
        self.G.stateChanged.connect(self.handleDiskChanged)
        self.H.stateChanged.connect(self.handleDiskChanged)
        self.I.stateChanged.connect(self.handleDiskChanged)
        self.J.stateChanged.connect(self.handleDiskChanged)
        self.K.stateChanged.connect(self.handleDiskChanged)
        self.L.stateChanged.connect(self.handleDiskChanged)
        self.M.stateChanged.connect(self.handleDiskChanged)
        self.N.stateChanged.connect(self.handleDiskChanged)
        self.O.stateChanged.connect(self.handleDiskChanged)
        self.P.stateChanged.connect(self.handleDiskChanged)
        self.Q.stateChanged.connect(self.handleDiskChanged)
        self.R.stateChanged.connect(self.handleDiskChanged)
        self.S.stateChanged.connect(self.handleDiskChanged)
        self.T.stateChanged.connect(self.handleDiskChanged)
        self.U.stateChanged.connect(self.handleDiskChanged)
        self.V.stateChanged.connect(self.handleDiskChanged)
        self.W.stateChanged.connect(self.handleDiskChanged)
        self.X.stateChanged.connect(self.handleDiskChanged)
        self.Y.stateChanged.connect(self.handleDiskChanged)
        self.Z.stateChanged.connect(self.handleDiskChanged)
        
        self.urw_start.clicked.connect(self.urw_process_start)
        self.urw_stop.clicked.connect(self.urw_process_stop)
        
        avalible_drive_list = get_drives()
        
        enable_list = {}
        
        for i in avalible_drive_list:
            enable_list.update({i:self.check_box_map[i]})
            
        for i in enable_list.values():
            i.setEnabled(True)
            
        self.output.append('磁盘类别检测结果：')
        self.drive_type_list: dict
        self.drive_type_list = get_drives_type()
        
        for i in self.drive_type_list.keys():
            self.output.append(f"{i}: {(self.drive_type_list)[i]['drive_type_str']}")
            if (int((self.drive_type_list)[i]['drive_type']) != 3) and (int((self.drive_type_list)[i]['drive_type']) != 6):
                self.check_box_map[i].setEnabled(False)
    
        self.monitor_thread = WorkerThread()
        self.monitor_thread.drive_changed.connect(self.update_disk_status)
        self.monitor_thread.start()
    
    def update_disk_status(self, drive_list):
        if drive_list[1] == 'inserted':
            self.output.append(f'磁盘 {drive_list[0]}: 已插入')
            (self.check_box_map)[drive_list[0]].setEnabled(True)
        elif drive_list[1] == 'ejected':
            self.output.append(f'磁盘 {drive_list[0]}: 已弹出')
            (self.check_box_map)[drive_list[0]].setEnabled(False)

    def on_urw_choice_changed(self):
        self.urw_count.setEnabled(True)
        if self.urw_choice.currentIndex() == 1:
            self.urw_count.setEnabled(True)
            self.label_2.setEnabled(True)
            self.isempty.setChecked(False)
            self.isempty.setEnabled(False)
        else:
            self.urw_count.setEnabled(False)
            self.label_2.setEnabled(False)
            self.isempty.setEnabled(True)
            self.urw_count.setText('')
    
    def information_box(self,title:str,content:str):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(content)
        msg_box.exec_()
        
    def warning_box(self,title:str,content:str):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(content)
        msg_box.exec_()
    
    def get_disk_list(self):
        disk_info = get_disk_info()
        if disk_info != False:
            msg = ''
            for name, device_id in disk_info:
                msg += f"\n{device_id} {name}"
            msg = msg.replace('\n','',1)
            msg_box = QMessageBox()
            msg_box.setWindowTitle('当前本机磁盘列表')
            msg_box.setText(msg)
            msg_box.exec_()
        else:
            self.warning_box(title='错误',content='获取硬盘列表失败，请再试一次！')
    
    def handleDiskChanged(self):
        sender: QObject
        sender = self.sender()
        value = str(sender.objectName())
        
        self.chosen_list: set
        
        self.chosen_list.add(value) if sender.isChecked() else self.chosen_list.discard(value)
    
    def urw_process_start(self):
        
        def run_single_test(chosen_list):
            msg = '\n开始跑圈, 目标磁盘: '
            for i in list(chosen_list):
                msg += f'{i}:, '
                run_urwtest_single(disk=i)
            msg += '圈数1圈。'
            self.output.append(msg)
        
        def run_multi_test(chosen_list,count):
            self.warning_box(title='警告',content='即将进入自动化操作，在测试过程未结束之前请不要随意操作电脑，以免产生不必要的麻烦！')
            msg = '\n开始跑圈, 目标磁盘: '
            for i in list(chosen_list):
                msg += f'{i}:, '
                run_urwtest_multi(
                    disk=i,
                    count=count
                    )
            msg += f'圈数{count}圈。'
            self.output.append(msg)
        
        if self.chosen_list == set({}):
            self.warning_box(title='错误',content='您还未选择任何磁盘！')
        else:
            if self.urw_choice.currentIndex() == 0:
                empty_list = disk_list_is_empty(list(self.chosen_list))
                if empty_list == True:
                    run_single_test(self.chosen_list)
                else:
                    if self.isempty.isChecked():
                        run_single_test(self.chosen_list)
                    else:
                        msg = ''
                        for i in empty_list:
                            msg += f'\n{i}:' 
                        empty_confirm = QMessageBox.question(self, '提示', f'''以下磁盘目录存在测试文件：
{msg}

是否要清除磁盘数据？''',QMessageBox.Yes | QMessageBox.No)
                        if empty_confirm == QMessageBox.Yes:
                            try:
                                for i in empty_list:
                                    for j in os.listdir(f'{i}:\\'):
                                        if (j.endswith('.bin')) or j.endswith('.BIN'):
                                            if os.path.isfile(os.path.join(f'{i}:\\',j)):
                                                os.remove(os.path.join(f'{i}:\\',j))
                            except:
                                self.information_box(title='提示',content='清空失败，请手动清空磁盘')
                            run_single_test(self.chosen_list)
                        else:
                            run_single_test(self.chosen_list)
            else:
                count = self.urw_count.displayText()
                if count == '':
                    self.information_box(title='提示',content='请输入跑圈次数！')
                else:
                    empty_list = disk_list_is_empty(list(self.chosen_list))
                    if empty_list == True:
                        run_multi_test(chosen_list=self.chosen_list,count=count)
                    else:
                            msg = ''
                            for i in empty_list:
                                msg += f'\n{i}:' 
                            empty_confirm = QMessageBox.question(self, '提示', f'''以下磁盘目录存在测试文件
{msg}

是否要清除磁盘数据？''',QMessageBox.Yes | QMessageBox.No)
                            if empty_confirm == QMessageBox.Yes:
                                # try:
                                    for i in empty_list:
                                        for j in os.listdir(f'{i}:\\'):
                                            if (j.endswith('.bin')) or j.endswith('.BIN'):
                                                if os.path.isfile(os.path.join(f'{i}:\\',j)):
                                                    os.remove(os.path.join(f'{i}:\\',j))
                                # except:
                                #     self.information_box(title='提示',content='清空失败，请手动清空磁盘')
                                    run_multi_test(chosen_list=self.chosen_list,count=count)
                            else:
                                run_multi_test(chosen_list=self.chosen_list,count=count)
    
    def urw_process_stop(self):
        def kill_process(process_name):
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'] == process_name:
                        pid = proc.info['pid']
                        os.kill(pid, signal.SIGTERM)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
        stop_confirm = QMessageBox.warning(self, '警告', '是否要终止所有进程',QMessageBox.Yes | QMessageBox.No)
        try:
            if stop_confirm == QMessageBox.Yes:
                kill_process(process_name="urwtest_v18.exe")
                kill_process(process_name="cmd.exe")
                self.information_box(title='提示',content='已终止所有进程')
        except Exception as e:
            self.warning_box(title='警告',content=f'错误：{e}\n，请自行手动停止进程！')
    
    def clear_all(self):
        for i in self.check_box_map.values():
            i: QCheckBox
            i.setChecked(False)
        self.chosen_list = set({})
        self.information_box(title='提示',content='已重置选项')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = selfForm()
    mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())
    mainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    mainWindow.show()
    sys.exit(app.exec_())