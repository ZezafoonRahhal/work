Z=int(input("Z="))
x=res=0
while Z!=0:
    res=res+(Z%2)*(10**x)
    Z=Z//2
    x=x+1
print(f"the binary number= {res}")
