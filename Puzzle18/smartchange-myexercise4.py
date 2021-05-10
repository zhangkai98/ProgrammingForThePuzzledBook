
memo = {}

def makeSmartChange(bills, target):
    global memo

    for bill in bills:

        if bill == target:
            memo[target] = [bill]
            return 

        elif bill < target:
            if (target-bill) in memo:
                sol = [bill] + memo[target-bill]
                if target in memo:
                    if len(sol) < len(memo[target]):
                        memo[target] = sol
                else:
                    memo[target] = sol

            else:
                makeSmartChange(bills, target-bill)

changeTarget = 21
bills = [7, 59, 71, 97]
makeSmartChange(bills, changeTarget)
print(memo[changeTarget])