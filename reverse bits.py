def reversebit(n,bitsize):
    binno=bin(n)

    afterrev=binno[-1:1:-1]
    afterrev=afterrev + (bitsize-len(afterrev)) * '0'

    print(int(afterrev,2))


m = int(input())
bitsize=32
for i in range(m):
    n=int(input())
    reversebit(n,bitsize)
