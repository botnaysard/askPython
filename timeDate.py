# LESSON

import time
timenow = time.time()

# print ticks just for curiosity purposes
print(timenow)

# convert ticks to human readable values

timenow = time.localtime(time.time())

#check output, again for curiosity
print(timenow)

year, month, day, hour, minute = timenow[0:5]
print(str(day) + "." + str(month) + "." + str(year))
print(str(hour) + ":" + str(minute))

# EXERCISES

print("\n")
print(str(year) + "-" + str(month) + "-" + str(day))