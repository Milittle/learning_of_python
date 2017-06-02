import math
def quadratic(a,b,c):
    diff = b*b-4*a*c
    if(diff > 0):
        x1 = (-b + math.sqrt(diff))/(2*a)
        x2 = (-b - math.sqrt(diff))/(2*a)
        return (math.floor(x1),math.floor(x2))
    else:
        return '无解'
print(quadratic(1,-3,2))