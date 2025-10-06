def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
sum=0
for j in range(3,2000001):
    if prime(j)==True:
        sum+=j
print(sum+2)


