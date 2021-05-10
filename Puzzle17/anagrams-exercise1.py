#Programming for the Puzzled -- Srini Devadas
#Anagramania
#Given a list of words, sort them such that all anagrams are grouped together
#An elegant, efficient algorithm

#This procedure selects a pivot and partitions the list into 3 sublists
#It only uses one element worth of additional storage for the pivot!
def pivotPartitionClever(lst, start, end, f):
    pivot = lst[end] 
    bottom = start - 1       
    top = end

    done = False
    while not done: 

        while not done:
            #Move rightward from left searching for element > pivot
            bottom += 1 
            if bottom == top: 
                done = True 
                break
            if f(lst[bottom]) > f(pivot): 
                lst[top] = lst[bottom] 
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

        while not done:
            #Move leftward from right searching for element < pivot
            top -= 1
            if top == bottom: 
                done = True 
                break
            if f(lst[top]) < f(pivot): 
                lst[bottom] = lst[top] 
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

    lst[top] = pivot 
    #print (lst)
    return top 


def quicksort(lst, start, end, comparef):
    if start < end: 
        #print ('Partition start: bottom =', start - 1, 'top = ', end)
        #print (lst)
        split = pivotPartitionClever(lst, start, end, comparef) 
        #print ('Partition end')
        quicksort(lst, start, split - 1, comparef)
        quicksort(lst, split + 1, end, comparef)
    return

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

#Dictionary mapping letters of the alphabet to prime numbers
chToprime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

#This procedure computes the hash of a string recursively
def primeHash(str):
    if len(str) == 0:
        return 1
    else:
        return chToprime[str[0]] * primeHash(str[1:])

print (corpus)
quicksort(corpus, 0, len(corpus) - 1, primeHash)
print (corpus)


