def marg_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = marg_sort(left)
    right = marg_sort(right)
    return marg_sort_list(left, right)


def marg_sort_list(a_arry,b_arry):
    sorted_list = []
    i = j = 0
    while (i < len(a_arry)) and (j < len(b_arry)):
        if a_arry[i] <= b_arry[j]:
            sorted_list.append(a_arry[i])
            i += 1
        else:
            sorted_list.append(b_arry[j])
            j += 1
    while (i < len(a_arry)):
        sorted_list.append(a_arry[i])
        i += 1
    while (j < len(b_arry)):
        sorted_list.append(b_arry[j])
        j += 1
        
        
    return sorted_list



if __name__ == '__main__':
    a = [15,17,58,92,108,152,175,450]
    b = [12,13,46,95,352]
    lst = [484,8,481,48,4,4,48,454,45,5415,848,451,54]
    #sort = marg_sort_list(a , b)
    sort = marg_sort(lst)
    print(sort)
    