import sys
# Write your code here
def binary_search_asse(arr,num,left_index,right_indx):
    if right_indx < left_index:
        return 
    mid_index = (left_index+right_indx)//2
    if mid_index >= len(arr) or mid_index < 0:
        return 
    mid_number = arr[mid_index]
    
    if mid_number == num:
        return mid_index
    if mid_number < num:
        left_index += 1
    elif mid_number > num:
        right_indx -= 1
    return binary_search_asse(arr, num, left_index, right_indx) 
def binary_search_des(arr,num,left_index,right_indx):
    if right_indx < left_index:
        return 
    mid_index = (left_index+right_indx)//2
    if mid_index >= len(arr) or mid_index < 0:
        return 
    mid_number = arr[mid_index]
    
    if mid_number == num:
        return mid_index
    if mid_number < num:
        right_indx -= 1
    elif mid_number > num:
        left_index += 1
    return binary_search_des(arr, num, left_index, right_indx) 
if __name__ == '__main__':
    lst1 = []
    lst2 = []
    n = int(input())
    if n > 999:
        sys.setrecursionlimit(n*10)

    lst = [int(i) for i in input().split(' ')]
    if lst[0] < lst [1]:
        rag = int(input())
        for j in range(rag):
            serach = int(input())
            find = binary_search_asse(lst,serach,0,len(lst))
            if find != None:
                lst1.append(find)
        for x in lst1:
            print(x+1)
    else:
        rag = int(input())
        for j in range(rag):
            serach = int(input())
            find = binary_search_des(lst,serach,0,len(lst))
            if find != None:
                lst2.append(find)
        for z in lst2:
            o = 100 - z
            print(o)