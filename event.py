import win32api
import win32con
import ctypes
import string
import subprocess
import win32com.client
import time
import os
import wmi
import glob

urwtest_path = os.path.join(os.getcwd(),'urwtest_v18.exe')

def enter():
    win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
    win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)

def run_urwtest_single(disk: str):
        subprocess.run(['start', 'cmd', '/c', urwtest_path, f'{disk}:', 'Y'], shell=True)

def run_urwtest_multi(disk: str, count: str):
    
    # shell = win32com.client.Dispatch("WScript.Shell")
    # shell.Run("cmd.exe /k")

    # shell.AppActivate("cmd.exe")
    # time.sleep(1)

    shell = win32com.client.Dispatch("WScript.Shell")
    shell.Run(f"{urwtest_path}")

    shell.AppActivate("urwtest_v18.exe")
    time.sleep(1)

    # shell.SendKeys(f"{urwtest_path}")
    # enter()
    # time.sleep(1)

    shell.SendKeys(disk)
    enter()
    time.sleep(1)

    shell.SendKeys('Y')
    enter()
    time.sleep(1)

    shell.SendKeys(count)
    enter()
    time.sleep(1)

    if count != '1':
    
        shell.SendKeys('Y')
        enter()

    # child = wexpect.spawn('cmd.exe /c')
    
# run_urwtest_multi(disk='I',count='3')

def get_disk_info():
    try:
        c = wmi.WMI()
        disk_info = []
        disks = sorted(c.Win32_DiskDrive(), key=lambda disk: disk.Index)
        for disk in disks:
            name = disk.Caption.strip()
            for partition in disk.associators("Win32_DiskDriveToDiskPartition"):
                for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                    disk_info.append((name, logical_disk.DeviceID))
        disk_info.sort(key=lambda x: x[1])
        return disk_info
    except:
        return False
    
def get_drives():
    drives = []
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f"{letter}")
        bitmask >>= 1
    return drives

DRIVE_UNKNOWN = 0
DRIVE_NO_ROOT_DIR = 1
DRIVE_REMOVABLE = 2
DRIVE_FIXED = 3
DRIVE_REMOTE = 4
DRIVE_CDROM = 5
DRIVE_RAMDISK = 6

def disk_list_is_empty(disk_list: list):
    list_not_empty = []
    
    for i in disk_list:  
        directory = f'{i}:\\'
        bin_files = glob.glob(os.path.join(directory, '*.bin'), recursive=True)
        _bin_files = glob.glob(os.path.join(directory, '*.BIN'), recursive=True) 
        if bin_files:
            list_not_empty.append(i)  
        elif _bin_files:
            list_not_empty.append(i)  
            
    if list_not_empty != []:
        return list_not_empty
    else:
        return True

def get_drives_type() -> dict:
    drives_info = {}
    bitmask = ctypes.windll.kernel32.GetLogicalDrives()
    
    for letter in string.ascii_uppercase:
        drive = f"{letter}:"
        if bitmask & 1:
            drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)

            if drive_type == DRIVE_FIXED:
                drive_type_str = "本地磁盘"
            elif drive_type == DRIVE_REMOVABLE:
                drive_type_str = "可移动磁盘"
            elif drive_type == DRIVE_CDROM:
                drive_type_str = "CD-ROM"
            elif drive_type == DRIVE_RAMDISK:
                drive_type_str = "内存盘"
            else:
                drive_type_str = "Unknown"
            drives_info.update({letter.replace(':',''):{
                'drive_type_str':drive_type_str,
                'drive_type':drive_type
                    }})
        bitmask >>= 1
    return drives_info