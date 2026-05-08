def NumToHex(n):
    hex='0123456789ABCDEF'
    result=''
    if n==0:
         return '0'
    elif n<0 :
        n+=2**32
  
    while n>0:
            remainder=n%16
            result=hex[remainder]+result
            n//=16
    return result
    

n=int(input("Enter a number:"))

print("Hex number:",NumToHex(n))
