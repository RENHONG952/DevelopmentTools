import itertools
import string
import random
import time

# 組合選擇的字符集
def build_charset(include_numbers, include_alphabet, include_special):
    charset = ""
    if include_numbers:
        charset += string.digits
    if include_alphabet:
        charset += string.ascii_letters
    if include_special:
        charset += string.punctuation
    return charset

# 生成隨機目標密碼
def generate_random_password(max_length, include_numbers, include_alphabet, include_special):
    charset = build_charset(include_numbers, include_alphabet, include_special)
    # 隨機長度和隨機字符組合
    actual_length = random.randint(1, max_length)
    password = ''.join(random.choice(charset) for _ in range(actual_length))
    return password

# 最大密碼長度
while True:
    try:
        max_password_length = int(input("請輸入最大密碼長度 : "))
        if max_password_length < 1:
            print("最大密碼長度必須大於零！")
        else:
            break
    except ValueError:
        print("請輸入有效的數字！")

# 密碼是否包含數字
while True:
    password_number = input("密碼是否包含數字 (Y/N) : ").lower()
    if password_number == 'y':
        include_numbers = True
        break
    elif password_number == 'n':
        include_numbers = False
        break
    else:
        print("請輸入正確的數字選項要求！")

# 密碼是否包含字母
while True:
    password_alphabet = input("密碼是否包含字母 (Y/N) : ").lower()
    if password_alphabet == 'y':
        include_alphabet = True
        break
    elif password_alphabet == 'n':
        include_alphabet = False
        break
    else:
        print("請輸入正確的字母選項要求！")

# 密碼是否包含特殊字符
while True:
    password_special = input("密碼是否包含特殊字符 (Y/N) : ").lower()
    if password_special == 'y':
        include_special = True
        break
    elif password_special == 'n':
        include_special = False
        break
    else:
        print("請輸入正確的特殊字符選項要求！")

# 檢查是否至少選擇一種密碼類型
if not (include_numbers or include_alphabet or include_special):
    print("至少需要選擇一種密碼類型！")
    exit()

# 生成隨機密碼
target_password  = generate_random_password(max_password_length, include_numbers, include_alphabet, include_special)
# 根據選擇生成字符集
charset = build_charset(include_numbers, include_alphabet, include_special)

# 進行密碼暴力破解
start_time = time.time()
count = 0
success = False
for length in range(1, max_password_length + 1):
    for password_tuple in itertools.product(charset, repeat = length):
        # 拼接字串
        password_str = ''.join(password_tuple)
        count += 1
        if count % 10000 == 0:
            print(f"正在嘗試第 {count} 種密碼組合 : {password_str}")
        # 成功破解密碼
        if password_str == target_password:
            print(f"\n密碼已破解 : {password_str} / 總共嘗試了 {count} 種密碼組合，共計耗時 {time.time() - start_time:.2f} 秒。")
            success = True
            break
    # 結束程式
    if success:
        break
# 確保所有組合皆已嘗試完畢
if not success:
    print("未能破解密碼，請檢查密碼長度和字符集設置。")