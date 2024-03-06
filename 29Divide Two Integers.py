def Solution(dividend,divisor):
    # if divisor == 1:
    #     if dividend>=2**31-1:
    #         return 2**31-1
    #     elif dividend<=-2**31:
    #         return -2**31
    #     else:
    #         return dividend
    # elif divisor == -1:
    #     if dividend >=2**31-1:
    #         return -2**32
    #     elif dividend <=-2**31:
    #         return 2**31-1
    #     else:
    #         return -dividend
    
    
    res = ''; sign = 1
    if (dividend<=0) ^ (divisor <=0):
        sign = -1
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    dividend_str = str(dividend)
    num = 0
    for i in range(len(dividend_str)):
        num = int(str(num)+dividend_str[i])
        digit = 0
        while num>=divisor:
            digit += 1
            num-=divisor
        res+=str(digit)
    res =  int(res)*sign
    if res >= 2**31-1:
        return 2**31-1
    elif res <= -2**31:
        return -2**31
    else:
        return res
        
dividend = 2147483647
divisor = -1
print(Solution(dividend, divisor))