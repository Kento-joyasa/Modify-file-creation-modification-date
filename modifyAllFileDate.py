import os
import datetime

# 设置要更改文件的文件夹路径
folder_path = r'path_to_your_dictionary'

# 设置你想要更改到的具体时间
target_year = 2023
target_month = 12
target_day = 24
target_hour = 12  # 24小时制
target_minute = 0
target_second = 0

# 创建一个新的datetime对象，表示目标修改时间
target_datetime = datetime.datetime(year=target_year, month=target_month, day=target_day,
                                    hour=target_hour, minute=target_minute, second=target_second)

# 转换目标时间为时间戳
new_mtime = target_datetime.timestamp()

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # 检查是否为文件
    if os.path.isfile(file_path):
        # 应用新的修改时间（这里我们将访问时间也设置为新的修改时间）
        os.utime(file_path, (new_mtime, new_mtime))

print(f"Modification times updated to {target_datetime.strftime('%Y-%m-%d %H:%M:%S')} where applicable.")