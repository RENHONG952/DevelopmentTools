# 輸入文字內容
text = input("請輸入要計算數量的內容 : ")

# 計算數量
char, digit, space, symbol = 0, 0, 0, 0
for i in text:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        symbol += 1

# 輸出結果
print(f"- 總字數 : {len(text)}\n- 文字數 : {char}\n- 數字數 : {digit}\n- 空格數 : {space}\n- 符號數 : {symbol}")