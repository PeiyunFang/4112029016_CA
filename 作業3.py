# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 18:18:00 2023

@author: lr
"""

import os

if not os.path.exists("CS"):
    os.mkdir("CS")

file_path = os.path.join("CS", "homework.txt")

content = "4112029016_方姵云"
with open(file_path, "w") as file:
    file.write(content)

with open(file_path, "r") as file:
    file_content = file.read()
    print("檔案內容:", file_content)

file_info = os.stat(file_path)
print("檔案資訊:")
print(f"檔案大小: {file_info.st_size} bytes")
print(f"創建時間: {file_info.st_ctime}")
print(f"修改時間: {file_info.st_mtime}")

os.remove(file_path)
print(f"{file_path} 已刪除。")

os.rmdir("CS")
print("CS 目錄已刪除。")