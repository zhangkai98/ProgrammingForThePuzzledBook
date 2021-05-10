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

corpus30 = ['abed', 'abet', 'abets', 'abut', 'acme', 'acre',
          'acres', 'actors', 'actress', 'airmen', 'alert',
          'alerted', 'ales', 'aligned', 'allergy', 'alter',
          'altered', 'amen', 'anew', 'angel', 'angle',
          'antler', 'apt', 'bade', 'baste', 'bead',
          'beast', 'beat', 'beats', 'beta']

corpus100 = ['abed', 'abet', 'abets', 'abut', 'acme', 'acre',
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
          'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean',
          'abed', 'abet', 'abets', 'abut', 'acme', 'acre',
          'acres', 'actors', 'actress', 'airmen', 'alert',
          'alerted', 'ales', 'aligned', 'allergy', 'alter',
          'altered', 'amen', 'anew', 'angel', 'angle',
          'antler', 'apt', 'bade', 'baste', 'bead',
          'beast', 'beat', 'beats', 'beta','apt', 'bade', 'baste']


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

# print (sorted(corpus, key=primeHash))

# len(strList) = 100
def dictByPrimeHash(strList):
    L = [[] for x in range(len(strList))]
    for s in strList:
        L[primeHash(s) % 97].append(s)
    return L 

print(dictByPrimeHash(corpus100))


