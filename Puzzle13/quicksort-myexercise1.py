#Programming for the Puzzled -- Srini Devadas
#The Disorganized Handyman
#A recursive sorting algorithm based on pivoting where a pivot is selected
#and the list split into three lists: the first containing elements smaller
#than the pivot, second elements equal to the pivot, and the third containing
#elements greater than the pivot. These sublists are recursively sorted.


#This procedure selects a pivot and partitions the list into 3 sublists
#It only uses one element worth of additional storage for the pivot!
def pivotPartitionClever(lst, start, end):
    pivot = lst[end] 
    bottom = start - 1       
    top = end
    movecounts = 0

    done = False
    while not done: 

        while not done:
            #Move rightward from left searching for element > pivot
            bottom += 1 
            if bottom == top: 
                done = True 
                break
            if lst[bottom] > pivot: 
                lst[top] = lst[bottom]
                movecounts+=1
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

        while not done:
            #Move leftward from right searching for element < pivot
            top -= 1
            if top == bottom: 
                done = True 
                break
            if lst[top] < pivot: 
                lst[bottom] = lst[top]
                movecounts+=1
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

    lst[top] = pivot 
    #print (lst)
    return top, movecounts 


def quicksort(lst, start, end):
    moves = 0
    if start < end:
        #print ('Partition start: bottom =', start - 1, 'top = ', end)
        #print (lst)
        split, moves = pivotPartitionClever(lst, start, end) 
        #print ('Partition end')
        moves = moves + quicksort(lst, start, split - 1) + quicksort(lst, split + 1, end)
    return moves
    
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print ('Initial list a is:', a)
move = quicksort(a, 0, len(a) - 1)
print ('Sorted list a is:', a, ",", move, "times moved.")

L = list(range(100))
print ('Initial list L is:', L)
move = quicksort(L, 0, len(L) - 1)
print ('Sorted list L is:', L, ",", move, "times moved.")

D = list(range(99, -1 ,-1))
print ('Initial list D is:', D)
move = quicksort(D, 0, len(D) - 1)
print ('Sorted list D is:', D, ",", move, "times moved.")

# b = [4, 4, 65, 2, -31, 0, 99, 83, -31, 782, 1]

