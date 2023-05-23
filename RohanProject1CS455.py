
# Rohan Mankame Project 1

#creating arrays to hold each equation, each equation will have its own array inside a bigger array representing a matrix
#answer and equations metrix will stay seprate
n = int(input("enter number of equations you want to enter: "))  # Building answer matrix from user input
ans= []
for i in range(n):
    NewNum = float(input("enter ans of equation"+ str(i+1) + ": "))
    ans.append(NewNum)

b = []
A = [] # holds all values in the matrix
for i in range(n):
    b=[]
    for j in range(n):
        NewNum = float(input("enter coefficient of x"+ str(j+1)  +"in equation "+str(i+1) +":")) # Building the square equation matrix
        b.append(NewNum)
    A.append(b)
# print(A)
# print(ans)
U=A # setting up matrix U

# creating matrix L (will input values in when calculating U)
w,h = n,n
L = [[0 for x in range(w)]for y in range(h)]
for j in range(n):
    for i in range(n):
        if j==i:
            L[i][j] = 1  # make middle values 1 diagonally
        else:
            L[i][j]=0  # set everything else to 0

# print(L)

# Finding U and filling in L
for k in range(n-1):
    for i in range(k+1,n):
        if U[i][k] != 0.0: # check value is not already 0
            multi=U[i][k]/U[k][k]  # calculate ratio used to get set our unwanted to 0 and calculate rows
            L[i][k] = -multi  # filling in values in L, replace 0 in L with opposite of the multiplier
            for j in range(k,n):
                U[i][j] = U[i][j] - multi*U[k][j] # row reduction
            ans[i] = ans[i] - multi*ans[k] # making sure ans matrix is also edited with row reduction

# print(U)
# print(L)

# Now both matrix U and L have been created and ready to be used for calculation of y values

# Calculating matrix y with solutions of y1,y2,...yn ,using ans and L matrixs
y= [0 for x in range(w)]   # create y matrix
y[n-1]=ans[n-1]/L[n-1][n-1]
for i in range(n-2,-1,-1):   # loop rows starting with getting yn to y1
    CalcY = ans[i]
    for j in range(i+1,n):  # loop columns for y val
        CalcY = CalcY -L[i][j]*y[j]
    y[i] = CalcY/L[i][i] # y value
#print(y)

# Now matrix y has created and ready to be used for calculation of x values

# Calculating matrix y with solutions of x1,x2,...xn ,using y and U matrixs
x= [0 for x in range(w)]    # create x matrix
x[n-1]=y[n-1]/U[n-1][n-1]
for i in range(n-2,-1,-1):  # loop rows starting with getting xn to x1
    CalcX = y[i]
    for j in range(i+1,n): # loop columns for x val
        CalcX = CalcX -U[i][j]*x[j]
    x[i] = CalcX/U[i][i] # x value
# print(x)

print("Program has found the x values")

# output the solutions of x
for i in range(len(x)):
    print("x"+str(i+1)+" is " + str(x[i]))

print("X values outputted")
print("Program will end now")

