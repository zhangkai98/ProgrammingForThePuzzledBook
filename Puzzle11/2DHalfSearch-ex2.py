def twoDHalfSearch(matrix, originR, originC, rowsize, colsize, query):
	if matrix[originR+rowsize-1][originC+colsize-1] < query:
		return False

	row = originR + (rowsize - 1)// 2
	col = originC + (colsize - 1)// 2
	center = matrix[row][col]

	if rowsize == 1 or colsize == 1:
		if rowsize == 1 and colsize == 1:
			if center == query:
				print('Find it!')
				print('Position:({} row,{} column)'.format(row+1, col+1))
				return True
			return False
		elif rowsize == 1:
			if center == query:
				print('Find it!')
				print('Position:({} row,{} column)'.format(row+1, col+1))
				return True
			elif center < query:
				return twoDHalfSearch(matrix, originR, col+1, 1, colsize-(col-originC+1), query)
			elif center > query:
				return twoDHalfSearch(matrix, originR, originC, 1, col-originC+1, query)
		elif colsize == 1:
			if center == query:
				print('Find it!')
				print('Position:({} row,{} column)'.format(row+1, col+1))
				return True
			elif center < query:
				return twoDHalfSearch(matrix, row+1, originC, rowsize-(row-originR+1), 1, query)
			elif center > query:
				return twoDHalfSearch(matrix, originR, originC, row-originR+1, 1, query)

	if center == query:
		print('Find it!')
		print('Position:({} row,{} column)'.format(row+1, col+1))
		return True
	elif center < query:
		return twoDHalfSearch(matrix, originR, col+1, row-originR+1, colsize-(col-originC+1), query) \
				or twoDHalfSearch(matrix, row+1, originC, rowsize-(row-originR+1), col-originC+1, query) \
				or twoDHalfSearch(matrix, row+1, col+1, rowsize-(row-originR+1), colsize-(col-originC+1), query)
	elif center > query:
		return twoDHalfSearch(matrix, originR, originC, row-originR+1, col-originC+1, query) \
				or twoDHalfSearch(matrix, originR, col+1, row-originR+1, colsize-(col-originC+1), query) \
				or twoDHalfSearch(matrix, row+1, originC, rowsize-(row-originR+1), col-originC+1, query) 

def search(matrix, query):
	if not twoDHalfSearch(matrix, 0, 0, len(matrix), len(matrix[0]), query):
		print('Not in this matirx!')

T = [[ 1,  4,  7, 11, 15],
	 [ 2,  5,  8, 12, 19],
	 [ 3,  6,  9, 16, 22],
	 [10, 13, 14, 17, 24],
	 [18, 21, 23, 26, 30]]

#search(T, 21)
search(T, 22)

