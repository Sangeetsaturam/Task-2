row=int(input("enter no of row:"))
col=int(input("enter no of col:"))

print("enter the elements of matrix1")
m1=[[int(input()) for i in range(col)] for j in range(row)]
print("m1:")
for i in range(row):
	for j in range(col):
		print(format(m1[i][j],"<3"),end="")
	print()

print("enter the elements of matrix2")
m2=[[int(input()) for i in range(col)] for j in range(row)]
print("m1:")
for i in range(row):
	for j in range(col):
		print(format(m2[i][j],"<3"),end="")
	print()

print("result:")
res=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
	for j in range(col):
		res[i][j]=m1[i][j]+m2[i][j]

		print(format(res[i][j],"<3"),end="")
	print()  

# Output:
# enter no of row:2
# enter no of col:2
# enter the elements of matrix1
# 1
# 2
# 3
# 4
# m1:
# 1  2
# 3  4
# enter the elements of matrix2
# 1
# 2
# 3
# 4
# m1:
# 1  2
# 3  4
# result:
# 2  4
# 6  8