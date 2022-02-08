
            

        
def syracuse(n):
    global L
    L = []

    while n != 1 :
        if n % 2 == 0 :
            n = n // 2
            print(n)
            L.append(n)
            
    
        else :
            n = n*3+1
            print(n)
            L.append(n)
    return L

print(syracuse(45))

def testconjecture(n_max):
    for i in range (n_max):
        syracuse(i)
        if L[-1] == 1 :
            return True 
        else : 
            return False 

print(testconjecture(5))




def tempsdevol (n):
    k=0
    while n != 1 :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = n*3+1
        k = k+1
    return k
print("le temps de vol est", tempsdevol(45))

        

        
        

