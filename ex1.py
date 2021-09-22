vector = [1,2,3,4,5]
x,y = vector, vector;
sum,prod  = 0,1

print(x[0]+x[1]+x[2])
for i in range(len(y)):
    sum = sum + y[i]
print(sum)
for i in range(len(x)):
    prod = prod * x[i]
print(prod)
print(abs(y[2]))
print(x[0]+y[0])
