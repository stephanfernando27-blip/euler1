sum=0
x=1
y=2
z=0
while True:
    z=x+y
    x=y
    y=z
    if z%2==0:
        sum+=z
    if z>=4000000:
        break
print(sum)