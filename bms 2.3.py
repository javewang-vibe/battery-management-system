# 电池数据分析系统
# 面对一堆电池温度，求平均值，最大值，最小值，并根据数据来判断系统最终的状态为保护、警告或者正常。
temp=[30,35,55,70,40]
normal_count=0
warning_count=0
danger_count=0

for t in temp:
    print("当前温度为:",t,"摄氏度")
    if t < 0:
        print("低温")
        warning_count += 1
    elif t <= 45:
        print("正常")
        normal_count += 1
    elif t <= 60:
        print("警告")
        warning_count += 1
    else:
        print("危险")
        danger_count += 1

print()

avg_temp=sum(temp)/len(temp)
max_temp=max(temp)
min_temp=min(temp)
print("平均温度：", round(avg_temp, 2), "摄氏度")
print("最高温度：", max_temp, "摄氏度")
print("最低温度：", min_temp, "摄氏度")
print("正常次数：", normal_count)
print("警告次数：", warning_count)
print("危险次数：", danger_count)
if danger_count>0:
    system_status="PROTECTION"
elif warning_count>0:
    system_status="WARNING"
else:
    system_status="NORMAL"
print(f"系统状态为：{system_status}")
