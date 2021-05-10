#Programming for the Puzzled -- Srini Devadas
#Anagramania
#Given a list of words, sort them such that all anagrams are grouped together
#A correct, though inefficient algorithm

corpus = ['abed', 'abet', 'abets', 'abut', 'acme', 'acre', 'acres', 'actors',
          'actress', 'airmen', 'alert', 'alerted', 'ales', 'aligned', 'allergy',
          'alter', 'altered', 'amen', 'anew', 'angel', 'angle', 'antler', 'apt',
          'bade', 'baste', 'bead', 'beast', 'beat', 'beats', 'beta', 'betas',
          'came', 'care', 'cares', 'casters', 'castor', 'costar', 'dealing',
          'gallery', 'glean', 'largely', 'later', 'leading', 'learnt', 'leas',
          'mace', 'mane', 'marine', 'mean', 'name', 'pat', 'race', 'races',
          'recasts', 'regally', 'related', 'remain', 'rental', 'sale', 'scare',
          'seal', 'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean']


#This procedure groups together words that are anagrams by selecting a word
#and finding all other words that are anagrams of this word. It repeats until
#all words have been processed
def anagramGrouping(input):

    output = []
    seen = [False] * len(input)
    for i in range(len(input)):
        if seen[i]:
            continue
        output.append(input[i])
        seen[i] = True
        for j in range(i + 1, len(input)):
            #Check if the two are anagrams of each other
            if not seen[j] and anagram(input[i], input[j]):
                output.append(input[j])
                seen[j] = True
    return output


#This procedure checks if two strings/words are anagrams
def anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print (anagramGrouping(corpus))

