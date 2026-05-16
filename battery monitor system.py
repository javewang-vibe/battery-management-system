# 电池温度报警系统
while True:
    temp_input = input("请输入当前温度（输入q退出）:")
    if temp_input == "q":
        print("系统已经退出")
        break
    tem=float(temp_input)
    if tem>60:
        print("危险报警")
    elif 45<tem<=60:
        print("温度偏高")
    elif 0<=tem<=45:
        print("温度正常")
    else:
        print("低温警告")
# 加入while true不会停止，该如何停止？