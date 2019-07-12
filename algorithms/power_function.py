def power(x,n,d):

    print(mul_pow(x,n))

    # odd_flag = 0
    # if (n & 1) == 1:
    #     n = n - 1
    #     odd_flag = 1

    # mid == n // 2

power_hash = {}
def mul_pow(x, n):
    # print('recursion')
    if (x,n) in power_hash.keys():
        return power_hash[(x,n)]
    

    if n <= 1:
        return x
    if (n & 1) == 1:
        power_hash[(x,n)] = mul_pow(x,(n-1)//2) * mul_pow(x, n//2) * x
    else:
        power_hash[(x,n)] = mul_pow(x, n//2) * mul_pow(x, n//2)

    return power_hash[(x,n)] 
    


power(10,3,2)

