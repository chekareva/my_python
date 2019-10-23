from random import randint 
A = [randint(-1000, 1000) for i in range(1000)] 
maxx = A.index(max(A)) 
minn = A.index(min(A)) 
count = 0 
if maxx > minn:
    for i in range(minn, maxx + 1):
        if A[i] < 0:
            count += 1
else:
    for i in range(minn, maxx + 1, -1):
        if A[i] < 0:
            count += 1 
print(count)
