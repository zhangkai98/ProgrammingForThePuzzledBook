#Programming for the Puzzled -- Srini Devadas
#You Can Read Minds (With a Little Calibration)
#Five random cards are chosen and one of them is hidden.
#Given four cards in a particular order, you can figure out what the fifth card is!

#Deck is are a list of strings, each string is a card
#The order of cards in the list matters.
deck = ['A_C', '2_C', '3_C', '4_C', '5_C', '6_C', '7_C', '8_C', '9_C', '10_C', 'J_C', 'Q_C',
        'K_C', 'A_D', '2_D', '3_D', '4_D', '5_D', '6_D', '7_D', '8_D', '9_D', '10_D', 'J_D',
        'Q_D', 'K_D', 'A_H', '2_H', '3_H', '4_H', '5_H', '6_H', '7_H', '8_H', '9_H', '10_H',
        'J_H', 'Q_H', 'K_H', 'A_S', '2_S', '3_S', '4_S', '5_S',
        '6_S', '7_S', '8_S', '9_S', '10_S', 'J_S', 'Q_S', 'K_S']

#This procedure figures out which card should be hidden based on the distance
#between the two cards that have the same suit.
#It returns the hidden card, the first exposed card, and the distance
def outputFirstCard(numbers, oneTwo, cards):


    encode = (numbers[oneTwo[0]] - numbers[oneTwo[1]]) % 13
    if encode > 0 and encode <= 6:
        hidden = oneTwo[0]
        other = oneTwo[1]
    else:
        hidden = oneTwo[1]
        other = oneTwo[0]
        encode = (numbers[oneTwo[1]] - numbers[oneTwo[0]]) % 13

##    #The following print statement is just for debugging!
##    print ('Hidden card is:', cards[hidden], 'and need to encode', encode)

    return hidden, other, encode


#This procedure orders three cards depending on the number "code" that
#needs to be encoded. 
#This part Should be changed in ex3
def outputNext3Cards(code, ind):
    
    if code == 1:
        second, third, fourth = ind[0], ind[1], ind[2]
    elif code == 2:
        second, third, fourth = ind[0], ind[2], ind[1]
    elif code == 3:
        second, third, fourth = ind[1], ind[0], ind[2]       
    elif code == 4:
        second, third, fourth = ind[1], ind[2], ind[0]
    elif code == 5:
        second, third, fourth = ind[2], ind[0], ind[1]
    else:
        second, third, fourth = ind[2], ind[1], ind[0]

    print ('Second card is:', deck[second])
    print ('Third card is:', deck[third])
    print ('Fourth card is:', deck[fourth])

    
#Sorts elements in tlist in ascending order.
def sortList(tlist):
    for index in range(0, len(tlist)-1):
        ismall = index
        for i in range(index, len(tlist)):
            if tlist[ismall] > tlist[i]:
                ismall = i
        tlist[index], tlist[ismall] = tlist[ismall], tlist[index]
    
    return

#This procedure is similar to AssistantOrdersCards() except it
#takes in a large number and "randomly" generates five cards.
def ComputerAssistant():

    print ('Cards are character strings as shown below.')
    print ('Ordering is:', deck)
    cards, cind, cardsuits, cnumbers = [], [], [], []
    numsuits = [0, 0, 0, 0]
    number = 0
    while number < 99999:
        number = int(input('Please give random number' +
                               ' of at least 6 digits:'))

#   #Generating 5 all different indices
    inum = 0
    clist = []
    while len(clist) < 5:
        number = number * (inum + 1) // (inum + 2)
        n = number % 52
        ++ inum
        if not n in clist:
            clist.append(n)

#   #Generating the list of pairsuits
    pairsuitlist = []
    for i in range(5):
        n = clist[i]
        cards.append(deck[n])
        cind.append(n)
        cardsuits.append(n // 13)
        cnumbers.append(n % 13)
        numsuits[n // 13] += 1
        if numsuits[n // 13] > 1 and (not (n // 13) in pairsuitlist):
            pairsuitlist.append(n // 13)
            
##    #Just for debugging
    print (cards)

    encode_min = 7
    hidden_final, other_final = 0, 0
    for pairsuit in pairsuitlist:
        cardh = []
        for i in range(5):
            if cardsuits[i] == pairsuit:
                cardh.append(i)

        hidden, other, encode = outputFirstCard(cnumbers, cardh, cards)
        if encode < encode_min:
            encode_min = encode
            hidden_final = hidden
            other_final = other
    print ('First card is:', cards[other_final])
    
    remindices = []
    for i in range(5):
        if i != hidden_final and i != other_final:
            remindices.append(cind[i])

    sortList(remindices)
    outputNext3Cards(encode_min, remindices)

    guess = input('What is the hidden card?')
    if guess == cards[hidden]:
        print ('You are a Mind Reader Extraordinaire!')
    else:
        print ('Sorry, not impressed!')

    return

ComputerAssistant()
