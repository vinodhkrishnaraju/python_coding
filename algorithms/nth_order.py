def nth_order(arr, m):
    start =0
    index = 0
    end = len(arr) - 1
    newArray = [None] * len(arr)
    for i in range(1, len(arr), 1):
        print(i)
        if arr[i] < arr[index]:
            newArray[start] = arr[i]
            start += 1
        else:
            newArray[end] = arr[i]
            end -= 1

    return newArray
print(nth_order([12,5,6,10,11,13,15],3))



# int searchNumOccurrence(vector<int> &V, int k, int start, int end) {
#     if (start > end) return 0;
#     int mid = (start + end) / 2;
#     if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
#     if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
#     return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
# }
