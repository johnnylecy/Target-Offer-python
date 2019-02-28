def quick_sort(lst, l ,r):
    if l < r:
        pivot = partition(lst, l, r)
        quick_sort(lst, l, pivot)
        quick_sort(lst, pivot+1, r)


def partition(lst, l, r):
    if l >= r: 
        return
    i = l
    pivot = lst[l]
    for j in range(r, l, -1):
        if lst[j] <= pivot:
            i -= 1
            lst[i], lst[j] = lst[j], lst[i]
        lst[j-1], pivot =  pivot, lst[j-1]
        return i
def quick_sort(lst, l ,r):
    if l < r:
        q = partition(lst, l, r)
        quick_sort(lst, l, q)
        quick_sort(lst, q+1, r)


    
if __name__ == '__main__':
    lst = [10, 2, 3, 7, 3, 9, 0, -1, 5]
    print(quick_sort(lst, 0, len(lst)-1))



