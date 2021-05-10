def coins(row, table):

    if len(row) == 0:
        result = 0
        scheme = 1
        table[0] = (result, scheme)
        return (result, table)

    elif len(row) == 1:
        result = row[0]
        scheme = 2
        table[1] = (result, scheme)
        return (result, table)

    elif len(row) == 2:
        result = row[0] + row[1]
        scheme = 3
        table[2] = (result, scheme)
        return (result, table)

    skip = coins(row[1:], table)[0]
    pickThenjump = coins(row[2:], table)[0] + row[0]
    pickTwo = coins(row[4:], table)[0] + row[0] + row[1]
    result = max(skip, pickThenjump, pickTwo)
    scheme = [skip, pickThenjump, pickTwo].index(result) + 1
    table[len(row)] = (result, scheme)
    return (result, table)

def coinsMemoize(row, memo):

    if len(row) == 0:
        result = 0
        scheme = 1
        memo[0] = (result, scheme)
        return (result, memo)

    elif len(row) == 1:
        result = row[0]
        scheme = 2
        memo[1] = (result, scheme)
        return (result, memo)

    elif len(row) == 2:
        result = row[0] + row[1]
        scheme = 3
        memo[2] = (result, scheme)
        return (result, memo)

    try:
        return (memo[len(row)][0], memo)
    except KeyError:
        skip = coinsMemoize(row[1:], memo)[0]
        pickThenjump = coinsMemoize(row[2:], memo)[0] + row[0]
        pickTwo = coinsMemoize(row[4:], memo)[0] + row[0] + row[1]
        result = max(skip, pickThenjump, pickTwo)
        scheme = [skip, pickThenjump, pickTwo].index(result) + 1
        memo[len(row)] = (result, scheme)
        return (result, memo)     

def coinsMemoizeNoEx(row, memo):

    if len(row) == 0:
        result = 0
        scheme = 1
        memo[0] = (result, scheme)
        return (result, memo)

    elif len(row) == 1:
        result = row[0]
        scheme = 2
        memo[1] = (result, scheme)
        return (result, memo)

    elif len(row) == 2:
        result = row[0] + row[1]
        scheme = 3
        memo[2] = (result, scheme)
        return (result, memo)

    if len(row) in memo:
        return (memo[len(row)][0], memo)
    else:
        skip = coinsMemoize(row[1:], memo)[0]
        pickThenjump = coinsMemoize(row[2:], memo)[0] + row[0]
        pickTwo = coinsMemoize(row[4:], memo)[0] + row[0] + row[1]
        result = max(skip, pickThenjump, pickTwo)
        scheme = [skip, pickThenjump, pickTwo].index(result) + 1
        memo[len(row)] = (result, scheme)
        return (result, memo)

def coinsIterative(row):
    #table[i] contains the optimum output for the LAST i coins
    table = {}
    table[0] = (0, 1)
    table[1] = (row[-1], 2)
    table[2] = (row[-1] + row[-2], 3)
    for i in range(3, len(row) + 1):
        skip = table[i-1][0]
        pickThenjump = table[i-2][0] + row[-i]
        pickTwo = (table[i-4][0] if i>4 else 0) + row[-(i-1)] + row[-i]
        result = max(skip, pickThenjump, pickTwo)
        scheme = [skip, pickThenjump, pickTwo].index(result) + 1
        table[i] = (result, scheme)
    return (table[len(row)], table) 

def traceback(row, table):
    select = []
    i = 0
    while i < len(row):
        if table[len(row)-i][1] == 1:
            i += 1
        elif table[len(row)-i][1] == 2:
            select.append(row[i])
            i += 2
        elif  table[len(row)-i][1] == 3:
            select.append(row[i])
            select.append(row[i+1])
            i += 4

    print ('Input row = ', row)
    print ('Table = ', table)
    print ('Selected coins are', select, 'and sum up to', table[len(row)][0])

row = [14, 3, 27, 4, 5, 15, 1]
result, memo = coins(row, {})
traceback(row, memo)
result, memo = coinsMemoize(row, {})
traceback(row, memo)
result, memo = coinsIterative(row)
traceback(row, memo)
result, memo = coinsMemoizeNoEx(row, {})
traceback(row, memo)
