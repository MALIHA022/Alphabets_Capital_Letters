'''N'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if col==1 or col==num or (col==row):
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    
