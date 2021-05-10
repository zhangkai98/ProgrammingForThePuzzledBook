#Programming for the Puzzled -- Srini Devadas
#Anagramania
#Given a list of words, sort them such that all anagrams are grouped together
#An elegant, efficient algorithm

corpus = ['abed', 'abet', 'abets', 'abut', 'acme', 'acre',
          'acres', 'actors', 'actress', 'airmen', 'alert',
          'alerted', 'ales', 'aligned', 'allergy', 'alter',
          'altered', 'amen', 'anew', 'angel', 'angle',
          'antler', 'apt', 'bade', 'baste', 'bead',
          'beast', 'beat', 'beats', 'beta', 'betas',
          'came', 'care', 'cares', 'casters', 'castor',
          'costar', 'dealing', 'gallery', 'glean',
          'largely', 'later', 'leading', 'learnt', 'leas',
          'mace', 'mane', 'marine', 'mean', 'name', 'pat',
          'race', 'races', 'recasts', 'regally', 'related',
          'remain', 'rental', 'sale', 'scare', 'seal',
          'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean']

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

def chToprimef(ch):
    return primes[ord(ch) - 97]

def primeHashf(str):
    if len(str) == 0:
        return 1
    else:
        return chToprimef(str[0]) * primeHashf(str[1:])

def quicksort(lst, start, end):
    if start < end:
        split = pivotPartitionByPrimeHash(lst, start, end)
        quicksort(lst, start, split-1)
        quicksort(lst, split+1, end)
    
def pivotPartitionByPrimeHash(lst, start, end):
    pivot = lst[end]
    bottom = start - 1
    top = end
    done = False

    while not done:
        while not done:
            bottom += 1
            if bottom == top:
                done = True
                break
            if primeHashf(lst[bottom]) > primeHashf(pivot):
                lst[top] = lst[bottom]
                break

        while not done:
            top -= 1
            if top == bottom:
                done = True
                break
            if primeHashf(lst[top]) < primeHashf(pivot):
                lst[bottom] = lst[top]
                break
    lst[top] = pivot
    return top


quicksort(corpus, 0, len(corpus)-1)
print(corpus)

#print (sorted(corpus, key=primeHashf))

