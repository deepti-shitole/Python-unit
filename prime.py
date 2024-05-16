import math
 
def is_prime(num):
     if num < 0:
        return 'Negative numbers are not allowed'
     for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
     return True
