ore = []
temp = []
or_min = []
or_max = []
for i in range(24):
    ore.append(i)
for i in range(len(ore)):
    t = input("Temprature pe ora "+ str(ore[i]) +" ")
    temp.append(int(t))
media = int(sum(temp)/24)
print("media este : " + str(media))
print(str(max(temp)) + " , " + str(min(temp)))
for i in range(24):
    if temp[i] == max(temp):
        or_max.append(ore[i])
    elif temp[i] == min(temp):
        or_min.append(ore[i])
print(or_min)
print(or_max)