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
    whilecounts = 0

    done = False
    while not done: 

        while not done:
            #Move rightward from left searching for element > pivot
            whilecounts += 1
            bottom += 1 
            if bottom == top: 
                done = True 
                break
            if lst[bottom] > pivot: 
                lst[top] = lst[bottom]
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

        while not done:
            #Move leftward from right searching for element < pivot
            whilecounts += 1
            top -= 1
            if top == bottom: 
                done = True 
                break
            if lst[top] < pivot: 
                lst[bottom] = lst[top]
                #print (lst, 'bottom =', bottom, 'top = ', top)
                break 

    lst[top] = pivot 
    #print (lst)
    return top, whilecounts 


def quicksort(lst, start, end):
    whiles = 0
    if start < end:
        #print ('Partition start: bottom =', start - 1, 'top = ', end)
        #print (lst)
        split, whiles = pivotPartitionClever(lst, start, end) 
        #print ('Partition end')
        whiles = whiles + quicksort(lst, start, split - 1) + quicksort(lst, split + 1, end)
    return whiles

'''    
a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print ('Initial list a is:', a)
whilects = quicksort(a, 0, len(a) - 1)
print ('Sorted list a is:', a, ",", whilects, "while counts.")
'''
L = list(range(100))
print ('Initial list L is:', L)
whilects = quicksort(L, 0, len(L) - 1)
print ('Sorted list L is:', L, ",", whilects, "while counts.")

D = list(range(99, -1 ,-1))
print ('Initial list D is:', D)
whilects = quicksort(D, 0, len(D) - 1)
print ('Sorted list D is:', D, ",", whilects, "while counts.")

R = [0] * 100
R[0] = 29
for i in range(100):
    R[i] = (9679 * R[i-1] + 12637 * i) % 2287
print ('Initial list R is:', R)
whilects = quicksort(R, 0, len(R) - 1)
print ('Sorted list R is:', R, ",", whilects, "while counts.")

