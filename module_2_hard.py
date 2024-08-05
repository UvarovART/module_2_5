def aim(n):
    key = []
    for i in range(1,n):
        for j in range(i+1,n):
            if n % (i + j) == 0:
                answer = str(i) + str(j)
                key.append(answer)
    return key
n = int(input('print a key from 3 to 20: '))
key = aim(n)
print(key)