from math import sqrt

number = int(input("Son kiriting: "))

for i in range(2, number + 1): 
    is_prime = True 
    for j in range(2, int(sqrt(i)) + 1): 
        if i % j == 0:  
            is_prime = False 
            break  
    if is_prime: 
        print(i, end=" ")