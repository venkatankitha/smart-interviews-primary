def flip(n):
    for i in range(n):
        a,b = map(int,input().split())
        c = a^b
        count = 0
        while c:
            count += c & 1
            c >>= 1
        print(count)

n = int(input())
flip(n)
