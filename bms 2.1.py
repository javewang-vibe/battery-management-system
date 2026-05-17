# BMS状态监控系统v1
# 同时输入温度和电压进行监测
def check_temp(temp):
    if temp<0:
        print("低温警告！")
        return "WARNING"
    elif temp<=45:
        print("温度正常")
        return "NORMAL"
    elif temp<=60:
        print("温度偏高")
        return "WARNING"
    else:
        print("电池过热")
        return "PROTECTION"

def check_voltage(voltage):
    if voltage<3.0:
        print("电池过放")
        return "PROTECTION"
    elif voltage<=4.2:
        print("电压正常")
        return "NORMAL"
    else:
        print("电池过充")
        return "PROTECTION"

error_count=0
while True:
    temp_input=input("请输入当前温度(按q退出):")
    if temp_input=="q":
        print("系统已经退出")
        break
    voltage_input=input("请输入当前电压(按q退出):")
    if voltage_input=="q":
        print("系统已经退出")
        break
    try:
        temp=float(temp_input)
        voltage=float(voltage_input)
    except:
        error_count += 1
        print(f"输入错误，请输入数字或q！当前错误次数{error_count}/3")
        if error_count>=3:
            print("错误次数过多，系统锁定！")
            break
        continue
    error_count = 0

    temp_status=check_temp(temp)
    voltage_status=check_voltage(voltage)

    if temp_status=="PROTECTION" and voltage_status=="PROTECTION":
        system_status="PROTECTION"
    elif temp_status=="WARNING" and voltage_status=="WARNING":
        system_status="WARNING"
    else:
        system_status="NORMAL"

    print(f"当前系统状态为:{system_status}")
