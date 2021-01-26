# Ejercicio 1 

def triangle(n):
    result = ''
    for i in range(n,0,-1):
        no_spaces = n-i
        no_stars = 2*i-1
        result += '  ' * no_spaces + '* ' * no_stars + '\n'

    return result
    

print(triangle(4))

print(triangle(5))

print(triangle(6))

# Ejercicio 2

def eje2(n, m): 
    if n > m and m > 0:
        return ((n-1)/m) + ((n-1)/(m-1))
    elif m == n:
        return 1
    elif m == 0:
        return 1

print(eje2(50,35))
print(eje2(100,85))

# Ejercicio 3 


def rombo(n): 
    x = round((n/2)+0.5)
    y = round((n/2)-0.5)
    result = ''
    for  i in range(x):
     no_spacesup = x-i-1
     no_starsup = i+1
     result += " " * no_spacesup + "* " * no_starsup + '\n'

    for i in range(y,0,-1):
         no_spacesdown = y-i+1
         no_starsdown = i
         result += " " * no_spacesdown + "* " * no_starsdown + '\n'
    
    return (result)
    
print(rombo(7))
print(rombo(9))
print(rombo(11))

# Ejercicio 4 
lista = []
def pares (x,y):
    for num in range(x, y + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else: lista.append(num)
    print(lista)

from time import process_time
start = process_time()
pares(0,100000)            
stop = process_time()
print(stop-start)








 










    

