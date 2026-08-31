# 服務費選項確認
while True:
    server_fee = input("是否包含額外服務費 ? (Y/N) : ").lower()
    if server_fee == "y":
        try:
            with_service_fee = True
            service_fee = float(input("請輸入服務費百分比 (%) : "))
            if not 0 <= service_fee <= 100:
                print("請輸入適當的服務費百分比區間！")
                continue
        except ValueError:
            print("請輸入正確的服務費百分比內容！")
            continue
        break
    elif server_fee == "n":
        with_service_fee = False
        break
    else:
        print("請輸入 Y 或 N 以確認是否需要計算服務費！")

# 輸入消費金額
fees = [[]]
person = 1
print("\n系統提示 : 輸入 A 切換至下一位消費者，輸入 B 結束並進行計算。")
while True:
    expense = input(f"請輸入第 {person} 位消費者的單/多筆消費金額 : ")
    # 下一位消費者
    if expense.lower() == "a":
        if not fees[person - 1]:
            print("請至少輸入一筆消費金額！")
            continue
        print()
        person += 1
        fees.append([])
        continue
    # 結束輸入金額
    elif expense.lower() == "b":
        if not fees[person - 1]:
            fees.pop()
        break
    # 記憶金額
    elif expense.isdigit():
        fees[person - 1].append(int(expense))
    else:
        print("請輸入正確的金額或指令！")

# 計算所有人的消費金額
print()
for i in range(len(fees)):
    total = sum(fees[i])
    # 包含服務費
    if with_service_fee:
        total += total * (service_fee / 100)
    print(f"第 {i + 1} 人的總消費金額 : $ {total:.1f}")