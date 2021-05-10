def tileFourMissingYard(n, missList):
	if len(missList) != 4:
		print('Not four missing tiles!')
		return False

	size = 2**n
	quadMissList = []	
	for missTile in missList:
		if missTile[0] < 0 or missTile[0] > size:
			print('Missing tiles beyond yard!')
			return False
		if missTile[1] < 0 or missTile[1] > size:
			print('Missing tiles beyond yard!')
			return False
		quadMissList.append(2*(missTile[0]>=size//2) + \
			(missTile[1]>=size//2)) 

	isBelongFourQuad = belongFourQuad(quadMissList)
	if isBelongFourQuad:
		print('Four missing pieces belong to four different quadrant')

	isBelongOneLTile = False
	for i in range(4):
		threeMissList = [miss for miss in missList if miss != missList[i]]
		if belongOneLTile(threeMissList):
			isBelongOneLTile = True
			print('There are three missing pieces belong to one L-shape tile!')
			break

	if isBelongFourQuad or isBelongOneLTile:
		print('This yard can be tiled fully by function <recursiveTile>')
		return True
	else:
		print('This yard cann\'t be tiled fully by function <recursiveTile>')
		return False


def belongFourQuad(quadMissList):
	for i in range(len(quadMissList)-1):
		for j in range(i+1,len(quadMissList)):
			if quadMissList[i] == quadMissList[j]:
				return False

	return True

def belongOneLTile(threeMiss):
	originR, originC = threeMiss[0][0], threeMiss[0][1]
	for i in range(len(threeMiss)):
		if threeMiss[i][0] < originR:
			originR = threeMiss[i][0]
		if threeMiss[i][1] < originC:
			originC = threeMiss[i][1]

	for j in range(4):
		threePieces = [(originR+r, originC+c) for (r,c) in [(0, 0), (0, 1), (1, 0), (1, 1)]]
		threePieces.pop(j)
		res = True
		for piece in threePieces:
			res = res and (piece in threeMiss)
		if res:
			break

	return res 

tileFourMissingYard(3, [(4, 4), (1, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(4, 4), (3, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(3, 7), (4, 4), (4, 6), (4, 7)])
tileFourMissingYard(3, [(3, 3), (3, 4), (4, 3), (4, 4)])


