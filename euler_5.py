sum=1
for i in range(1,21):
    sum*=i
for j in range(20, sum, 20):   # step by 20 since the number must be divisible by 20
    if all(j % c == 0 for c in range(1, 21)):
        print(j)
        break
