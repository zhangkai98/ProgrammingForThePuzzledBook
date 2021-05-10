
small = {'A': ['B', 'C'],
         'B': ['A', 'C', 'D'],
         'C': [ 'B', 'E'],
         'D': ['B', 'E'],
         'E': ['C', 'D', 'F'],
         'F': ['E']}

large = {'A': ['B', 'C', 'E'], 'B': ['A', 'C'], 'C': ['A', 'B', 'J'],
         'D': ['E', 'F', 'G'], 'E': ['A', 'D', 'K'], 'F': ['D', 'N'],
         'G': ['D', 'H', 'I'], 'H': ['G', 'M'], 'I': ['G', 'P'],
         'J': ['C', 'K', 'L'], 'K': ['E', 'J', 'L'], 'L': ['J', 'K', 'S'],
         'M': ['H', 'N', 'O'], 'N': ['F', 'M', 'O'], 'O': ['N', 'M', 'V'],
         'P': ['I', 'Q', 'R'], 'Q': ['P', 'W'], 'R': ['P', 'X'],
         'S': ['L', 'T', 'U'], 'T': ['S', 'U'], 'U': ['S', 'T', 'V'],
         'V': ['O', 'U', 'W'], 'W': ['Q', 'V', 'Y'], 'X': ['R', 'Y', 'Z'],
         'Y': ['W', 'X', 'Z'], 'Z': ['X', 'Y']}

def checkSymmetry(graph):
   isSymmetric = True
   for start in graph:
      for end in graph[start]:
         if start not in graph[end]:
            isSymmetric = False
            print('lack of \'', end, '\': [\'', start, '\']', sep='')
   return isSymmetric

checkSymmetry(small)