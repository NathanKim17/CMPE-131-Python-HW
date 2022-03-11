def sort_list(unsortedList):
    #obtain length of the list
    n = len(unsortedList)
    if n == 0:
        return "List is empty"
    
    if (isinstance(unsortedList[0], int) != True) and (isinstance(unsortedList[0], float) != True):
         return "List must be of type int or float"

    #initialize outer loop control variable
    i = 0
    #outer loop which runs n times
    while i < n:
        j = 0
        #inner loop which iterates over the unsorted items (does not look at the sorted items)
        while j < n-i-1:
            #if the current item is greater than the next item, swap
            if unsortedList[j] > unsortedList[j+1]:
                temp = unsortedList[j]
                unsortedList[j] = unsortedList[j+1]
                unsortedList[j+1] = temp
            #increment j
            j = j + 1
        #increment i
        i = i + 1
    #unsortedList is now sorted
    return unsortedList
    

uL = [3, 2, 56, -22, 5736, 23]
uL = sort_list(uL)
print(uL)
nullList = ["apple", "gaga"]
nullList = sort_list(nullList)
print(nullList)
