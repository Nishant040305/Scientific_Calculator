import time
def prime(n):
    s = time.time()
    if n == int(n):
        n = int(n)
        a = True
        for k in range(2,int(n**1/2)+3):
            if n%k==0:
                a = False
                k = k+1
                break
    else:
        a = False
    e = time.time()

    return a
def prange(a,b):
    a,b = int(a),int(b)
    if a>b:
        a,b=b,a
    L = list()
    for x in range(a,b+1):
        if prime(x)=='True':
            L.append(x)
    return L
                



if __name__ == '__main__':

    print(prime(999999937))
    x = input()