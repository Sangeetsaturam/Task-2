
p=int(input("enter no of row :"))
q=int(input("enter no of col :"))

print("enter the elements of matrix1")
m1=[[int(input()) for i in range(q)] for j in range(p)]
print("m1:")
for i in range(p):
	for j in range(q):
		print(format(m1[i][j],"<4"),end="")

res=[[0 for i in range(p)] for j in range(q)]
for i in range(q):
	for j in range(p):
		res[i][j]=m1[j][i]

print("result:")
for i in range(q):
    for j in range(p):
         print(format(res[i][j],"<4"), end="")
    print() 
     
# output:
# enter no of row :2
# enter no of col :2
# enter the elements of matrix1
# 1
# 2
# 3
# 4
# m1:
# 1   2   3   4   
# result:
# 1   3   2   4