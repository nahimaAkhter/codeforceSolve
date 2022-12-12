# long long way
x=int(input())

for i in range (1,x+1):
    y= str(input())

    if len(y) >10:
        z = str(y[0]) + str(len(y[1:-1])) + str(y[-1])

        print(z)
    else:
        print(y)

