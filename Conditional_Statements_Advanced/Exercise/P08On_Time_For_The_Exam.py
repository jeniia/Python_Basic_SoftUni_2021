exam_hour = int(input())
exam_minutes = int(input())
arrive_hour = int(input())
arrive_minutes = int(input())
exam_time = exam_hour * 60 + arrive_minutes
arrive_time = arrive_hour * 60 + arrive_minutes
output = ""
output2 = ""
diff = 0
if arrive_time < exam_time - 30:
    output = "Early"
    diff = exam_time - arrive_time
    if diff < 60:
        output2 = f"{diff} minutes before the start"
    else:
        h = diff / 60
        m = diff % 60
        output2 = f"{h}:{m:.02f} hours before the start"
if arrive_time <= exam_time:
    output = "On time"
    diff = arrive_time - exam_time
    output2 = f"{diff} minutes before the start"
if arrive_time > exam_time:
    output = "Late"
    diff = arrive_time - exam_time
    if diff < 60:
        output2 = f"{diff} minutes after the start"
    else:
        diff = arrive_time - exam_time
        hours = diff / 60
        minutes = diff % 60
        output2 = f"{hours}:{minutes:.02f} hours after the start"
print(output)
print(output2)