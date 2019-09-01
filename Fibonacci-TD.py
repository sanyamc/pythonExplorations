memo=[]

def fib_helper(n):
    global memo
    if n==0 or n==1:
        return 1
    if memo[n]!=-1:
        return memo[n]
    val1 = fib_helper(n-1)
    memo[n-1] = val1
    val2 = fib_helper(n-2)
    memo[n-2] = val2

    memo[n] = val1+val2
    return val1+val2

def fib(n):
    global memo
    memo = []
    
    [memo.append(-1) for i in range(0,n+1)]
    return fib_helper(n)

def fib_BU_Helper(n):
    global memo
    for i in range(2, n+1):
        val = memo[i-1] + memo[i-2]
        memo.append(val)

        #global.memo.append((global.memo[i-1] + global.memo[i-2]))
    return memo[n]

def fib_BU(n):
    global memo
    memo = [1,1]
    
    return fib_BU_Helper(n)

    

def fib_naive(n):
    if n==0 or n==1:
        return 1
    return fib_naive(n-1)+fib_naive(n-2)






