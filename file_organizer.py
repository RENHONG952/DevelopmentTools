from pathlib import Path

# 規則定義
rules = {
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx",
                  ".ppt", ".pptx", ".csv", ".md"],
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp",
               ".svg", ".ico"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".m4a", ".ogg"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm"],
    "archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "code": [".py", ".c", ".cpp", ".h", ".java", ".js",
             ".ts", ".html", ".css", ".json"]
}

# 路徑選擇
while True:
    path = input("請輸入要整理的資料夾路徑 : ")
    path = Path(path)
    # 路徑檢查
    if not path.exists():
        print("路徑不存在，請重新輸入。")
        continue
    if not path.is_dir():
        print("請輸入一個資料夾路徑。")
        continue
    break

# 進行檔案整理
for file in path.iterdir():
    # 確認是一般檔案
    if file.is_file():
        # 取得副檔名
        file_extension = file.suffix.lower()
        # 根據規則移動檔案
        moved = False
        for folder, extensions in rules.items():
            if file_extension in extensions:
                target_folder = path / folder
                target_folder.mkdir(exist_ok=True)
                file.rename(target_folder / file.name)
                moved = True
                break
        # 找不到對應副檔名
        if not moved:
            other_folder = path / "others"
            other_folder.mkdir(exist_ok=True)
            file.rename(other_folder / file.name)
print("檔案整理完成！")