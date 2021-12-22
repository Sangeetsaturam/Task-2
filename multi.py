
p=int(input("enter no of row for matr1:"))
q=int(input("enter no of col for mat2:"))
n=int(input("enter no of col for matr1 /row no of matr2"))


print("enter the elements of matrix1")
m1=[[int(input()) for i in range(n)] for j in range(p)]
print("m1:")
for i in range(p):
	for j in range(n):
		print(format(m1[i][j],"<3"),end="")
	print()

print("enter the elements of matrix2")
m2=[[int(input()) for i in range(q)] for j in range(n)]
print("m2:")
for i in range(q):
	for j in range(n):
		print(format(m2[i][j],"<3"),end="")
	print()


res=[[0 for i in range(q)] for j in range(p)]
for i in range(p):
	for j in range(q):
		for k in range(n):
			res[i][j]=res[i][j]+m1[i][k]+m2[k][j]

print("result:")
for i in range(p):
	for j in range(q):
		print(format(res[i][j],"<3"),end="")
	print()

# output:
# enter no of row for matr1:2
# enter no of col for mat2:2
# enter no of col for matr1 /row no of matr22
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
# m2:
# 1  2
# 3  4
# result:
# 7  9
# 11 13