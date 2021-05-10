def rFibMemo(x, memo):
    if x == 0:
        memo[0] = 0
        return (0, memo)
    elif x == 1:
        memo[1] = 1
        return (1, memo)
    try:
        return (memo[x], memo)
    except:
        memo[x] = rFibMemo(x-1, memo)[0] + rFibMemo(x-2, memo)[0]
        return (memo[x], memo)


rFibEle, table = rFibMemo(10, {})
print ('Element = ', rFibEle)
print ('Table = ', table)