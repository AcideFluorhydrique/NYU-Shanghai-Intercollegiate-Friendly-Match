def lcp(s, t):
    k = 0
    for i in range(0, min(len(s), len(t))):
        if s[i] == t[i]:
            k += 1
        else:
            break
    return k

def suf(s,i):
    output = s[i-1:]
    return output

def f(s):
    fs = 0
    for i in range(1,len(s)+1):
        fs += lcp(s,suf(s,i))
    return fs

T = int(input(""))
A = []
for i in range(T):
    n = int(input())
    si = input()

    B = list(map(int, si.split()))
    #for j in range(n):
        #si = int(input(""))
        #2
        # B.append(si)

    p = 0
    for k in range(n):
        
        # F = []
        # p = 0
        """
        for l in B:
            F = []
            if l != B[k]:
                C[k] = l
                F.append(f(C))
                fc = max(F)
                output = fc^(int(l))
                p += output
        """
        F = []
        for l in range(1,1 + n):
            C = B.copy()
            #F = []
            if l != C[k]:
                C[k] = l
                #print("****",f(C))
                F.append(f(C))

        fc = max(F)
        #print(fc)
        output = fc^(k+1)
        p += output



    #for m in range(n)
    #xor = output^
    A.append(p)

for i in A:
    print(i)
