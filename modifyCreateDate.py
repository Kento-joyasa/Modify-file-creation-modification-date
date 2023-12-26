import os
import datetime
import pywintypes
import win32file
import win32con

# 设置要更改的单个文件路径
file_path = r'F:\AllCode\suanfa\期末作业\2021204469师宇鹤.pdf'

# 设置你想要更改到的具体时间
target_year = 2023
target_month = 12
target_day = 23
target_hour = 12
target_minute = 0
target_second = 0

# 创建一个新的datetime对象，表示目标修改时间
target_datetime = datetime.datetime(year=target_year, month=target_month, day=target_day,
                                    hour=target_hour, minute=target_minute, second=target_second)

# 将datetime对象转换成Windows系统的文件时间
win_file_time = pywintypes.Time(target_datetime)

# 检查文件是否存在
if os.path.isfile(file_path):
    # 打开文件获取句柄
    handle = win32file.CreateFile(
        file_path,
        win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL,
        None
    )

    # 修改文件创建日期
    win32file.SetFileTime(handle, win_file_time)

    # 关闭文件句柄
    handle.Close()
    print(f"Creation time for {file_path} updated to {target_datetime.strftime('%Y-%m-%d %H:%M:%S')}.")
else:
    print(f"The file {file_path} does not exist.")