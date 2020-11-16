N=int(input("N giriniz:"))
def toplam(N):
    if N==1:
        return 1
    else:
        print(N)
        return N+toplam(N-1)
print (toplam(N))

        
