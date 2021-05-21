import math

record_seconds = float(input())
distance_in_meters = float(input())
time_for_meter = float(input())

ivan_time = distance_in_meters * time_for_meter
slowing_distance = math.floor(distance_in_meters / 15)
lost_time = slowing_distance * 12.5
ivan_result = ivan_time + lost_time
difference = math.fabs(ivan_result - record_seconds)
if record_seconds <= ivan_result:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {ivan_result:.2f} seconds.")