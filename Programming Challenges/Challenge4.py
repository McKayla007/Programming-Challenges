# work out distance travelled from speed and time
speed = int(input("Enter speed: "))
time = int(input("Enter time in seconds: "))
distance = speed*time
print("At the speed of", speed,"and the time of", time,"s, you will travel", distance,"m")

# EXTENSION: work out how fast you will need to move to travel certain distance within certain time
distance = int(input("Enter distance you want to travel: "))
time = int(input("Enter the amount of time you want to travel the distance by: "))
speed = distance/time
print("You will need to travel at a speed of", speed, "m/s to travel", distance, "m")