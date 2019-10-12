def fibo(n):
        r0 = 0
        r1 = 1
        r2 = r1 + r0

        if( n == 0): return r0
        if( n == 1): return r1
        if( n == 2): return r2

        for r in range(3, n+1):
            r0 = r1
            r1 = r2
            r2 = r1 + r0

        return r2

num = input("Enter a natural number: ")

fibo_seq = []
for n in range(0, int(num)+1):
    fibo_seq.append(fibo(n))

print("Here's your Fibonacci sequence:")
print(fibo_seq)
