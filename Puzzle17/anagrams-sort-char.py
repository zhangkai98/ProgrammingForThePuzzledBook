#Programming for the Puzzled -- Srini Devadas
#Anagramania
#Given a list of words, sort them such that all anagrams are grouped together
#A more efficient algorithm though not efficient in terms of storage

corpus = ['abed', 'abet', 'abets', 'abut', 'acme', 'acre', 'acres', 'actors',
          'actress', 'airmen', 'alert', 'alerted', 'ales', 'aligned', 'allergy',
          'alter', 'altered', 'amen', 'anew', 'angel', 'angle', 'antler', 'apt',
          'bade', 'baste', 'bead', 'beast', 'beat', 'beats', 'beta', 'betas',
          'came', 'care', 'cares', 'casters', 'castor', 'costar', 'dealing',
          'gallery', 'glean', 'largely', 'later', 'leading', 'learnt', 'leas',
          'mace', 'mane', 'marine', 'mean', 'name', 'pat', 'race', 'races',
          'recasts', 'regally', 'related', 'remain', 'rental', 'sale', 'scare',
          'seal', 'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean']

corp = ['ate', 'but', 'eat', 'tub', 'tea']
        
#This procedure groups together words that are anagrams by selecting a word
#and finding all other words that are anagrams of this word. It repeats until
#all words have been processed
def anagramSortChar(input):

    canonical = []
    for i in range(len(input)):
        #Append tuple with the sorted letters as first item, and word as second item
        canonical.append((sorted(input[i]), input[i]))

    #Sort based on first tuple followed by second tuple
    canonical.sort()
    output = []
    for t in canonical:
        #print(t)
        output.append(t[1])

    return output


print (anagramSortChar(corpus))
