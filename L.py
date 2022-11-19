'''L'''

size = int(input("Enter the size of your alphabet: "))
num = size

for row in range(1,num+1):
    for col in range(1,num+1):
        if row== num or col==1:
            sign="*"
            
        else:
            sign = " "
        print(sign, end="")
        
    print()
