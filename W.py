'''W'''

size = int(input("Enter a size: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        trick = row + col
        if col==1 or col==num or ((row==col and row>=((num+1)//2) or (trick==(num+1)) and row>=((num+1)//2))):
            sign = "*"
            print(sign,end="")
        else:
            sign = " "
            print(sign,end="")
    print()    
