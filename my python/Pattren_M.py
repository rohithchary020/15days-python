# input
a=[[" " for i in range(11)] for i in range(11)]


# sep block
for i in range(11):
    for j in range(11):
        if j==0 or j==10:
            a[i][j]="M"
        elif i==j and i<6:
            a[i][j]="M"
        elif i+j==10 and i<5:
            a[i][j]="M"

# sep block
for i in range(11):
    for j in range(11):
        print(a[i][j],end=" ")
    print()
        
