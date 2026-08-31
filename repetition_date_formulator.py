from datetime import datetime
import calendar

# 制定日期
while True:
    customize = input("請輸入 (Y) 自訂義日期或輸入 (N) 以當前日期為基準 : ")
    # 使用者自訂義日期
    if customize.lower() == "y":
        date_input = input("請輸入自訂義日期 (YYYY/MM/DD) : ")
        try:
            base_date = datetime.strptime(date_input, "%Y/%m/%d")
            break
        except ValueError:
            print("日期格式錯誤，請使用正確要求格式。")
            continue
    # 使用當前日期
    elif customize.lower() == "n":
        base_date = datetime.now()
        break
    else:
        print("請輸入正確的要求內容！")

# 重複安排天數
while True:
    try:
        repet_day = int(input("請輸入要重複安排的天數 : "))
        if repet_day <= 0:
            print("重複天數必須大於零!")
            continue
        break
    except ValueError:
        print("請輸入有效的天數整數。")

# 提取詳細日期
month = base_date.month
day = base_date.day
max_day = calendar.monthrange(base_date.year, month)[1]
# 無可安排日期
if (day + repet_day > max_day) : print("本月已無足夠天數可被安排！")
# 重複安排日期
weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
print()
while day + repet_day <= max_day:
    day += repet_day
    date = datetime(base_date.year, month, day)
    weekday = date.weekday()
    print(f"- {date.strftime('%Y/%m/%d')} ( {weekdays[weekday]} )")