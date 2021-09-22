ven = [200,300,600,100,250]
print(sum(ven))
print(int(sum(ven)/len(ven)))
print("venitul maximal e in ziua a " + str((int(ven.index(max(ven)))+1))+"-a")
print("venitul minimal e in ziua a " + str((int(ven.index(min(ven)))+1))+"-a")
