def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result
    '''contador=num-1
    resultado=0
    while num>0:
        resultado=num*(contador)
        contador-=1
    return resultado'''



print(factorial(5))
