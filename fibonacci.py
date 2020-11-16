def fibonacci(sayi,n,counter):
    counter+=1
    
    a= sayi+n

    print(a, end=" ")
    
    if counter==30:
        
        return
    
    fibonacci(n,a,counter)
    
fibonacci(0,1,0)
    
    
    
