def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)




def partition(the_list, start_index, end_index):

    pivot = the_list[end_index]

    left_index  = start_index
    right_index = end_index - 1

    while left_index <= right_index:

        # Walk until we find something on the left side that belongs
        # on the right (less than the pivot).
        while left_index <= end_index and the_list[left_index] < pivot:
            left_index += 1

        # Walk until we find something on the right side that belongs
        # on the left (greater than or equal to the pivot).
        while right_index >= start_index and the_list[right_index] >= pivot:
            right_index -= 1

        # Swap the items at left_index and right_index, moving the element
        # that's smaller than the pivot to the left half and the element
        # that's larger than the pivot to the right half.
        if left_index < right_index:
            the_list[right_index], the_list[left_index] =\
                the_list[left_index], the_list[right_index]

        # Unless we've looked at all the elements in the list and are
        # done partitioning. In that case, move the pivot element into
        # its final position.
        else:
            the_list[end_index], the_list[left_index] = the_list[left_index], the_list[end_index]

    return left_index

def quicksort_sublist(the_list, start_index, end_index):

    # Base case: list with 0 or 1 elements.
    if (start_index >= end_index):
        return

    # Divide the list into two smaller sublists
    pivot_index = partition(the_list, start_index, end_index)

    # Recursively sort each sublist
    quicksort_sublist(the_list, start_index, pivot_index - 1)
    quicksort_sublist(the_list, pivot_index + 1, end_index)

def quicksort(the_list):
    quicksort_sublist(the_list, 0, len(the_list) - 1)



    
