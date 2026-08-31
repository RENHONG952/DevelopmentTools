from pathlib import Path

# 鎖定路徑
desktop = Path.home() / "Desktop"

# 建立資料夾
while True:
    folder_name = input("請輸入資料夾名稱 : ")
    folder = desktop / folder_name
    try:
        folder.mkdir(exist_ok=False)
        break
    except FileExistsError:
        print("資料夾已存在，請重新輸入名稱！")
        
# 建立多個副資料夾
subfolder_name = ["folder_" + str(i) for i in range(1, 11)]
for i in subfolder_name:
    subfolder = folder / i
    subfolder.mkdir()
print("操作已成功完成！")