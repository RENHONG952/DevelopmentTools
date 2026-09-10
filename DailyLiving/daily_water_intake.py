# 體重輸入
while True:
    try:
        weight = float(input("請輸入體重 : "))
        if weight <= 0:
            print("體重必須大於零，才可以正確計算！")
            continue
        break
    except ValueError:
        print("請輸入有效的體重數值。")

# 計算建議攝取區間
water_intake_min = round(weight * 30)
water_intake_max = round(weight * 35)
print(f"\n一般情況下建議的每日飲水量約 : {water_intake_min} ~ {water_intake_max} mL")