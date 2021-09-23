
with open("./pr1/in.txt", 'r') as f:
    arr = f.readline().split(",")

rev,even,odd,div,h,m,n,o= [],[],[],[],[],[],[],[];
oddN= [];
u,uu,medE,medO = 0,0,0,0;
x,y = input("x, y = ").split(" ")
x, y = int(x), int(y)

#transform into int
for i in range(len(arr)):
    arr[i] = int(arr[i])

#writeline
def writeFile(string):
    f.writelines(string+"\n")
#b
for i in range(len(arr),0,-1):
    rev.append(arr[i-1])
#c
c = sorted(arr)
c.sort(reverse= True)
#d
for i in range(len(arr)):
    if (arr[i]%2==0):
        u+=1
        medE+=arr[i]
        even.append(arr[i])
    elif(arr[i]%2!=0):
        odd.append(arr[i])

#j
semnificative = []
for i in arr:
    if i>9 and i<100:
        semnificative.append(i)
#e
medE = medE/u
#f 
for i in range(len(arr)):
    if arr[i]>x and arr[i]%y!=0:
        div.append(arr[i])
    if arr[i]>x and arr[i]<y:
        h.append(arr[i])
#i
for i in range(len(arr)):
    if arr[i]<0 and arr[i]%2==1:
        oddN.append(arr.index(arr[i]))
#j tebuie de facut

#k
l = arr.index(min(arr))
arrayZero = arr[0]
arr[0]=min(arr)
arr[l] = arrayZero
   
#n
dividble = []
for i in arr:
    if i%3==0:
        dividble.append(i)
#o
division = []

for i in arr:
    counter = 0;
    if i > 0:
        for c in range(1,i):
            if i%c==0:
                counter+=1;
        if (counter<=4):
            division.append(i)
    elif i < 0:
        for c in range(i,1,-1):
            if i%c==0:
                counter+=1;
        if (counter<=4):
            division.append(i)
    else:
        division.append(i)




with open("./pr1/out.txt", 'w') as f:
    writeFile("a)"+str(arr[:5]))
    writeFile("b)"+str(rev))
    writeFile("c)"+str(c))
    writeFile("d)"+str(even))
    writeFile("e)"+str(medE))
    writeFile("f)"+str(odd))
    writeFile("g)"+str(div))
    writeFile("h)"+str(h))
    writeFile("i)"+str(oddN))
    writeFile("j)"+str(semnificative))
    writeFile("k) l)"+str(arr))
    writeFile("m)"+str(even))
    writeFile("n)"+str(dividble))
    writeFile("o)"+str(division))
    