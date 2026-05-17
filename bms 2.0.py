# 函数版电池温度监测系统(输入三次错误自动锁定）
# 温度检测函数
def check_temp(temp):
    if temp < 0:
        print("❄️ 低温警告！")
    elif temp <= 45:
        print("✅ 电池温度正常")
    elif temp <= 60:
        print("⚠️ 温度偏高，请注意")
    else:
        print("🚨 危险！电池过热!")
error_count=0
while True:
    temp_input=input("请输入当前温度(按q退出）:")
    if temp_input=="q":
        print("系统已退出")
        break
    try:
        temp=float(temp_input)
    except:
        error_count+=1
        print(f"输入错误，请输入数字或q!当前错误次数:{error_count}/3`")
        if error_count==3:
            print("错误次数过多，系统锁定！")
            break
        continue
    error_count=0
    check_temp(temp)
