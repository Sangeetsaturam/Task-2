#7.	We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    ans=False  
    
    for i in range(heads+1):
        j=heads-i
        if (2*i)+(4*j)==legs:
            chicken_count=i
            rabbit_count=j
            ans=True
            break
    if (ans==True):
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)
    
solve(50,150)

# output:
# 25 25