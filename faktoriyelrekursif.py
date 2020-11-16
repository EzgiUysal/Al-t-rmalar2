N=int(input("N giriniz:"))
def faktoriyel(N):
    if N==1:
        return 1
    else:
        print(N)
        return N*faktoriyel(N-1)
print(faktoriyel(N))

        
