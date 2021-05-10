
def twoDSearch(matrix, R, C, query):
	if R > (len(matrix)-1) or C < 0:
		return False
	topright = matrix[R][C]
	if topright == query:
		print('Find it!')
		print('Position:({} row, {} column)'.format(R+1, C+1))
		return True
	if topright < query:
		return twoDSearch(matrix, R+1, C, query)
	if topright > query:
		return twoDSearch(matrix, R, C-1, query)


def search(matrix, query):
	Col = len(matrix[0]) - 1
	if not twoDSearch(matrix, 0, Col, query):
		print('Not in this martix')

T = [[ 1,  4,  7, 11, 15],
	 [ 2,  5,  8, 12, 19],
	 [ 3,  6,  9, 16, 22],
	 [10, 13, 14, 17, 24],
	 [18, 21, 23, 26, 30]]

#search(T, 21)
search(T, 13)





	