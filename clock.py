import time
import winsound

def focus_timer(total_time, focus_interval, break_interval):
    num_intervals = total_time // (focus_interval + break_interval)
    for i in range(num_intervals):
        print("Focus for {} minutes".format(focus_interval))
        time.sleep(focus_interval * 60)  # 转换为秒
        winsound.Beep(1000, 1000)  # 播放声音提醒休息
        print("Take a {}-minute break".format(break_interval))
        time.sleep(break_interval * 60)  # 转换为秒
        winsound.Beep(1000, 1000)  # 播放声音提醒继续专注

    print("Focus session complete!")

# 输入总时间（分钟）、专注时间（分钟）和休息时间（分钟）
total_time = int(input("Enter total time in minutes: "))
focus_interval = int(input("Enter focus interval in minutes: "))
break_interval = int(input("Enter break interval in minutes: "))

focus_timer(total_time, focus_interval, break_interval)
